from http.server import BaseHTTPRequestHandler, HTTPServer

class Servidor(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"Hola, este es mi servidor web en Python!</H1>")

if __name__ == "__main__":
    httpd = HTTPServer(('localhost', 8000), Servidor)
    print("Servidor iniciado en http://localhost:8000")
    httpd.serve_forever()
    