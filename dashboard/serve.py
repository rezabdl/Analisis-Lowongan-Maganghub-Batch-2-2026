import http.server
import socketserver
import os
import sys

PORT = 8080
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def end_headers(self):
        # Enable CORS and disable aggressive caching during prototyping
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        super().end_headers()

def run_server():
    port = PORT
    for attempt in range(5):
        try:
            with socketserver.TCPServer(("", port), Handler) as httpd:
                print(f"MagangHub Batch 2 2026 Prototype Server running at:")
                print(f"http://localhost:{port}/")
                print(f"Serving directory: {DIRECTORY}")
                sys.stdout.flush()
                httpd.serve_forever()
                break
        except OSError:
            port += 1

if __name__ == "__main__":
    run_server()
