from getpass import getpass
from socket import *
from base64 import *
import ssl

EMAIL_USERNAME = "validateabcd123@gmail.com"
EMAIL_PASSWORD = "superadmin@"
DESTINATION_EMAIL = "thuan2172001@gmail.com"
SUBJECT_EMAIL = "Test send mail"
EMAIL_BODY = "This is an email!"

msg = '\r\nI love computer networks!'
endmsg = '\r\n.\r\n'

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailServer = 'smtp.gmail.com'
mailPort = 587

# Create socket called clientSocket and establish a TCP connection with mailserver
#Fill in start
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailServer, mailPort))
#Fill in end

recv = clientSocket.recv(1024)
print("rec: " + recv.decode())

# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'.encode()
clientSocket.send(heloCommand)
recv1 = clientSocket.recv(1024)
print("rec1: " + recv1.decode())

# Account Authentication
# Fill in start
strtlscmd = "STARTTLS\r\n".encode()
clientSocket.send(strtlscmd)
recv2 = clientSocket.recv(1024)

sslClientSocket = ssl.wrap_socket(clientSocket)

EMAIL_ADDRESS = b64encode(EMAIL_USERNAME.encode())
EMAIL_PASSWORD = b64encode(EMAIL_PASSWORD.encode())

authorizationcmd = "AUTH LOGIN\r\n"

sslClientSocket.send(authorizationcmd.encode())
recv2 = sslClientSocket.recv(1024)
print("rec2: " + recv2.decode())

sslClientSocket.send(EMAIL_ADDRESS + "\r\n".encode())
recv3 = sslClientSocket.recv(1024)
print("rec3: " + recv3.decode())

sslClientSocket.send(EMAIL_PASSWORD + "\r\n".encode())
recv4 = sslClientSocket.recv(1024)
print("rec4: " + recv4.decode())
# Fill in end    
	
# Send MAIL FROM command and print server response.
# Fill in start
mailfrom = "MAIL FROM: <{}>\r\n".format(EMAIL_USERNAME)
sslClientSocket.send(mailfrom.encode())
recv5 = sslClientSocket.recv(1024)
print("rec5: " + recv5.decode())
# Fill in end    

# Send RCPT TO command and print server response.
# Fill in start
rcptto = "RCPT TO: <{}>\r\n".format(DESTINATION_EMAIL)
sslClientSocket.send(rcptto.encode())
recv6 = sslClientSocket.recv(1024)
print("rec6: " + recv6.decode())
# Fill in end

# Send DATA command and print server response. 
# Fill in start
data = 'DATA\r\n'
sslClientSocket.send(data.encode())
recv7 = sslClientSocket.recv(1024)
print("rec7: " + recv7.decode())
# Fill in end    

# Send message data.
# Fill in start
sslClientSocket.send("Subject: {}\n\n{}".format(SUBJECT_EMAIL, msg).encode())
# Fill in end

# Message ends with a single period.
# Fill in start
sslClientSocket.send(endmsg.encode())
recv8 = sslClientSocket.recv(1024)
print("rec8: " + recv8.decode())
# Fill in end

# Send QUIT command and get server response.
# Fill in start
quitcommand = 'QUIT\r\n'
sslClientSocket.send(quitcommand.encode())
recv9 = sslClientSocket.recv(1024)
print("rec9: " + recv9.decode())

sslClientSocket.close()
print('Was successful!')
# Fill in end