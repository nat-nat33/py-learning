import socket

host = ""
port = 8080;

mySocket = socket.socket();
mySocket.bind((host,port));
mySocket.listen();


while True:
	client, add = mySocket.accept();
	message = client.recv(1024).decode();
	print(message);
	#reply = "You asked " + message
	client.send("HTTP/1.0 200 Not Found\r\n".encode());
	client.close();

