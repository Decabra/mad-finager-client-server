# IP ADDRESS OF THIS SERVER IS '10.7.61.211' and LOCAL IP IS '127.0.0.1'
from core import index
import socket
from _thread import *

ServerSideSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '0.0.0.0'
port = 95
ThreadCount = 0
try:
    ServerSideSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print('Socket is listening..')
print(socket.gethostname())
ServerSideSocket.listen(5)


def multi_threaded_client(connection, client_id):
    connection.send(str.encode('Server is working:'))
    while True:
        user_choice = connection.recv(2048).decode('utf-8')
        if user_choice < "5":
            file_name = connection.recv(2048).decode('utf-8')

        if user_choice == "4":
            writeRequest = connection.recv(2048).decode('utf-8')
            auditResponse = index.audit_write_request(writeRequest)
            connection.send(str.encode(auditResponse))
            if auditResponse == "passed":
                writing_text = connection.recv(2048).decode('utf-8')
                response = index.main(user_choice, file_name, client_id, writing_text)
            else:
                response = "Another Client is accessing the file"

        else:
            if user_choice >= "5":
                file_name = "empty"
            response = index.main(user_choice, file_name, client_id)

        if not user_choice or not file_name:
            break

        connection.sendall(str.encode(response))

        if user_choice == "3":
            do_close = connection.recv(2048).decode('utf-8')
            res = index.close_file(do_close)
            connection.send(str.encode(res))

    connection.close()


while True:
    Client, address = ServerSideSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(multi_threaded_client, (Client, ThreadCount,))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
ServerSideSocket.close()
