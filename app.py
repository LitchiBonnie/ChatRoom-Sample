"""
PyChat - A Simple Real-time Chat Room
Flask application with WebSocket support for real-time messaging
"""

from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
from datetime import datetime
import uuid

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
socketio = SocketIO(app, cors_allowed_origins="*")

# Store connected users
connected_users = {}

@app.route('/')
def index():
    """Serve the main chat room page"""
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    """Handle new user connection"""
    user_id = str(uuid.uuid4())
    connected_users[user_id] = {
        'session_id': request.sid,
        'connected_at': datetime.now()
    }
    
    # Notify all users that someone joined
    emit('user_status', {
        'message': 'A user has joined the chat',
        'timestamp': datetime.now().strftime('%H:%M:%S'),
        'type': 'join'
    }, broadcast=True)
    
    print(f"User {user_id} connected")

@socketio.on('disconnect')
def handle_disconnect():
    """Handle user disconnection"""
    # Find and remove user from connected_users
    user_to_remove = None
    for user_id, user_info in connected_users.items():
        if user_info['session_id'] == request.sid:
            user_to_remove = user_id
            break
    
    if user_to_remove:
        del connected_users[user_to_remove]
        
        # Notify all users that someone left
        emit('user_status', {
            'message': 'A user has left the chat',
            'timestamp': datetime.now().strftime('%H:%M:%S'),
            'type': 'leave'
        }, broadcast=True)
        
        print(f"User {user_to_remove} disconnected")

@socketio.on('send_message')
def handle_message(data):
    """Handle incoming chat messages"""
    # Validate message data
    if not data.get('message') or not data.get('message').strip():
        return  # Don't send empty messages
    
    # Create message object with timestamp
    message_data = {
        'message': data['message'].strip(),
        'avatar': data.get('avatar', '😀'),  # Default to 😀 emoji if none selected
        'timestamp': datetime.now().strftime('%H:%M:%S'),
        'sender_id': request.sid  # Use session ID to identify sender
    }
    
    # Broadcast message to all connected users
    emit('receive_message', message_data, broadcast=True)
    
    print(f"Message sent: {message_data['message']} with avatar: {message_data['avatar']}")

if __name__ == '__main__':
    socketio.run(app, debug=True, host='127.0.0.1', port=5000)
