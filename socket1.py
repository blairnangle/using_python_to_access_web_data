import socket


mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.py4inf.com', 80))
mysock.send('GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n')  # "\n" in place of user pressing [return]

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data)

mysock.close()

# Works in Python 2, not 3
