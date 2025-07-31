# PyChat - Simple Real-time Chat Room

A modern, emoji-powered chat application built with Flask and Socket.IO for real-time messaging.

## Features

- 🚀 Real-time messaging using WebSocket connections
- 😀 Emoji avatars for personalized chat experience
- 📱 Responsive design that works on desktop and mobile
- 🎨 Beautiful gradient UI with smooth animations
- 👥 User join/leave notifications
- ⏰ Timestamps for all messages
- 🔒 Simple and secure Flask backend

## Avatar Options

Choose from 6 fun emoji avatars:
- 😀 Happy Face
- 😎 Cool Sunglasses
- 🤖 Robot
- 🐱 Cat
- 🚀 Rocket
- ⭐ Star

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## Installation

1. Clone or download this repository to your local machine

2. Navigate to the project directory:
   ```bash
   cd test
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Start the Flask application:
   ```bash
   python app.py
   ```

2. Open your web browser and navigate to:
   ```
   http://127.0.0.1:5000
   ```

3. Choose your emoji avatar by clicking on one of the options

4. Start chatting! Type your message and press Enter or click Send

5. Open multiple browser tabs or share the URL with friends to test real-time messaging

## Project Structure

```
test/
├── app.py                 # Flask application and Socket.IO server
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── static/
│   ├── css/
│   │   └── style.css     # Application styles
│   ├── images/
│   │   └── avatar1.svg   # Legacy avatar file (not used)
│   └── js/
│       └── chat.js       # Frontend JavaScript
└── templates/
    └── index.html        # Main chat interface
```

## Dependencies

- **Flask** - Web framework for Python
- **Flask-SocketIO** - WebSocket support for real-time communication
- **python-socketio** - Socket.IO server implementation
- **python-engineio** - Engine.IO server implementation

## Technical Details

### Backend (Flask + Socket.IO)
- Handles WebSocket connections for real-time messaging
- Manages user sessions and connection state
- Broadcasts messages to all connected clients
- Provides join/leave notifications

### Frontend (HTML + CSS + JavaScript)
- Modern, responsive design with CSS Grid and Flexbox
- Socket.IO client for real-time communication
- Emoji avatar selection system
- Message display with timestamps and user identification

### Features
- **Real-time Communication**: Messages appear instantly for all users
- **User Management**: Tracks connected users and handles disconnections gracefully
- **Message Validation**: Prevents empty messages from being sent
- **Responsive Design**: Works on desktop, tablet, and mobile devices
- **Visual Feedback**: Hover effects, animations, and clear visual indicators

## Customization

### Adding More Emoji Avatars

To add more emoji avatars, edit the `templates/index.html` file and add new avatar options:

```html
<div class="avatar-option" data-avatar="🎯" data-emoji="🎯">
    <span class="avatar-emoji">🎯</span>
</div>
```

### Styling Changes

Modify `static/css/style.css` to customize:
- Colors and gradients
- Font sizes and families
- Layout and spacing
- Animations and transitions

### Server Configuration

In `app.py`, you can modify:
- Server port (default: 5000)
- Host address (default: 127.0.0.1)
- CORS settings
- Secret key for sessions

## Browser Compatibility

- Chrome 60+
- Firefox 55+
- Safari 12+
- Edge 79+

## Troubleshooting

### Common Issues

1. **Port already in use**: If you get a port error, either:
   - Stop other applications using port 5000
   - Change the port in `app.py`: `socketio.run(app, port=5001)`

2. **Dependencies not found**: Make sure you've installed requirements:
   ```bash
   pip install -r requirements.txt
   ```

3. **Emojis not displaying**: Ensure your browser supports modern emoji standards

4. **Connection issues**: Check that your firewall isn't blocking the connection

## License

This project is open source and available under the MIT License.

## Contributing

Feel free to fork this project and submit pull requests for improvements!

## Future Enhancements

Potential features to add:
- User nicknames
- Private messaging
- Chat rooms/channels
- Message history persistence
- File sharing
- Voice messages
- Dark/light theme toggle
