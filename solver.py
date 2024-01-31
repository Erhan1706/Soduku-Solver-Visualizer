from typing import List


def solveSudoku(board: List[List[str]]) -> None:
        solveHelper(board, 0, 0)

def solveHelper(board, i, j):
    if i == 9: return True
    elif j == 9: return solveHelper(board, i + 1, 0)
    elif board[i][j] != ".": return solveHelper(board, i, j + 1)
    else:
        for num in range(1,10):
            valid = sudokuChecker(i,j,num,board)
            if valid:
                board[i][j] = str(num)
                if solveHelper(board, i, j + 1): return True 
                board[i][j] = "."

def sudokuChecker(i : int, j : int, num: int, board: List[List[str]]) -> bool:
    num = str(num)
    for index in range(0, 9):
        if board[i][index] == ".": continue
        elif board[i][index] == num: return False
    for index in range(0, 9):
        if board[index][j] == ".": continue
        elif board[index][j]  == num: return False
    startIndexCol = i // 3 * 3
    startIndexRow = j // 3 * 3 
    for index in range(0, 3):
        for index2 in range(0,3):
            cur =  board[startIndexCol + index][startIndexRow + index2]
            if cur == ".": continue
            elif cur == num: return False
    return True

board =  [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]
#print(sudokuChecker(0,2,5,board))
solveSudoku(board)
print(board)