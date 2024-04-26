// Import required modules
const express = require('express');
const http = require('http');
const socketIo = require('socket.io');

// Create an Express app
const app = express();
const server = http.createServer(app);
const io = socketIo(server);

// Define a port for the server to listen on
const port = process.env.PORT || 3000;

// Define a route to serve the frontend client
app.use(express.static('../client'));

// Define a WebSocket connection handler
io.on('connection', (socket) => {
    console.log('A user connected');

    // Event listener for receiving chat messages
    socket.on('chat message', (message) => {
        console.log('Message received:', message);
        // Broadcast the received message to all connected clients
        io.emit('chat message', message);
    });

    // Event listener for handling disconnection
    socket.on('disconnect', () => {
        console.log('User disconnected');
    });
});

// Start the server and listen for incoming connections
server.listen(port, () => {
    console.log(`Server listening at http://localhost:${port}`);
});
