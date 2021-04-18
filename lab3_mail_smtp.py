import smtplib, ssl
from socket import *

msg = "\r\n I love Computer Networks"
endmsg = "\r\n.\r\n"

smtp_server = "smtp.gmail.com"
port = 587  # For starttls
username ="validateabcd123@gmail.com"
password = "superadmin@"

mailserver = (smtp_server, port) #Fill in start #Fill in end
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(mailserver)

# Create a secure SSL context
context = ssl.create_default_context()

# Try to log in to server and send email
try:
    server = smtplib.SMTP(smtp_server,port)
    server.ehlo() # Can be omitted
    server.starttls(context=context) # Secure the connection
    server.login(username, password)

    recv = clientSocket.recv(1024)
    print("Message after connection request:" + recv.decode())
    if recv[:3] != '220':
        print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024)
    print(recv1.decode())
    if recv1[:3] != '250':
        print('250 reply not received from server.')

    # Send MAIL FROM command and print server response.
    mailFrom = "MAIL FROM: <validateabcd123@gmail.com> \r\n"
    clientSocket.send(mailFrom.encode())
    recv2 = clientSocket.recv(1024)
    print("After MAIL FROM command: " + recv2.decode())
    if recv2[:3] != '250':
        print('250 reply not received from server.')

    # Send RCPT TO command and print server response.
    rcptTo = "RCPT TO: <thuan2172001@gmail.com> \r\n"
    clientSocket.send(rcptTo.encode())
    recv3 = clientSocket.recv(1024)
    print("After RCPT TO command: " + recv3.decode())
    if recv3[:3] != '250':
        print('250 reply not received from server.')

    # Send DATA command and print server response.
    data = "DATA\r\n"
    clientSocket.send(data.encode())
    recv4 = clientSocket.recv(1024)
    print("After DATA command: " + recv4.decode())
    if recv4[:3] != '250':
        print('250 reply not received from server.')

    print(recv.decode())
    if recv[:3] != '354':
        print('354 reply not received from server.') 

    # Send message data.
    subject = "Subject: SMTP mail client testing \r\n\r\n" 
    clientSocket.send(subject.encode())
    clientSocket.send(endmsg.encode())
    recv_msg = clientSocket.recv(1024)
    print("Response after sending message body:" + recv_msg.decode())
    if recv_msg[:3] != '250':
        print('250 reply not received from server.')

    server.sendmail(username, "thuan2172001@gmail.com", subject.encode())

    # Send QUIT command and get server response.
    clientSocket.send("QUIT\r\n".encode())
    message=clientSocket.recv(1024)
    print(message.decode())
    clientSocket.close()    

except Exception as e:
    # Print any error messages to stdout
    print(e)
finally:
    server.quit() 