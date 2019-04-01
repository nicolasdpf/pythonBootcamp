from IPython.display import clear_output

def display_board(board):
    clear_output()
    print (board[7] + ' | ' + board[8] + ' | ' + board[9])
    print ('  |   |')  
    print ('------------')
    print ('  |   |')  
    print (board[4] + ' | ' + board[5] + ' | ' + board[6])
    print ('  |   |')  
    print ('------------')
    print ('  |   |')
    print (board[1] + ' | ' + board[2] + ' | ' + board[3])
    print ('  |   |')
    
test_board = ['#', 'X', 'X', 'X','O', 'X','O', 'X','O', '#']
display_board(test_board)
display_board(test_board)

def player_input():
    marker = ''

    while not (marker == 'X' and marker == 'O'):
        marker = input('Player1: Choose X or O: ').upper()
    
    if marker == 'X':
        return('X', 'O')
    else:
        return('O', 'X')

player1_marker, player2_marker = player_input()