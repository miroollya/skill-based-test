import socket

def main():
    server_address = "192.168.152.128"
    server_port = 8443

    # Create a TCP/IP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to the server
        client_socket.connect((server_address, server_port))

        # Get user input for pressure in bar
        pressure_bar = float(input("Enter the pressure value in bar: "))

        # Send the pressure value to the server
        client_socket.sendall(str(pressure_bar).encode())

        # Receive the converted value from the server
        data = client_socket.recv(1024)
        pressure_atm = float(data.decode())

        # Display the converted value
        print(f"{pressure_bar} bar is approximately {pressure_atm:.4f} atm")

    except Exception as e:
        print("An error occurred:", e)

    finally:
        # Close the socket
        client_socket.close()

if __name__ == "__main__":
    main()
