#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <arpa/inet.h>
#include <unistd.h>
#include <signal.h>

#define PORT 8443

volatile sig_atomic_t stop = 0;

void handle_interrupt(int signum) {
    stop = 1;
}

int main() {
    int client_socket;
    struct sockaddr_in server_addr;

    
    client_socket = socket(AF_INET, SOCK_STREAM, 0);
    if (client_socket < 0) {
        perror("Error creating socket");
        return 1;
    }

    
    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(PORT);

    if (inet_pton(AF_INET, "192.168.152.128", &server_addr.sin_addr) <= 0) {
        perror("Invalid address/ Address not supported");
        return 1;
    }

    if (connect(client_socket, (struct sockaddr*)&server_addr, sizeof(server_addr)) < 0) {
        perror("Connection failed");
        return 1;
    }

   
    signal(SIGINT, handle_interrupt);

    while (!stop) {
        
        int random_number;
        if (recv(client_socket, &random_number, sizeof(random_number), 0) <= 0) {
           
            break;
        }

        printf("Received random number from server: %d\n", random_number);
    }

    
    close(client_socket);

    return 0;
}
