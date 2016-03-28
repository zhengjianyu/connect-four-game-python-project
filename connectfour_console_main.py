#  Jianyu Zheng 33062456 and Shengruo Zhang 12478726.  ICS 32 Lab sec 5.  Lab asst 1.

import connectfour as C
import connectfour_functions as F

def main_program() -> None:
##    while True:
    State = C.new_game_state()
    while True:
        winner = C.winning_player(State)
        F.new_board(State.board)
        if winner != C.NONE:
            break
        try:
            print("It's " + F.full_name(State.turn) + " player's turn. ", end = '')
            command = input(F.Menu).upper()
            if command == 'A':
                column_number = int(input('please enter the column number: '))
                State = C.drop_piece(State, column_number - 1)
                print()
            elif command == 'B':
                column_number = int(input('please enter the column number: '))
                State = C.pop_piece(State, column_number - 1)
                print()
            else:
                F.invalid_command(command)
        except C.InvalidConnectFourMoveError:
            print('\nInvaild command. Please try again.\n')
        except ValueError:
            print('\nError. Column number must be between 1 and 7.\n') 
        except C.ConnectFourGameOverError:
            print('\nError. Game is over.\n')
    if winner == C.RED:
        print('Red player wins!')
    elif winner == C.YELLOW:
        print('Yellow player wins!')
    print()
##    break
##    restart()



if __name__ == '__main__':
    main_program()

