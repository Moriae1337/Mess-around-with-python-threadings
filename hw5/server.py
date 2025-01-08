import socket

# Constants
PORT = 8080
BUFFER_SIZE = 1024
ADDRESS = "0.0.0.0"

def main():
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("Socket created successfully.")

        server_socket.bind((ADDRESS, PORT))
        print(f"Socket bound to port {PORT}.")

        server_socket.listen(3)
        print(f"Server is listening on port {PORT}...")

        client_socket, client_address = server_socket.accept()
        print(f"Connection accepted from client: {client_address}")

        buffer = client_socket.recv(BUFFER_SIZE).decode("utf-8")
        if buffer:
            print(f"Message received: {buffer}")
        else:
            print("Failed to read data from client.")

        response = "Hello from server!"
        client_socket.send(response.encode("utf-8"))
        print("Response sent to client.")

        client_socket.close()
        print("Client connection closed.")

    except socket.error as e:
        print(f"Socket error: {e}")
    except KeyboardInterrupt:
        print("\nServer interrupted by user.")
    finally:
        server_socket.close()
        print("Server shut down.")

if __name__ == "__main__":
    main()
