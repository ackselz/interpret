const express = require('express');
const WebSocket = require('ws');

const app = express();
app.use(express.json({ extended: false }));
app.use(express.static('public'));

var port = process.env.PORT || 3000;

const wss = new WebSocket.Server({ server: app.listen(port) });

wss.on('connection', function connection(ws) {

  ws.on('error', console.error);

  ws.on('message', function message(data) {
    console.log("received message: ", data)
    wss.clients.forEach(function each(client) {
      if (client.readyState === WebSocket.OPEN) {
        client.send(data);
      }
    });
  });
});