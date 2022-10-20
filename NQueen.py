count = 0
def isSafe(board, n, row, col):
   
    newrow = row
    newcol = col
    

    while (row >= 0 and col >= 0):
        if(board[row][col] == 1):
            return False;
        row -= 1
        col -= 1
 
    col = newcol;
    row = newrow;

    while(col >= 0):
        if(board[row][col] == 1):
            return False;
        col -= 1
        
    row = newrow;
    col = newcol;

    while (row<n and col>=0):
        if(board[row][col] == 1):
            return False;
        row += 1
        col -= 1

    return True;

def solveBoard(board, n, col):
    global count
    if(col == n):
        count +=1
        print(f"Solution No. {count}: ", board)
        return
    

    for row in range(n):
        if(isSafe(board, n, row, col)):
            board[row][col] = 1
            solveBoard(board, n, col+1)
            board[row][col] = 0

n = int(input("Enter How many queens(n) you want to in N*N chess board: "))
board = [[0 for j in range(n)] for i in range(n)]

solveBoard(board, n, 0)
