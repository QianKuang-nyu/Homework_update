#import socket module
from socket import *
import sys # In order to terminate the program

def webServer(port=13331):
    serverSocket = socket(AF_INET, SOCK_STREAM)

    #Prepare a sever socket
    #Fill in start
    serverSocket.bind(('127.0.0.1',port))
    serverSocket.listen(1)
    #Fill in end

    while True:
        #Establish the connection
        print('Ready to serve...')
        connectionSocket, addr = serverSocket.accept()
        try:
        	# In python3
        	# str->bytes: encode()
        	# bytes->str: decode()

        	# get info from client
            message = connectionSocket.recv(1024).decode()
            filename = message.split()[1]
            
            # file I/O
            f = open(filename[1:])
            outputdata = f.read()

            #Send one HTTP header line into socket
            #Fill in start
            connectionSocket.send('HTTP/1.1 200 OK\r\n'.encode())
            # A blank line is needed, otherwise not work
            connectionSocket.send('\r\n'.encode())
            #Fill in end

            #Send the content of the requested file to the client
            for i in range(0, len(outputdata)):
                connectionSocket.send(outputdata[i].encode())

            connectionSocket.send("\r\n".encode())
            connectionSocket.close()
        except IOError:
            #Send response message for file not found (404)
            #Fill in start
            connectionSocket.send('HTTP/1.1 404 NOT FOUND\r\n'.encode())
            # # A blank line is needed, otherwise not work
            connectionSocket.send('\r\n'.encode())
            # To output something
            connectionSocket.send('<html><body> \
            	Undefined Page</body></html>\r\n'.encode())

            #Fill in end

            #Close client socket
            #Fill in start
            connectionSocket.close()
            #Fill in end

    serverSocket.close()
    sys.exit()  # Terminate the program after sending the corresponding data

if __name__ == "__main__":
    webServer(13331)
