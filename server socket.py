import socket

# Define server address and port
SERVER_HOST = '0.0.0.0'  # Listen on all interfaces
SERVER_PORT = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(1)
print("Server is listening on port:", SERVER_PORT)
# Accept a connection
client_socket, client_address = server_socket.accept()
print(f"Connection from {client_address}")

while True:
    data = client_socket.recv(1024)
    if not data:
        break
    print(f"Received: {data.decode()}")

client_socket.close()
server_socket.close()

