import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost",9000))


while True:
    user = input("Send your data to server : ")
    s.send(bytes(user,"utf-8"))
    msg = s.recv(1024)
    msg = msg.decode("utf-8")
    print(msg)

