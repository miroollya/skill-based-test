import socket
import threading
import random

QUOTES = [
    "Cita-cita tinggi menghasilkan pengorbanan yang besar. - Tunku Abdul Rahman",
    "Hidup ini adalah tentang memberi, bukan hanya menerima. - Tun Abdul Razak",
    "Biar mati anak, jangan mati adat. - Hang Tuah",
    "Air dicincang tak akan putus. - Hang Jebat",
    "Raja adil raja disembah, raja zalim raja disanggah. - Hang Nadim",
    "Tak kenal maka tak cinta. - Raja Bersiong",
    "Raja dan rakyat berpisah tiada. - Sultan Mahmud Mangkat Dijulang",
    "Kerana nila setitik, rosak susu sebelanga. - Sultan Alauddin Riayat Shah",
    "Berguru pandai, berguru mulia, berguru dari sejauh mana pun. - Hang Li Po",
    "Jika benih tidak kuat, pohon tidak akan berkembang. - P. Ramlee",
    "It's just a bad day, not a bad life. - Miroolya"
]

def handle_client(client_socket):
    try:
        
        random_quote = random.choice(QUOTES)

        
        client_socket.sendall(random_quote.encode())

    except Exception as e:
        print("Error handling client:", e)

    finally:
        
        client_socket.close()

def main():
    server_address = "192.168.152.128"
    server_port = 8888

   
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    
    server_socket.bind((server_address, server_port))

   
    server_socket.listen(5)

    print("Server is listening on IP", server_address, "and port", server_port)

    while True:
        
        client_socket, client_address = server_socket.accept()
        print("Accepted connection from", client_address)

        
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

if __name__ == "__main__":
    main()
