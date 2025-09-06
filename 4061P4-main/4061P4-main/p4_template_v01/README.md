P4 group 57
CSCI 4061 - Fall 2024 - Project #4
-Nicholas Haddad: hadda049
-Aiden Theiste: theis683
-Ben Ziebol: ziebo012

Assumptions:
that there will be a output/img folder

Individual contributions:
ziebo012: first 1/3 of functions
theis683: second 1/3 of functions
hadda049: final 1/3 of functions

Makefile Changes:
None

How could enable to make each request parallelized:
Essentially make it so that each connection will create a new thread to handle the request(s)

void parralize() {
    initialize variables

    send_file_to_client(socket,buffer,size);

    close and clean up
}

(in main)
while(1) {
    initialize variables

    pthread_t thread;
    pthread_create(thread, null, client, socket);

    close and clean up
}