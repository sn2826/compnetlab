#Basic server socket steps:
#1. Bind
#2. Listen
#3. Accept
#4. Close


#import socket module
from socket import *
import sys # In order to terminate the program

def webServer(port=13331):
    serverSocket = socket(AF_INET, SOCK_STREAM)

    #Prepare a sever socket
    
    serverSocket.bind(('', port))
    serverSocket.listen(1)


    while True:
        #Establish the connection
        print('Ready to serve...')
        connectionSocket, addr = serverSocket.accept()
        try:
            message = connectionSocket.recv(2048)
            filename = message.split()[1]
            f = open(filename[1:])
            outputdata = f.read()
            f.close()

            #Send one HTTP header line into socket
            #Fill in start
            connectionSocket.send(bytes('HTTP/1.0 200 OK\r\n\r\n', "UTF-8"))
            #Fill in end

            #Send the content of the requested file to the client
            for i in range(0, len(outputdata)):
                connectionSocket.send(outputdata[i].encode())

            connectionSocket.send("\r\n".encode())
            connectionSocket.close()
        except IOError:
            #Send response message for file not found (404)
            #Fill in start
            connectionSocket.send(bytes("404 File Not Found\r\n\r\n", "UTF-8"))
            #Fill in end

            #Close client socket
            #Fill in start
            connectionSocket.close()
            #Fill in end

    serverSocket.close()
    sys.exit()  # Terminate the program after sending the corresponding data

if __name__ == "__main__":
    webServer(13331)
