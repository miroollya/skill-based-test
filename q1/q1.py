import socket

def main():
    server_address = "izani.synology.me"
    server_port = 8443

    try:
        # Create a TCP/IP socket
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect to the server
        client_socket.connect((server_address, server_port))

        print("Connected to the server!")

        # Replace 'YOUR_UITM_STUDENT_ID' with your actual UiTM Student ID
        student_id = "2021454448"

        # Send the Student ID to the server
        client_socket.sendall(student_id.encode())

        # Receive the server's response
        response = client_socket.recv(1024).decode()
        print("Server response:", response)

        # Close the socket connection
        client_socket.close()

    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()
