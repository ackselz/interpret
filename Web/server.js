const express = require('express');
const WebSocket = require('ws');
const app = express();
app.use(express.json({ extended: false }));
app.use(express.static('public'));

var port = process.env.PORT || 3000;
console.log("Server started on port " + port)
const server = new WebSocket.Server({ server: app.listen(port) });

server.on('connection', (socket) => {
  socket.on('message', (msg) => {
    server.clients.forEach(client => {
      client.send(msg);
    })
  });
});