from http.server import BaseHTTPRequestHandler, HTTPServer

HOST_NAME = "localhost"
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
                }
            </style>
            <body>
                <div id='data'>></div>
                <script>
                    var ws = new WebSocket('ws://localhost:8001');

                    ws.addEventListener('message', ({data}) => {
                        const currentContent = document.getElementById('data').innerHTML;
                        document.getElementById('data').innerHTML = currentContent + ' ' + data;
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