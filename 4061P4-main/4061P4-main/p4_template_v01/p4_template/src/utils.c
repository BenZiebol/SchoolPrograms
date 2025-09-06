#include "../include/utils.h"
#include "../include/server.h"
#include <arpa/inet.h> // inet_addr()
#include <netdb.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h> // bzero()
#include <sys/socket.h>
#include <unistd.h> // read(), write(), close()
#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include <dirent.h>
#include <pthread.h>
#include <errno.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <sys/time.h>
#include <fcntl.h>
#include <sys/time.h>
#include <time.h>
#include <stdbool.h>
#include <unistd.h>
#include <signal.h>
#include <limits.h>
#include <stdint.h>

//Declare a global variable to hold the file descriptor for the server socket
int master_fd;
//Mutex lock for the server socket
pthread_mutex_t socket_mutex = PTHREAD_MUTEX_INITIALIZER;
//Socket address struct for the server
struct sockaddr_in server_addr;

/*
################################################
##############Server Functions##################
################################################
*/

void init(int port) {
	
	int sd;//Socket descriptor
    struct sockaddr_in server;
    int opt = 1;//Used for setsockopt

    //Create a socket
    if ((sd = socket(AF_INET, SOCK_STREAM, 0)) < 0) {
        perror("Failed to create socket");
        exit(EXIT_FAILURE);
    }

    //Set socket options to be reusable
    if (setsockopt(sd, SOL_SOCKET, SO_REUSEADDR, &opt, sizeof(opt)) < 0) {
        perror("Failed to set socket options");
        exit(EXIT_FAILURE);
    }

    //Configure server address structure
    memset(&server, 0, sizeof(server));
    server.sin_family = AF_INET;
    server.sin_addr.s_addr = INADDR_ANY;
    server.sin_port = htons(port);

    //Bind socket to the port
    if (bind(sd, (struct sockaddr*)&server, sizeof(server)) < 0) {
        perror("Bind failed");
        exit(EXIT_FAILURE);
    }

    //Mark socket as passive with a connection queue of 5
    if (listen(sd, 5) < 0) {
        perror("Listen failed");
        exit(EXIT_FAILURE);
    }

    //Save the file descriptor globally
    master_fd = sd;
    memcpy(&server_addr, &server, sizeof(server));

    printf("UTILS.O: Server Started on Port %d\n", port);
    fflush(stdout);
	
   //TODO: create an int to hold the socket file descriptor
   //TODO: create a sockaddr_in struct to hold the address of the server
   /**********************************************
    * IMPORTANT!
    * ALL TODOS FOR THIS FUNCTION MUST BE COMPLETED FOR THE INTERIM SUBMISSION!!!!
    **********************************************/
   // TODO: Create a socket and save the file descriptor to sd (declared above)
   // TODO: Change the socket options to be reusable using setsockopt(). 
   // TODO: Bind the socket to the provided port.
   // TODO: Mark the socket as a pasive socket. (ie: a socket that will be used to receive connections.
   // We save the file descriptor to a global variable so that we can use it in accept_connection().
   // TODO: Save the file descriptor to the global variable master_fd
}


/**********************************************
 * accept_connection - takes no parameters
   - returns a file descriptor for further request processing.
   - if the return value is negative, the thread calling
     accept_connection must should ignore request.
***********************************************/
int accept_connection(void) {
    struct sockaddr_in client_addr;
    socklen_t addrlen = sizeof(client_addr);
    int newsock;

    //Acquire mutex lock
    if (pthread_mutex_lock(&socket_mutex) != 0) {
        perror("Mutex lock failed");
        return -1;
    }

    //Accept new connection
    newsock = accept(master_fd, (struct sockaddr*)&client_addr, &addrlen);
    
    //Release mutex lock
    if (pthread_mutex_unlock(&socket_mutex) != 0) {
        perror("Mutex unlock failed");
        if (newsock >= 0) {
            close(newsock);
        }
        return -1;
    }

    if (newsock < 0) {
        perror("Accept failed");
        return -1;
    }

    return newsock;
	
   //TODO: create a sockaddr_in struct to hold the address of the new connection
   /**********************************************
    * IMPORTANT!
    * ALL TODOS FOR THIS FUNCTION MUST BE COMPLETED FOR THE INTERIM SUBMISSION!!!!
    **********************************************/
   // TODO: Aquire the mutex lock
   // TODO: Accept a new connection on the passive socket and save the fd to newsock
   // TODO: Release the mutex lock
   // TODO: Return the file descriptor for the new client connection
}


/**********************************************
 * send_file_to_client
   - socket is the file descriptor for the socket
   - buffer is the file data you want to send
   - size is the size of the file you want to send
   - returns 0 on success, -1 on failure 
************************************************/
int send_file_to_client(int socket, char * buffer, int size) 
{
    //Create a packet_t to hold the packet data
	packet_t packet = {size};

    //Send the file size packet
	if (send(socket, &packet, sizeof(packet_t), 0) < 0) {
		perror("Send packet to socket error");
		return -1;
	}

    //Send the file data
	if (send(socket, buffer, size, 0) < 0) {
		perror("Send data to socket error");
		return -1;
	}
	
    //Return 0 on success, -1 on failure
	return 0;

}


