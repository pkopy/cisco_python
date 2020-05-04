from random import randrange




def DisplayBoard(board):
    #
# the function accepts one parameter containing the board's current status
# and prints it out to the console
#
    
    line = '-----+'
    emptyLine = '     |'
    def lineWithNumber(n):
        return '  ' + str(n) + '  '
    print('+' + line * 3)
    for i in range(3):
        
        print(('|' + emptyLine * 3))
        wholeLine = '|'
        for j in board[i]:
            wholeLine += lineWithNumber(j) + '|'
        print(wholeLine)
        print(('|' + emptyLine * 3))
        print('+' + line * 3)

def EnterMove(board):
#
# the function accepts the board current status, asks the user about their move, 
# checks the input and updates the board according to the user's decision
#
    pass

def MakeListOfFreeFields(board):
#
# the function browses the board and builds a list of all the free squares; 
# the list consists of tuples, while each tuple is a pair of row and column numbers
#
    pass
def VictoryFor(board, sign):
#
# the function analyzes the board status in order to check if 
# the player using 'O's or 'X's has won the game
#
    pass
def DrawMove(board):
#
# the function draws the computer's move and updates the board
#
    pass

board = [[1,2,3],[4,'X',5], [6,7,8]]
DisplayBoard(board)