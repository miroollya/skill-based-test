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

    // Create socket
    client_socket = socket(AF_INET, SOCK_STREAM, 0);
    if (client_socket < 0) {
        perror("Error creating socket");
        return 1;
    }

    // Connect to the server
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

    // Register the signal handler for Ctrl+C (SIGINT)
    signal(SIGINT, handle_interrupt);

    while (!stop) {
        // Receive the random number from the server
        int random_number;
        if (recv(client_socket, &random_number, sizeof(random_number), 0) <= 0) {
            // Connection with the server is closed, exit the loop
            break;
        }

        printf("Received random number from server: %d\n", random_number);
    }

    // Close the socket
    close(client_socket);

    return 0;
}
