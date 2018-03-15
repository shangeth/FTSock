import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = input("enter the IP of server : ")
port = int(input("Enter the port of server"))

s.connect((host,port))

# getting name of file
data = s.recv(1024)
file_name = data.decode()
print(file_name)
#getting file
with open("someeeee.jpg", 'wb') as f:
    while True:
        print('receiving...')
        data = s.recv(1024)
        print(data)
        f.write(data)
        if not data:
            break


f.close()
s.close()