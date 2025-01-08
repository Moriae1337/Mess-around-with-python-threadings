import socket
import struct

PORT = 8080
SERVER_ADDRESS = "127.0.0.1"
BUFFER_SIZE = 1024

def send_message(sock, message):
    message_bytes = message.encode('utf-8')
    message_length = struct.pack('!I', len(message_bytes))
    sock.sendall(message_length)
    sock.sendall(message_bytes)

def receive_message(sock):
    length_prefix = sock.recv(4)
    if not length_prefix:
        raise ConnectionError("Connection closed while receiving message length.")
    message_length = struct.unpack('!I', length_prefix)[0]
    data = b''
    while len(data) < message_length:
        chunk = sock.recv(min(BUFFER_SIZE, message_length - len(data)))
        if not chunk:
            raise ConnectionError("Connection closed while receiving message data.")
        data += chunk

    return data.decode('utf-8')

def main():
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        print(f"Connecting to {SERVER_ADDRESS}:{PORT}...")
        client_socket.connect((SERVER_ADDRESS, PORT))
        print("Connected to the server.")

        for i in range(100):
            message = f"Message: {i + 1}"
            send_message(client_socket, message)
            print(f"Client sent: {message}")

            received_message = receive_message(client_socket)
            print(f"Client received: {received_message}")

    except ConnectionError as e:
        print(f"Connection error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        
        client_socket.close()
        print("Connection closed.")

if __name__ == "__main__":
    main()
