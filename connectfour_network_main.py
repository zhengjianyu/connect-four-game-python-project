#  Jianyu Zheng 33062456 and Shengruo Zhang 12478726.  ICS 32 Lab sec 5.  Lab asst 1.

import socket
import connectfour as _X_
import connectfour_protocol as _P_
import connectfour_functions as _F_

HOST = 'evil-monkey.ics.uci.edu'
PORT = 4444

def main_program(host, port) -> None:
    username = _P_.confirm_username()
    game_socket = socket.socket()
    try:
        print('\nconnecting to server...\n')
        game_socket.connect((host, port))
        print('Connected successfully.\n')
        _P_.send_message(game_socket, str('I32CFSP_HELLO ' + username))
        reply1 = _P_.receive_message(game_socket)
        print(reply1, end = '\n\n')
        _P_.send_message(game_socket, 'AI_GAME')
        reply2 = _P_.receive_message(game_socket)
        print(reply2, end = '\n\n')
    except ConnectionRefusedError:
        print('Invalid port')
        return 'Invalid'
##    while True:
    State = _X_.new_game_state()
    while True:
        winner = _X_.winning_player(State)
        _F_.new_board(State.board)
        if winner != _X_.NONE:
            break
        try:
            _F_.turn(State.turn)
            command = input(_F_.Menu).upper()
            if command == 'A':
                column_number = int(input('please enter the column number: '))
                State = _X_.drop_piece(State, column_number - 1)
                print()
                AI = _P_.AI(game_socket, 'A', column_number).split()
##                print(AI)
##                _C_.new_board(State.board)
##                print()
##                _N_.AI_turn(State.turn)
                if AI[0] == 'DROP':
                    State = _X_.drop_piece(State, int(AI[1]) - 1)
                elif AI[0] == 'POP':
                    State = _X_.pop_piece(State, int(AI[1]) - 1)
            elif command == 'B':
                column_number = int(input('please enter the column number: '))
                State = _X_.pop_piece(State, column_number - 1)
                print()
                AI = _P_.AI(game_socket, 'B', column_number).split()
##                print(AI)
##                _C_.new_board(State.board)
##                print()
##                _N_.AI_turn(State.turn)
                if AI[0] == 'DROP':
                    State = _X_.drop_piece(State, int(AI[1]) - 1)
                elif AI[0] == 'POP':
                    State = _X_.pop_piece(State, int(AI[1]) - 1)
            else:
                _F_.invalid_command(command)
        except _X_.InvalidConnectFourMoveError:
            print('\nInvaild command. Please try again.\n')
        except ValueError:
            print('\nError. Column number must be between 1 and 7.\n') 
        except _X_.ConnectFourGameOverError:
            print('\nError. Game is over.\n')
    if winner == _X_.RED:
        print('Red player wins!')
    elif winner == _X_.YELLOW:
        print('Yellow player wins!')
##        restart = input('\nPlay again?  (Y/N)').upper()
##        if restart == 'Y':
##            print('game restart!\n\n')
##            State = _X_.new_game_state()
##        elif restart == 'N':
##            print('\nThanks for playing, Bye!')
##            break
##        else:
##            _C_.invalid_command(restart)
    print('\nGame is over.\nThanks for playing, Bye!')




    
if __name__ == '__main__':
    main_program(HOST, PORT)
