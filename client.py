import socket

port = 95

ClientMultiSocket = socket.socket()
print('Waiting for connection response')

host = input("Enter IP: ")
try:
    ClientMultiSocket.connect((host, port))
    res = ClientMultiSocket.recv(1024)
    print(res.decode('utf-8'))
    while True:
        print("\n1. Create File\n2. Delete File\n3. Open File for read\n4. Open File for write  \n5. Show Map"
              "\n6. Kill Program")
        user_choice = input("Enter value: ")
        if user_choice < "5":
            file_name = input("Enter File name: ")
        else:
            file_name = "empty"

        ClientMultiSocket.send(str.encode(user_choice))
        ClientMultiSocket.send(str.encode(file_name))
        if user_choice == "3":
            do_close = input("Enter reading time: ")
            ClientMultiSocket.send(str.encode(do_close))

        if user_choice == "4":
            active = ClientMultiSocket.recv(1024).decode('utf-8')
            print(active)
            if file_name != active:
                ClientMultiSocket.send(str.encode(file_name))
                writing_text = input(f"Enter text for file {file_name}: ")
                ClientMultiSocket.send(str.encode(writing_text))
            else:
                ClientMultiSocket.send(str.encode("Another client accessing the file"))

        res = ClientMultiSocket.recv(1024).decode('utf-8')
        print(res)
        if res == "Command executed with code 1":
            break
except socket.error as e:
    print("Server is not available")
ClientMultiSocket.close()
