import socket

host_ip , server_port = "127.0.0.1" , 9999
data = "Hey?\n"

tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    tcp_client.connect((host_ip , server_port))
    tcp_client.sendall(data.encode())

    received = tcp_client.recv(1024)

finally:
    tcp_client.close()

print("Bytes sent: {}".format(data))
print("Bytes Received: {}".format(received.decode()))


