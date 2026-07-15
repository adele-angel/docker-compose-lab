from http.server import SimpleHTTPRequestHandler, HTTPServer

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
print("App running on port 8000...")
server.serve_forever()
