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
    return rand() % 900 + 100; // Generate a random number between 100 and 999
}

int main() {
    srand(time(0)); // Seed the random number generator with the current time

    int server_socket, client_socket;
    struct sockaddr_in server_addr, client_addr;
    socklen_t client_addr_len = sizeof(client_addr);

    // Create socket
    server_socket = socket(AF_INET, SOCK_STREAM, 0);
    if (server_socket < 0) {
        perror("Error creating socket");
        return 1;
    }

    // Bind the socket to a specific IP and port
    server_addr.sin_family = AF_INET;
    server_addr.sin_addr.s_addr = INADDR_ANY;
    server_addr.sin_port = htons(PORT);

    if (bind(server_socket, (struct sockaddr*)&server_addr, sizeof(server_addr)) < 0) {
        perror("Error binding socket");
        return 1;
    }

    // Start listening for incoming connections
    if (listen(server_socket, 5) < 0) {
        perror("Error listening");
        return 1;
    }

    printf("Server is listening on port %d...\n", PORT);

    // Register the signal handler for Ctrl+C (SIGINT)
    struct sigaction sa;
    sa.sa_handler = handle_interrupt;
    sigemptyset(&sa.sa_mask);
    sa.sa_flags = 0;
    sigaction(SIGINT, &sa, NULL);

    while (!stop) {
        // Accept client connection
        client_socket = accept(server_socket, (struct sockaddr*)&client_addr, &client_addr_len);
        if (client_socket < 0) {
            perror("Error accepting client connection");
            continue; // Try accepting the next connection
        }

        // Generate a random number
        int random_number = generate_random_number();

        // Send the random number to the client
        send(client_socket, &random_number, sizeof(random_number), 0);
        printf("Random number %d sent to the client.\n", random_number);

        // Close the client socket
        close(client_socket);
    }

    // Close the server socket
    close(server_socket);

    return 0;
}
