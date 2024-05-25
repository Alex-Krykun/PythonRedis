import socket


def main():
    server_socket = socket.create_server(("localhost", 6379))
    client_socket, address = server_socket.accept()

    while True:
        request: bytes = client_socket.recv(512)
        data_str: str = request.decode() 

        if "ping" in data_str.lower():
            client_socket.send("+PONG\r\n".encode())


if __name__ == "__main__":
    main()
