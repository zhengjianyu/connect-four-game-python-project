#  Jianyu Zheng 33062456 and Shengruo Zhang 12478726.  ICS 32 Lab sec 5.  Lab asst 1.

import socket


def login(host, port) -> None:
    '''specifies a username and connect to the server'''
    name = confirm_username()
    try:
        s = socket.socket()
        print('\nconnecting to server...\n')
        s.connect((host, port))
        print('Connected successfully.\n')
        send_message(s, str('I32CFSP_HELLO ' + name))
        reply1 = receive_message(s)
        print(reply1, end = '\n\n')
        send_message(s, 'AI_GAME')
        reply2 = receive_message(s)
        print(reply2, end = '\n\n')
        return s
    except ConnectionRefusedError:
        print('Invalid port')
        return 'Invalid'

def confirm_username() -> str:
    '''specify a username'''
    while True:
        username = input('Plaese create a username: ')
        if ' ' in username:
            print('Invalid. Username should not contain any whitespace.\nPlease try again.\n')
        else:
            return username

def send_message(socket: socket.socket, message: str) -> None:
    '''takes a string, send it to the server'''
    encode = (message + '\r\n').encode(encoding = 'utf-8')
    socket.send(encode)

def receive_message(socket: socket.socket) -> str:
    '''returns the message from the server'''
    message = socket.recv(4096).decode(encoding='utf-8').rstrip()
    return message
    
def close(socket: socket.socket) -> None:
    '''closes the connection to the server'''
    socket.close()

def AI(s: socket, command: str, column_number: int) -> None:
    '''receive actions from server'''
    if command == 'A':
        s.send(str('DROP ' + str(column_number) + '\r\n').encode(encoding = 'utf-8'))
        c = s.recv(4096).decode(encoding = 'utf-8')
        reply_A = s.recv(4096).decode(encoding = 'utf-8')
        return reply_A
    elif command == 'B':
        s.send(str('POP ' + str(column_number) + '\r\n').encode(encoding = 'utf-8'))
        c = s.recv(4096).decode(encoding = 'utf-8')
        reply_B = s.recv(4096).decode(encoding = 'utf-8')
        return reply_B

##def AI_turn(turn: str) -> None:
##    '''takes Y or R, returns the information about turn'''
##    print("It's " + _C_.full_name(turn) + " player's turn.\nPlease wait while AI is making choice.\n")



