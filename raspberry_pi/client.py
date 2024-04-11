from http.server import BaseHTTPRequestHandler, HTTPServer
import socket

HOST_NAME = socket.gethostbyname(socket.gethostname())
PORT = 8080

class HTTPHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        html = """
        <html lang="en">
            <style>
                body {
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    font-size: 4rem;
                    font-family: monospace;
                }
                #data {
                    padding: 4rem;
                }
            </style>
            <body>
                <div id='data'>></div>
                <script>
                    const pingInterval = setInterval(() => {
                        ws.send('ping');
                    }, 30000); // Send a ping message every 30 seconds

                    const ws = new WebSocket('ws://' + location.hostname + ':8001');

                    ws.addEventListener('message', ({data}) => {
                        if (data === 'pong') return;
                        const currentContent = document.getElementById('data').innerHTML;
                        document.getElementById('data').innerHTML = currentContent + ' ' + data;
                    });

                    // Handle WebSocket close event
                    ws.addEventListener('close', () => {
                        clearInterval(pingInterval); // Stop sending ping messages
                    });
                </script>
            </body>
        </html>
        """

        self.wfile.write(bytes(html, 'utf-8'))

if __name__ == "__main__":        
    http_server = HTTPServer((HOST_NAME, PORT), HTTPHandler)
    print("Server started http://%s:%s" % (HOST_NAME, PORT))

    try:
        http_server.serve_forever()
    except KeyboardInterrupt:
        pass

    http_server.server_close()
    print("Server stopped.")
