import socket

def main():
    server_address = "192.168.152.128"
    server_port = 8888

    # Create a TCP/IP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to the server
        client_socket.connect((server_address, server_port))

        # Receive the quote from the server
        quote = client_socket.recv(1024).decode()

        # Display the received quote
        print("Quote of the Day:", quote)

    except Exception as e:
        print("Error:", e)

    finally:
        # Close the socket
        client_socket.close()

if __name__ == "__main__":
    main()
