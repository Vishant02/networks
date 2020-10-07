from http.server import HTTPServer,BaseHTTPRequestHandler


tasklist = ['Task 1','Task 2','Task 3']

class requestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type','text/html')
        self.end_headers()

        output = ''
        output += '<html><body>'
        output += '<h1>Task List</h1>'
        for task in tasklist:
            output += task
            output += '</br>'
            output += '</body></html>'
        self.wfile.write(output.encode())


def main():
    PORT = 9000
    server_address = ('localhost',PORT)
    server = HTTPServer(server_address, requestHandler)
    print('Server running on port %s' % PORT)
    server.serve_forever()

main()
