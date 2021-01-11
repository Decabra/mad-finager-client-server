# IP ADDRESS OF THIS SERVER IS '10.7.61.211' and LOCAL IP IS '127.0.0.1'
from core import index
import socket
from _thread import *

ServerSideSocket = socket.socket()
host = ''
port = 95
ThreadCount = 0
try:
    ServerSideSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print('Socket is listening..')
ServerSideSocket.listen(5)


def multi_threaded_client(connection, client_id):
    connection.send(str.encode('Server is working:'))
    while True:
        user_choice = connection.recv(2048).decode('utf-8')
        file_name = connection.recv(2048).decode('utf-8')
        if user_choice == "3":
            do_close = connection.recv(2048).decode('utf-8')
            response = index.main(user_choice, file_name, client_id, "", do_close)
        elif user_choice == "4":
            connection.send(str.encode(index.get_active_access()))
            active = connection.recv(2048).decode('utf-8')
            print(active)
            index.set_active_access(active)
            if file_name == active:
                writing_text = connection.recv(2048).decode('utf-8')
                response = index.main(user_choice, file_name, client_id, writing_text, "")
            else:
                response = active
        else:
            response = index.main(user_choice, file_name, client_id)
        if not user_choice or not file_name:
            break
        connection.sendall(str.encode(response))
    connection.close()


while True:
    Client, address = ServerSideSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(multi_threaded_client, (Client, ThreadCount,))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
ServerSideSocket.close()
