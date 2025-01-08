import socket

PORT = 8080
SERVER_ADDRESS = "127.0.0.1"

def main():
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("Socket successfully created.")

        server_address = (SERVER_ADDRESS, PORT)

        client_socket.connect(server_address)
        print(f"Client connected to server at {SERVER_ADDRESS}:{PORT}")

    except ConnectionRefusedError:
        print("Connection failed: The server is not available.")
    except socket.error as e:
        print(f"Socket error: {e}")
    finally:
        client_socket.close()
        print("Socket closed.")

if __name__ == "__main__":
    main()
