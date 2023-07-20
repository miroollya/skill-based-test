import socket

def bar_to_atm(pressure_bar):
    return pressure_bar / 1.01325

def main():
    server_address = "192.168.152.128"
    server_port = 8443

    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    
    server_socket.bind((server_address, server_port))

    
    server_socket.listen(1)

    print("Server is listening on port", server_port)

    while True:
        
        print("Waiting for a connection...")
        client_socket, client_address = server_socket.accept()

        try:
            
            data = client_socket.recv(1024)
            pressure_bar = float(data.decode())

           
            pressure_atm = bar_to_atm(pressure_bar)

           
            client_socket.sendall(str(pressure_atm).encode())

        except ValueError:
            client_socket.sendall(b"Invalid input. Please enter a valid pressure value in bar.")

        finally:
            
            client_socket.close()

if __name__ == "__main__":
    main()
