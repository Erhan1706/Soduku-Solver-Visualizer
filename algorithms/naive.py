from typing import List
import pygame
import pygame_widgets
from algorithms.validCheckers import insertChecker

class Calls:
    callNum = 0

c = Calls()
def naiveBacktracking(board, i: int, j: int):
    c.callNum += 1
    if i == 9:
        yield board  # Yield the final board state
        print(c.callNum)
        raise StopIteration
    elif j == 9:
        yield from naiveBacktracking(board, i + 1, 0)  # Move to the next row
    elif board[i][j].getText() != "":
        yield from naiveBacktracking(board, i, j + 1)  # Move to the next column
    else:
        for num in range(1, 10):
            valid = insertChecker(i, j, num, board)
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

