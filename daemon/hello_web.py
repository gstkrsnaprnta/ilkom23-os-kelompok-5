from http.server import SimpleHTTPRequestHandler, HTTPServer

class HelloHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"<html><body><h1>Hello Web!</h1></body></html>")

def run(server_class=HTTPServer, handler_class=HelloHandler):
    server_address = ("", 8080)  # Port 8080
    httpd = server_class(server_address, handler_class)
    print("Starting httpd server on port 8080...")
    httpd.serve_forever()

if __name__ == "__main__":  # Corrected double underscores
    run()
 