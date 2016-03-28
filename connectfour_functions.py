#  Jianyu Zheng 33062456 and Shengruo Zhang 12478726.  ICS 32 Lab sec 5.  Lab asst 1.

import connectfour as C


Menu = '''Please choose one of the following:
A: drop piece
B: pop piece
'''

def invalid_command(response) -> None:  # string -> interaction
    ''' Print message for invalid menu command. '''
    print("Sorry; '" + response + "' isn't a valid command.  Please try again.\n")

def full_name(turn: str) -> str:
    '''takes a 'R' or 'Y', returns 'Red' or 'Yellow' '''
    if turn == 'R':
        return 'Red'
    if turn == 'Y':
        return 'Yellow'

def new_board(board: list) -> None:
    '''returns a readable game board'''
##    print(board)
    print('--------------------------------------------------------------')
    for row in range(len(board)):
        print(str(row+1), end = '  ')
    print()
    for col in range(len(board[0])):
        new_row(board, col)
    print()
        
def new_row(board: list, num: int) -> None:
    '''reverse the rows and columns'''
    for row in board:
        print(new_piece(row[num]), end = '  ')
    print()

def new_piece(piece: str) -> str:
    '''takes a whitespace returns a dot'''
    if piece == ' ':
        return '.'
    else:
        return piece

##def restart() -> None:
##    '''if player enter Y, restart the game.'''
##    YN = input('Play again? (Y/N) ').upper()
##    if YN == 'Y':
##        print('game restart!\n\n')
##        main_program()
##    elif YN == 'N':
##        print('\nThanks for playing. Bye!')
##    else:
##        invalid_command(YN)
##        restart()

def turn(turn: str) -> None:
    '''takes Y or R, prints a string of information about the turn'''
    print("It's " + full_name(turn) + " player's turn. ", end = '')




