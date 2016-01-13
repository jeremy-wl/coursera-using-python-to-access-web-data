import socket

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.connect(('www.pythonlearn.com', 80))
mysocket.send('GET http://www.pythonlearn.com/code/intro-short.txt HTTP/1.0\n\n'.encode())
# Difference between a unicode string and a byte string
# http://stackoverflow.com/questions/6224052/what-is-the-difference-between-a-string-and-a-byte-string#answer-6224384
# The encoding and decoding of the two types of string
# http://stackoverflow.com/questions/11781639/typeerror-str-does-not-support-buffer-interface#answer-11781741

data = mysocket.recv(512)

while len(data) > 1:
    print(data)
    data = mysocket.recv(512)

mysocket.close()
