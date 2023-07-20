import socket
import threading
import random

QUOTES = [
    "Be yourself; everyone else is already taken. - Oscar Wilde",
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Life is what happens when you're busy making other plans. - John Lennon",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "In the end, it's not the years in your life that count. It's the life in your years. - Abraham Lincoln",
    "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
    "Believe you can and you're halfway there. - Theodore Roosevelt",
    "Life is 10% what happens to you and 90% how you react to it. - Charles R. Swindoll",
    "The journey of a thousand miles begins with one step. - Lao Tzu",
    "It's just a bad day, not a bad life. - Miroolya"
]

def handle_client(client_socket):
    try:
        # Choose a random quote from the list
        random_quote = random.choice(QUOTES)

        # Send the quote to the client
        client_socket.sendall(random_quote.encode())

    except Exception as e:
        print("Error handling client:", e)

    finally:
        # Close the client socket
        client_socket.close()

def main():
    server_address = "192.168.152.128"
    server_port = 8888

    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the server address and port
    server_socket.bind((server_address, server_port))

    # Start listening for incoming connections
    server_socket.listen(5)

    print("Server is listening on IP", server_address, "and port", server_port)

    while True:
        # Wait for a connection
        client_socket, client_address = server_socket.accept()
        print("Accepted connection from", client_address)

        # Create a new thread to handle the client request
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

if __name__ == "__main__":
    main()
