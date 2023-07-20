import socket

def main():
    server_address = "izani.synology.me"
    server_port = 8443

    try:
        
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

       
        client_socket.connect((server_address, server_port))

        print("Connected to the server!")

        
        student_id = "2021454448"

       
        client_socket.sendall(student_id.encode())

       
        response = client_socket.recv(1024).decode()
        print("Server response:", response)

       
        client_socket.close()

    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()
