import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect(("localhost", 12345))

client_socket.send("Hi, server!".encode("utf-8"))

message = client_socket.recv(1024).decode("utf-8")
print(f"Server message: {message}")

client_socket.close()