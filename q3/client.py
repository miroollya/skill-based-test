import socket

def main():
    server_address = "192.168.152.128"
    server_port = 8443

    
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        
        client_socket.connect((server_address, server_port))

       
        pressure_bar = float(input("Enter the pressure value in bar: "))

       
        client_socket.sendall(str(pressure_bar).encode())

        
        data = client_socket.recv(1024)
        pressure_atm = float(data.decode())

        
        print(f"{pressure_bar} bar is approximately {pressure_atm:.4f} atm")

    except Exception as e:
        print("An error occurred:", e)

    finally:
        
        client_socket.close()

if __name__ == "__main__":
    main()
