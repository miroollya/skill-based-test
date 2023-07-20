import socket

def main():
    server_address = "192.168.152.128"
    server_port = 8888


    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:

        client_socket.connect((server_address, server_port))


        quote = client_socket.recv(1024).decode()

        print("hi!!! have a great day :)")
        print("Quote of the Day:", quote)

    except Exception as e:
        print("Error:", e)

    finally:

        client_socket.close()

if __name__ == "__main__":
    main()

