import socket

PORT = 8080
BUFFER_SIZE = 1024
SERVER_ADDRESS = "127.0.0.1"

def main():
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("Socket successfully created.")

        server_address = (SERVER_ADDRESS, PORT)

        client_socket.connect(server_address)
        print("Connected to server.")

        message = "Hallo, am Apparat ist Yedynach Dmytro."
        client_socket.send(message.encode("utf-8"))
        print("Message sent to server.")

        response = client_socket.recv(BUFFER_SIZE).decode("utf-8")
        print(f"Response from server: {response}")

    except socket.error as e:
        print(f"Socket error: {e}")

    finally:
        client_socket.close()
        print("Connection closed.")

if __name__ == "__main__":
    main()
