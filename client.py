import socket
buffer = 5120
port = 95
ClientMultiSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
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
        ClientMultiSocket.send(str.encode(user_choice))
        if user_choice < "5":
            file_name = input("Enter File name: ")
            ClientMultiSocket.send(str.encode(file_name))

        if user_choice == "4":
            ClientMultiSocket.send(str.encode(file_name))
            check = ClientMultiSocket.recv(buffer).decode('utf-8')
            if check == "passed":
                writing_text = input(f"Enter text for file {file_name}: ")
                ClientMultiSocket.send(str.encode(writing_text))

        res = ClientMultiSocket.recv(buffer).decode('utf-8')
        print(res)

        if user_choice == "3":
            while True:
                do_close = input("Enter c to close the file: ")
                if do_close == "c":
                    break
            ClientMultiSocket.send(str.encode(file_name))
            response = ClientMultiSocket.recv(buffer).decode('utf-8')
            print(response)

        if res == "terminated":
            break

except socket.error as e:
    print("Server is not available")
ClientMultiSocket.close()
