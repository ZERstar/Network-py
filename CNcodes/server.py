import socketserver

class Handler_TCPServer(socketserver.BaseRequestHandler):

    def handle(self) :
        self.data = self.request.recv(1024).strip()
        print("{} sent: ".format(self.client_address[0]))
        print(self.data)
        self.request.sendall("Ack from TCP server".encode())

if __name__ == "__main__":
    HOST , PORT = "localhost", 9999
    tcp_server = socketserver.TCPServer((HOST , PORT), Handler_TCPServer)
    tcp_server.server_forever()