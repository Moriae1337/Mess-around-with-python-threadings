import socket
import struct

PORT = 8080
BUFFER_SIZE = 1024

def send_message(client_socket, message):

    message_bytes = message.encode('utf-8')
    message_length = struct.pack('!I', len(message_bytes))
    client_socket.sendall(message_length)
    client_socket.sendall(message_bytes)
def receive_message(client_socket):

    length_prefix = client_socket.recv(4)
    if not length_prefix:
        return None
    message_length = struct.unpack('!I', length_prefix)[0]

    data = b''
    while len(data) < message_length:
        chunk = client_socket.recv(min(BUFFER_SIZE, message_length - len(data)))
        if not chunk:
            raise ConnectionError("Connection closed during message reception")
        data += chunk

    return data.decode('utf-8')

def main():

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("0.0.0.0", PORT))
    server_socket.listen(socket.SOMAXCONN)
    print(f"Server is listening on port {PORT}...")

    try:
        client_socket, client_address = server_socket.accept()
        print(f"Connection accepted from {client_address}")

        for i in range(100):

            received_message = receive_message(client_socket)
            print(f"Server received: {received_message}")

            response = f"Confirm: {received_message}"
            send_message(client_socket, response)

    except (ConnectionError, KeyboardInterrupt) as e:
        print(f"Server error: {e}")
    finally:
        client_socket.close()
        server_socket.close()
        print("Server has closed the connection.")

if __name__ == "__main__":
    main()
