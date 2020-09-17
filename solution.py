from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

    # Create socket called clientSocket and establish a TCP connection with mailserver and port
    # Fill in start
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver,port))
    # Fill in end

    recv = clientSocket.recv(1024).decode()
    print(recv) # 220 test.nyu
    if recv[:3] != '220':
        print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    print(recv1) # 250 Hello test.nyu, pleased to meet you
    if recv1[:3] != '250':
        print('250 reply not received from server.')

    # Send MAIL FROM command and print server response.
    # Fill in start
    MAILFROM = 'MAIL FROM <test@test.nyu>\r\n'
    clientSocket.send(MAILFROM.encode())
    recv2 = clientSocket.recv(1024).decode()
    print(recv2) # 250 test@test.nyu ... Sender ok
    if recv2[:3] != '250':
        print('250 reply not received from server.')
    # Fill in end

    # Send RCPT TO command and print server response.
    # Fill in start
    RCPTTO = 'RCPT TO: <test2@test.nyu>\r\n'
    clientSocket.send(RCPTTO.encode())
    recv3 = clientSocket.recv(1024).decode()
    print(recv3) # 250 test2@test.nyu ... Recipient ok
    if recv3[:3] != '250':
        print('250 reply not received from server.')
    # Fill in end

    # Send DATA command and print server response.
    # Fill in start
    clientSocket.send('DATA\r\n'.encode())
    recv4 = clientSocket.recv(1024).decode()
    print(recv4) # 354 Enter mail, end with '.' on a line by it self
    if recv4[:3] != '354':
        print('354 reply not received from server.')
    # Fill in end

    # Send message data.
    # Fill in start
    clientSocket.send(msg.encode())
    # Fill in end

    # Message ends with a single period.
    # Fill in start
    clientSocket.send(endmsg.encode())
    recv5 = clientSocket.recv(1024).decode()
    print(recv5) # 250 Message accepted for delivery
    if recv5[:3] != '250':
        print('250 reply not received from server.')
    # Fill in end

    # Send QUIT command and get server response.
    # Fill in start
    clientSocket.send('QUIT\r\n'.encode())
    recv6 = clientSocket.recv(1024).decode()
    print(recv6) # 221 test.nyu closing connection
    if recv6[:3] != '221':
        print('221 reply not received from server.')
    # Fill in end


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
