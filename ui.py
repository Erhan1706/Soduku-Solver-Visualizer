import pygame 
import pygame_widgets
import numpy as np
from pygame_widgets.button import Button
from pygame_widgets.textbox import TextBox
from pygame_widgets.slider import Slider
from pygame_widgets.dropdown import Dropdown
from algs import algorithmsList
from algorithms.solver import naiveBacktracking
import asyncio

# Colors 
BLUE = (10, 10, 250)
WHITE = (250, 250, 250)
BLACK = (0, 0, 0)
RED = (250, 10, 10)
GREEN = (10, 250, 10) 
GRAY = (220, 220, 220)

pygame.init()

baseFont = pygame.font.SysFont('Century Gothic', 16)

screen = pygame.display.set_mode((900, 520))
pygame.display.set_caption('Sudoku Solver Algorithms Visualizer')


def handleInputChange(i, j):
  try: 
    num = int(board[i][j].getText())
    if num > 9 or num < 1: 
       raise Exception("Invalid Number")
  except ValueError:
    board[i][j].setText("")
  except:
    board[i][j].setText(board[i][j].getText()[:-1])
   

board = np.empty((9, 9), dtype=object)

for i in range(9):
   row = []
   for j in range(9):
      textbox = TextBox(screen, 10 + j * 55,  10 + i * 55, 50, 50, fontSize=30,
                  borderColour=(255, 255, 255), textColour=BLACK,
                  radius=10, borderThickness=2, onTextChanged=handleInputChange, onTextChangedParams=(i, j))
      board[i][j] = textbox


def updateScreen(): screen.fill(WHITE)

def drawBoardLines():
  pygame.draw.line(screen, BLACK, (5, 5), (5, 500), 2)
  pygame.draw.line(screen, BLACK, (500, 5), (500, 500), 2)
  pygame.draw.line(screen, BLACK, (5, 5), (500, 5), 2)
  pygame.draw.line(screen, BLACK, (5, 500), (500, 500), 2)

  pygame.draw.line(screen, BLACK, (171, 5), (171, 500), 2)
  pygame.draw.line(screen, BLACK, (335, 5), (335, 500), 2)
  pygame.draw.line(screen, BLACK, (5, 171), (500, 171), 2)
  pygame.draw.line(screen, BLACK, (5, 335), (500, 335), 2)


drawBoardLines()
a = algorithmsList[0](board, 0, 0)
def test():
  try: 
    s = next(a)
  except StopIteration:
    print("")

# slider = Slider(screen, 600, 50, 300, 10, min=0, max=99, step=1, handleRadius=20)
dropdown = Dropdown(
    screen, 600, 80, 250, 50, name='Algorithm',
    choices=[
        'Naive Backtracking',
        'Smart Backtracking (MRV)',
    ],
    borderColour=BLACK, colour=GRAY, values=[1, 2], direction='down', textHAlign='left', 
    font = baseFont,
    onClick = test
)

intialBoard =  [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]

def parseToBoard(defBoard): 
  for i in range(0,9):
    for j in range(0,9):
      if defBoard[i][j] != ".": 
        board[i][j].setText(defBoard[i][j])

def defaultBoard():
  parseToBoard(intialBoard)

defaultBoard()