#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <arpa/inet.h>
#include <unistd.h>
#include <time.h>
#include <signal.h>

#define PORT 8443

volatile sig_atomic_t stop = 0;

void handle_interrupt(int signum) {
    stop = 1;
}

int generate_random_number() {
    return rand() % 900 + 100; 
}

int main() {
    srand(time(0)); 

    int server_socket, client_socket;
    struct sockaddr_in server_addr, client_addr;
    socklen_t client_addr_len = sizeof(client_addr);

    
    server_socket = socket(AF_INET, SOCK_STREAM, 0);
    if (server_socket < 0) {
        perror("Error creating socket");
        return 1;
    }

    
    server_addr.sin_family = AF_INET;
    server_addr.sin_addr.s_addr = INADDR_ANY;
    server_addr.sin_port = htons(PORT);

    if (bind(server_socket, (struct sockaddr*)&server_addr, sizeof(server_addr)) < 0) {
        perror("Error binding socket");
        return 1;
    }

    
    if (listen(server_socket, 5) < 0) {
        perror("Error listening");
        return 1;
    }

    printf("Server is listening on port %d...\n", PORT);

    
    struct sigaction sa;
    sa.sa_handler = handle_interrupt;
    sigemptyset(&sa.sa_mask);
    sa.sa_flags = 0;
    sigaction(SIGINT, &sa, NULL);

    while (!stop) {
        
        client_socket = accept(server_socket, (struct sockaddr*)&client_addr, &client_addr_len);
        if (client_socket < 0) {
            perror("Error accepting client connection");
            continue; 
        }

        
        int random_number = generate_random_number();

        
        send(client_socket, &random_number, sizeof(random_number), 0);
        printf("Random number %d sent to the client.\n", random_number);

        
        close(client_socket);
    }

    
    close(server_socket);

    return 0;
}
