from typing import List
import pygame
import pygame_widgets
import time

def naiveBacktracking(board, i: int, j: int):
    if i == 9:
        yield board  # Yield the final board state
    elif j == 9:
        yield from naiveBacktracking(board, i + 1, 0)  # Move to the next row
    elif board[i][j].getText() != "":
        yield from naiveBacktracking(board, i, j + 1)  # Move to the next column
    else:
        for num in range(1, 10):
            valid = sudokuChecker(i, j, num, board)
            if valid:
                board[i][j].textColour = (250, 10, 10)
                board[i][j].setText(str(num))
                pygame_widgets.update(pygame.event.get())
                pygame.display.update()

                # Yield the current board state
                yield board

                # Recursively call the function for the next column
                yield from naiveBacktracking(board, i, j + 1)

                # Undo the changes after the recursive call
                board[i][j].setText("")


def sudokuChecker(i : int, j : int, num: int, board) -> bool:
    num = str(num)
    for index in range(0, 9):
        if board[i][index].getText() == "": continue
        elif board[i][index].getText() == num: return False
    for index in range(0, 9):
        if board[index][j].getText() == "": continue
        elif board[index][j].getText() == num: return False
    startIndexCol = i // 3 * 3
    startIndexRow = j // 3 * 3 
    for index in range(0, 3):
        for index2 in range(0,3):
            cur =  board[startIndexCol + index][startIndexRow + index2].getText()
            if cur == "": continue
            elif cur == num: return False
    return True


# solveSudoku(board)
