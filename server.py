import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(('localhost', 12345)) # HOST, PORT

server_socket.listen()

print("Server is ready to connect...")

client_socket, address = server_socket.accept()

print(f"Connection Accepted from {address}")

message = client_socket.recv(1024).decode("utf-8") #1024 bite amount, encode
print(f"Client message: {message}")

client_socket.send("Message received".encode("utf-8"))

client_socket.close()
server_socket.close()
