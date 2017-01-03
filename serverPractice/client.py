import socket

mySocket = socket.socket();
host = socket.gethostname()
port = 6666

mySocket.connect((host,port))
mySocket.send("This is my schtooopid  message!".encode())
print(mySocket.recv(1024).decode())
mySocket.close()