/**********************************************
 * get_request_server
   - fd is the file descriptor for the socket
   - filelength is a pointer to a size_t variable that will be set to the length of the file
   - returns a pointer to the file data
************************************************/
char * get_request_server(int fd, size_t *filelength)
{
    packet_t packet;
    
    //Receive the size packet
    if (recv(fd, &packet, sizeof(packet_t), 0) < 0) {
        perror("Failed to receive size packet");
        return NULL;
    }

    //Set the file length
    *filelength = packet.size;

    //Allocate buffer for file data
    char *buffer = malloc(packet.size);
    if (buffer == NULL) {
        perror("Failed to allocate memory for file");
        return NULL;
    }

    //Receive the file data
    ssize_t received = recv(fd, buffer, packet.size, 0);
    if (received < 0 || received != packet.size) {
        perror("Failed to receive file data");
        free(buffer);
        return NULL;
    }

    return buffer;
    //TODO: create a packet_t to hold the packet data
    //TODO: receive the response packet
    //TODO: get the size of the image from the packet
    //TODO: recieve the file data and save into a buffer variable.
    //TODO: return the buffer
}


/*
################################################
##############Client Functions##################
################################################
*/

/**********************************************
 * setup_connection
   - port is the number of the port you want the client to connect to
   - initializes the connection to the server
   - if setup_connection encounters any errors, it will call exit().
************************************************/
int setup_connection(int port)
{
	int sockfd;
    struct sockaddr_in serv_addr;

    //Create socket
    if ((sockfd = socket(AF_INET, SOCK_STREAM, 0)) < 0) {
        perror("Socket creation failed");
        exit(EXIT_FAILURE);
    }

    //Initialize server address structure
    memset(&serv_addr, 0, sizeof(serv_addr));
    serv_addr.sin_family = AF_INET;
    serv_addr.sin_port = htons(port);
    
    //Convert IP address from string to binary form
    if (inet_pton(AF_INET, "127.0.0.1", &serv_addr.sin_addr) <= 0) {
        perror("Invalid address");
        exit(EXIT_FAILURE);
    }

    //Connect to the server
    if (connect(sockfd, (struct sockaddr*)&serv_addr, sizeof(serv_addr)) < 0) {
        perror("Connection failed");
        exit(EXIT_FAILURE);
    }

    return sockfd;
    //TODO: create a sockaddr_in struct to hold the address of the server
    //TODO: create a socket and save the file descriptor to sockfd
    //TODO: assign IP, PORT to the sockaddr_in struct
    //TODO: connect to the server
    //TODO: return the file descriptor for the socket
}


/**********************************************
 * send_file_to_server
   - socket is the file descriptor for the socket
   - file is the file pointer to the file you want to send
   - size is the size of the file you want to send
   - returns 0 on success, -1 on failure
************************************************/
int send_file_to_server(int socket, FILE *file, int size) 
{
    packet_t packet = {size};

    //Send the size packet
    if (send(socket, &packet, sizeof(packet_t), 0) < 0) {
        perror("Failed to send size packet");
        return -1;
    }

    //Allocate buffer for file data
    char *buffer = malloc(size);
    if (buffer == NULL) {
        perror("Failed to allocate memory for file");
        return -1;
    }

    //Read file into buffer
    if (fread(buffer, 1, size, file) != size) {
        perror("Failed to read file");
        free(buffer);
        return -1;
    }

    //Send the file data
    if (send(socket, buffer, size, 0) < 0) {
        perror("Failed to send file data");
        free(buffer);
        return -1;
    }

    free(buffer);
    return 0;
	
    //TODO: send the file size packet
    //TODO: send the file data
    // TODO: return 0 on success, -1 on failure
}

/**********************************************
 * receive_file_from_server
   - socket is the file descriptor for the socket
   - filename is the name of the file you want to save
   - returns 0 on success, -1 on failure
************************************************/
int receive_file_from_server(int socket, const char *filename) 
{
    packet_t packet;
    
    //Receive the size packet
    if (recv(socket, &packet, sizeof(packet_t), 0) < 0) {
        perror("Failed to receive size packet");
        return -1;
    }

    //Allocate buffer for file data
    char *buffer = malloc(packet.size);
    if (buffer == NULL) {
        perror("Failed to allocate memory for file");
        return -1;
    }

    //Receive the file data
    ssize_t received = recv(socket, buffer, packet.size, 0);
    if (received < 0 || received != packet.size) {
        perror("Failed to receive file data");
        free(buffer);
        return -1;
    }

    //Open file for writing
    FILE *fp = fopen(filename, "wb");
    if (fp == NULL) {
        perror("Failed to open file for writing");
        free(buffer);
        return -1;
    }

    //Write the data to file
    if (fwrite(buffer, 1, packet.size, fp) != packet.size) {
        perror("Failed to write file");
        free(buffer);
        fclose(fp);
        return -1;
    }

    free(buffer);
    fclose(fp);
    return 0;
    //TODO: create a buffer to hold the file data
    //TODO: open the file for writing binary data
   //TODO: create a packet_t to hold the packet data
   //TODO: receive the response packet
    //TODO: get the size of the image from the packet
   //TODO: recieve the file data and write it to the file
    //TODO: return 0 on success, -1 on failure
}

