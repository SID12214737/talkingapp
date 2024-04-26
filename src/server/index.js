// Import required modules
const express = require('express');

// Create an Express app
const app = express();

// Define a port for the server to listen on
const port = process.env.PORT || 3000;

// Define a route to handle incoming requests
app.get('/', (req, res) => {
    res.send('Hello World!');
});

// Start the server and listen for incoming connections
app.listen(port, () => {
    console.log(`Server listening at http://localhost:${port}`);
});
