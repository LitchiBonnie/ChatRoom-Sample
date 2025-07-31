/**
 * PyChat - Frontend JavaScript
 * Handles WebSocket connections, avatar selection, and message sending/receiving
 */

class ChatApp {
    constructor() {
        this.socket = null;
        this.selectedAvatar = '😀'; // Default emoji avatar
        this.chatWindow = document.getElementById('chatWindow');
        this.messageInput = document.getElementById('messageInput');
        this.sendButton = document.getElementById('sendButton');
        
        this.init();
    }
    
    init() {
        // Initialize Socket.IO connection
        this.socket = io();
        
        // Set up event listeners
        this.setupSocketEvents();
        this.setupUIEvents();
        
        // Select default avatar
        this.selectAvatar('😀');
        
        console.log('PyChat initialized successfully');
    }
    
    setupSocketEvents() {
        // Connection established
        this.socket.on('connect', () => {
            console.log('Connected to server');
            this.addSystemMessage('Connected to chat room');
        });
        
        // Connection lost
        this.socket.on('disconnect', () => {
            console.log('Disconnected from server');
            this.addSystemMessage('Disconnected from chat room');
        });
        
        // Receive new message
        this.socket.on('receive_message', (data) => {
            this.displayMessage(data);
        });
        
        // User status updates
        this.socket.on('user_status', (data) => {
            this.addSystemMessage(data.message);
        });
    }
    
    setupUIEvents() {
        // Avatar selection
        document.querySelectorAll('.avatar-option').forEach(option => {
            option.addEventListener('click', (e) => {
                const avatarId = option.getAttribute('data-avatar');
                this.selectAvatar(avatarId);
            });
        });
        
        // Send button click
        this.sendButton.addEventListener('click', () => {
            this.sendMessage();
        });
        
        // Enter key press in message input
        this.messageInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') {
                this.sendMessage();
            }
        });
        
        // Focus on message input when page loads
        this.messageInput.focus();
    }
    
    selectAvatar(avatarId) {
        // Remove selected class from all avatars
        document.querySelectorAll('.avatar-option').forEach(option => {
            option.classList.remove('selected');
        });
        
        // Add selected class to chosen avatar
        const selectedOption = document.querySelector(`[data-avatar="${avatarId}"]`);
        if (selectedOption) {
            selectedOption.classList.add('selected');
            this.selectedAvatar = avatarId;
            console.log(`Avatar selected: ${avatarId}`);
        }
    }
    
    sendMessage() {
        const message = this.messageInput.value.trim();
        
        // Validate message
        if (!message) {
            console.log('Cannot send empty message');
            return;
        }
        
        // Prepare message data
        const messageData = {
            message: message,
            avatar: this.selectedAvatar
        };
        
        // Send message to server
        this.socket.emit('send_message', messageData);
        
        // Clear input field
        this.messageInput.value = '';
        this.messageInput.focus();
        
        console.log('Message sent:', messageData);
    }
    
    displayMessage(data) {
        const messageElement = document.createElement('div');
        messageElement.className = 'message';
        
        // Check if this is our own message
        const isOwnMessage = data.sender_id === this.socket.id;
        if (isOwnMessage) {
            messageElement.classList.add('own');
        }
        
        // Create message content
        const messageContent = document.createElement('div');
        messageContent.className = 'message-content';
        
        // Create avatar element
        const avatarElement = document.createElement('span');
        avatarElement.className = 'avatar emoji-avatar';
        avatarElement.textContent = data.avatar;
        avatarElement.title = `Avatar: ${data.avatar}`;
        
        // Create message text container
        const messageTextContainer = document.createElement('div');
        messageTextContainer.className = 'message-text';
        
        const messageText = document.createElement('div');
        messageText.textContent = data.message;
        
        const timestamp = document.createElement('div');
        timestamp.className = 'timestamp';
        timestamp.textContent = data.timestamp;
        
        messageTextContainer.appendChild(messageText);
        messageTextContainer.appendChild(timestamp);
        
        // Append elements to message content
        messageContent.appendChild(avatarElement);
        messageContent.appendChild(messageTextContainer);
        
        // Append message content to message element
        messageElement.appendChild(messageContent);
        
        // Add message to chat window
        this.chatWindow.appendChild(messageElement);
        
        // Scroll to bottom
        this.scrollToBottom();
    }
    
    addSystemMessage(message) {
        const messageElement = document.createElement('div');
        messageElement.className = 'message system';
        
        const messageContent = document.createElement('div');
        messageContent.className = 'message-content';
        
        const messageText = document.createElement('div');
        messageText.textContent = message;
        
        const timestamp = document.createElement('div');
        timestamp.className = 'timestamp';
        timestamp.textContent = new Date().toLocaleTimeString('en-US', {
            hour12: false,
            hour: '2-digit',
            minute: '2-digit',
            second: '2-digit'
        });
        
        messageContent.appendChild(messageText);
        messageContent.appendChild(timestamp);
        messageElement.appendChild(messageContent);
        
        this.chatWindow.appendChild(messageElement);
        this.scrollToBottom();
    }
    
    scrollToBottom() {
        // Smooth scroll to bottom of chat window
        this.chatWindow.scrollTop = this.chatWindow.scrollHeight;
    }
}

// Initialize the chat application when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    new ChatApp();
});
