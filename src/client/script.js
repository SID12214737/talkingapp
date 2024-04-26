// Establish WebSocket connection with the server
const socket = io();

// Get references to HTML elements
const chatWindow = document.getElementById('chat-window');
const messageInput = document.getElementById('message-input');
const sendButton = document.getElementById('send-button');

// Event listener for sending messages
sendButton.addEventListener('click', () => {
    const message = messageInput.value;
    sendMessage(message);
});

// Function to send a message to the server
function sendMessage(message) {
    // Emit a 'chat message' event to the server with the message content
    socket.emit('chat message', message);
    // Clear the message input field
    messageInput.value = '';
}

// Event listener for receiving messages from the server
socket.on('chat message', (message) => {
    // Create a new <div> element to display the message
    const messageElement = document.createElement('div');
    messageElement.textContent = message;
    // Append the message element to the chat window
    chatWindow.appendChild(messageElement);
    // Scroll to the bottom of the chat window
    chatWindow.scrollTop = chatWindow.scrollHeight;
});

// Import the simple-peer library
const SimplePeer = require('simple-peer');

// Create a new instance of SimplePeer
const peer = new SimplePeer({ initiator: true });

// Event listener for when a connection is established
peer.on('connect', () => {
    console.log('Connection established!');
    // Now you can start sending audio/video data
});

// Event listener for when data is received
peer.on('data', (data) => {
    console.log('Received data:', data);
});

// Event listener for when the connection is closed
peer.on('close', () => {
    console.log('Connection closed');
});
