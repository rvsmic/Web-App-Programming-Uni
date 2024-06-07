#include <iostream>
#include <string>
#include <ctime>
#include <errno.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <unistd.h>
#include <netdb.h>
#include <pthread.h>

#define BUFFER_SIZE 1024

/**
g++ tcp_multithreaded_server.cpp -o tcp_multithreaded_server -lpthread
*/

void *ClientThread(void *args)
{
    int sock = *(int*)args;

    // odbieranie/wysylanie wiadomosci od/do klienta
    // ...
}

int main(int argc, char **argv)
{
    // utworzenie gniazda
    // bind
    // listen

    // akceptowanie klientow - w petli nieskonczonej
    while(client_fd = accept(server_fd, (struct sockaddr *) &client, &client_len))
    {
        // tworzymy nowy watek
        pthread_t thread;

        // uruchamiamy watek, jego obsluga (tym, za co odpowiada watek) zajmuje
        // sie funkcja ClientThread, przekazujemy jej jako argument socket klienta
        if(pthread_create(&thread, NULL, ClientThread, (void*) &client_fd) < 0)
        {
            std::cout << ("Could not create a new thread socket\n");
            perror("pthread_create");
            return 1;
        }
    }

    // zamkniecie socketow

    return 0;
}
