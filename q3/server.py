import socket

def bar_to_atm(pressure_bar):
    return pressure_bar / 1.01325

def main():
    server_address = "192.168.152.128"
    server_port = 8443

    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the server address and port
    server_socket.bind((server_address, server_port))

    # Start listening for incoming connections
    server_socket.listen(1)

    print("Server is listening on port", server_port)

    while True:
        # Wait for a connection
        print("Waiting for a connection...")
        client_socket, client_address = server_socket.accept()

        try:
            # Receive the pressure value from the client
            data = client_socket.recv(1024)
            pressure_bar = float(data.decode())

            # Convert pressure to atmosphere-standard (atm)
            pressure_atm = bar_to_atm(pressure_bar)

            # Send the converted value back to the client
            client_socket.sendall(str(pressure_atm).encode())

        except ValueError:
            client_socket.sendall(b"Invalid input. Please enter a valid pressure value in bar.")

        finally:
            # Close the connection
            client_socket.close()

if __name__ == "__main__":
    main()
