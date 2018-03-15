import socket

file = input("Enter the file name(in the current directory) : ")


host = ""
port = 9998

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host, port))
s.listen(5)



while True:
    conn,addr = s.accept()
    print("New Client Connected - {} from port {}".format(str(addr[0]),str(addr[1])))
    conn.send(str.encode(file))
    f = open(file, "rb")
    for line in f:
        conn.send(line)
    f.close()
    conn.close()




