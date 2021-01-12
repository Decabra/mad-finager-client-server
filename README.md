# Mad-Finager-client-server
The purpose of this project is to build the server for the file management component of distributed file management system. The goal of this project is to build the structure for file management to provide access to user(s) to create, delete, read, write the content onto the files in the system remotely.  
It represents its output and store its files in JavaScript Object Notation (JSON) file in a very beautiful manner.


# Motivation
Mostly we have seen many computers having the implementation of File Management System. So, creating, writing data or reading content from the file, or open a file is done by using a simple project called "Mad-Finager with client-server ". We can do all the things remotely from different devices.

# Build status
Previous version of this project is implemented as "Mad-Finager with Threading"


# Code style
We have used Python language by using its thread library, with the usage of JSON file structure. 


# Technology Used
Python 3.7 and JSON

# Built with

PyCharm and Intelligaia IDE


# How to use?
1.	First, we have to execute server.py file to start the server which is running until the server program terminates.
2.	After this, we run the client file, and give the IP Address of the server, for easiness let’s give 127.0.0.1. An id assigned to the client i.e “Client_id 0” and start performing operations like creating, deleting, read, writing onto the file with show map also.
3.	If this process is going on and another user come and make connection with server, another thread attached into the server and handle its working. Another id is assigned to the client i.e “Client_id 1” and start performing operations like creating, deleting, read, writing onto the file with show map also.

To understand the system, we have implemented different features. For this, we have to understand all of its feature.

1.	It has two programs, a server and a client which is depicted in this screenshot.
![serverclient](https://user-images.githubusercontent.com/57443179/104350734-4e8e5100-5526-11eb-9598-36a8db634af8.png)

 
2.	The client allows the user to specify the IP address of the server
 ![ipaddress](https://user-images.githubusercontent.com/57443179/104350689-3f0f0800-5526-11eb-83f1-f285841de77d.png)

3.	The server know that which client is connected with it and it display its username. 
![username](https://user-images.githubusercontent.com/57443179/104350717-4afaca00-5526-11eb-9043-e2ebc8442c8a.png)
4.	In our system, we provide an interface to client to apply the operations developed in the previous.
 ![interface](https://user-images.githubusercontent.com/57443179/104350685-3f0f0800-5526-11eb-9165-0344e83b7e29.png)
5.	The client gives errors when the server is not available.
![error](https://user-images.githubusercontent.com/57443179/104350684-3e767180-5526-11eb-86ec-0a6b50beebfd.png)
 
6.	The client displays the response of the actions performed.
![actions](https://user-images.githubusercontent.com/57443179/104350683-3ddddb00-5526-11eb-8de1-648bb5249efb.png)
 
7.	The server respond to multiple requests at the same time. For example, in this screenshot, first we run the server and then starting three different operations, and server responds to all of the request. 
 ![multiplerequest](https://user-images.githubusercontent.com/57443179/104350677-3cacae00-5526-11eb-9af7-1e8a42b3a3bc.png)
8.	The server must bind to port 95.
 ![socket](https://user-images.githubusercontent.com/57443179/104350735-4f26e780-5526-11eb-8e13-71741027b20e.png)
9.	The server and clients run on different machines.



# Contribute
You can give contribution to make it a Giant File Management System with other features of replace, manage, date modified and other general features.

# License
NUST © Sarmad Sohail
NUST © Hamza Amjad
NUST © Muhammad Umer Farooq
