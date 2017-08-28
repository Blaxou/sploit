import socket

host = "localhost"
port = 4444                   # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
s.sendall(b'I am Connected to you')
data = s.recv(1024)
s.close()
print('Received : ' + repr(data))
