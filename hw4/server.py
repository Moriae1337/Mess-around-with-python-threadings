import socket

PORT = 8080
ADDRESS = "0.0.0.0"

def main():
    try:

        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("Socket successfully created.")

        server_socket.bind((ADDRESS, PORT))
        print(f"Server is listening on port {PORT}...")

        server_socket.listen(3)

        print("Waiting for a client connection...")
        client_socket, client_address = server_socket.accept()
        print(f"Client connected from {client_address}")

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
