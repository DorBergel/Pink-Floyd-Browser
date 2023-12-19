import os
import socket


def menu():
    print("Hello dear friend, what would you like to do?")
    print("1- Find song's name by lyrics")
    print("2- Find out all songs in specific album")
    print("3- Find song's duration")
    print("4- Find song's lyrics")
    print("5- Find song's writer")
    print("6- Quit")
    choice = input("--> ")
    return choice


def client_program():

    choice = int
    query = ""
    host = socket.gethostname()  # as both code is running on same pc
    port = 5000  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    while choice != 6:

        choice = menu()

        if choice == '1':
            query = input("Type the lyrics: ")
            query = "SNG" + query
        elif choice == "2":
            query = input("Enter albums name: ")
            query = "ALM" + query
        elif choice == '3':
            query = input("Enter song's name: ")
            query = "DUR" + query
        elif choice == '4':
            query = input("Enter song's name: ")
            query = "LYR" + query
        elif choice == '5':
            query = input("Enter song's name: ")
            query = "WRT" + query
        else:
            break

        client_socket.send(query.encode())  # send message
        data = client_socket.recv(1024).decode()  # receive response

        print('Server\'s response: ' + data)  # show in terminal
        input("Press Enter to continue...")
        os.system('clear')

    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()