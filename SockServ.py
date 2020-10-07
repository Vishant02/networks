import socketserver
import threading
import http.server


class EchoHandler(socketserver.BaseRequestHandler):

    def handle(self):
        print("got connection from ",self.client_address)

        data = 'dummy'

        while len(data):
            data = self.request.recv(1024)
            data = data.decode("utf-8")
            self.request.send(bytes(data,"utf-8"))

            print("Client left")



servAddr = ("localhost",9000)
server = socketserver.TCPServer(servAddr,EchoHandler)
server.serve_forever()