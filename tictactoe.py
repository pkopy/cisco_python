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
    while True:
        try:
            lst = MakeListOfFreeFields(board)
            if len(lst) == 0:
                break
            userSquare = int(input('Enter your move:'))
            row = int((userSquare-1)//3)
            column = (userSquare-1)-int(((userSquare-1)//3)*3)
#             print(row, column)
            if (row, column) not in lst:
                continue
            else:
                board[row][column] = 'O'
                VictoryFor(board, 'O')
            break
        except:

            print('Try one more time')


def MakeListOfFreeFields(board):
#
# the function browses the board and builds a list of all the free squares; 
# the list consists of tuples, while each tuple is a pair of row and column numbers
#
    lst = []
    for elem in range(len(board)):
        for square in board[elem]:
            if (type(square) == int):

#                 print((elem, ((square-1)-int((square-1)//3)*3)))
                lst.append((elem, ((square-1)-int((square-1)//3)*3)))
#                 print(square)
#     print(lst)
    return lst
def VictoryFor(board, sign):
#
# the function analyzes the board status in order to check if 
# the player using 'O's or 'X's has won the game
#
    if board[0][0] == board[0][1] == board[0][2]:
        print(sing,' win')

def DrawMove(board):
#
# the function draws the computer's move and updates the board
#
    ok = True
    while ok:
        square = randrange(9)
        row = int(square//3)
        column = square-int(square//3)*3
        lst = MakeListOfFreeFields(board)
        if len(lst) == 0:
            break
        if ((row, column) not in lst):
#             print('bleee')
            pass
        else:
            ok = False
#             print('ff',square+1, int(square//3), square-int(square//3)*3)
            board[row][column] = 'X'
#         ok=False
#     DisplayBoard(board)

board = [[1,2,3],[4,"X",6], [7,8,9]]
x = MakeListOfFreeFields(board)
while len(x) > 0:
    DisplayBoard(board)
    x = MakeListOfFreeFields(board)

    EnterMove(board)
    DrawMove(board)
# MakeListOfFreeFields(board)
