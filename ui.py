import pygame 
import pygame_widgets
import numpy as np
from pygame_widgets.button import Button
from pygame_widgets.textbox import TextBox
from pygame_widgets.slider import Slider
from pygame_widgets.dropdown import Dropdown
from algs import algorithmsList
from algorithms.validCheckers import isBoardValid
from algorithms.generator import boardGenerator
from algorithms.generator import pokeHoles


# Colors 
BLUE = (10, 10, 250)
WHITE = (250, 250, 250)
BLACK = (0, 0, 0)
RED = (250, 10, 10)
GREEN = (10, 250, 10) 
GRAY = (220, 220, 220)

class UI:

  def __init__(self):
    pygame.init()

    self.baseFont = pygame.font.SysFont('Century Gothic', 16)
    self.secondFont = pygame.font.SysFont('Century Gothic', 20)
    self.screen = pygame.display.set_mode((900, 520))
    pygame.display.set_caption('Sudoku Solver Algorithms Visualizer')

    self.delay = 0.5
    self.runAlgo = False
    self.surface = self.baseFont.render('', True, BLACK)

    # Setup default board
    intialBoard = [["5","3",".",".","7",".",".",".","."]
          ,["6",".",".","1","9","5",".",".","."]
          ,[".","9","8",".",".",".",".","6","."]
          ,["8",".",".",".","6",".",".",".","3"]
          ,["4",".",".","8",".","3",".",".","1"]
          ,["7",".",".",".","2",".",".",".","6"]
          ,[".","6",".",".",".",".","2","8","."]
          ,[".",".",".","4","1","9",".",".","5"]
          ,[".",".",".",".","8",".",".","7","9"]] 

    self.board = np.empty((9, 9), dtype=object)
    self.setupBoard()
    self.parseToBoard(intialBoard)
    self.drawBoardLines()

    # UI Elements
    self.startButton = Button(
        self.screen,
        600,  # X-coordinate of top left corner
        440,  # Y-coordinate of top left corner
        200,  # Width
        25,  # Height
        text='Start',  
        font = self.baseFont,
        margin=20, 
        inactiveColour= GRAY,  
        hoverColour=(150, 150, 150),  
        pressedColour=(100, 100, 100), 
        radius=0,  
        onClick= self.startStopHandler
      )
    self.slider = Slider(self.screen, 610, 210, 230, 12, min=0, max=0.5, step=0.05, handleRadius=13, initial=0.1)
    self.dropdown = Dropdown(
        self.screen, 600, 245, 250, 50, name='Algorithm',
        choices=[
            'Naive Backtracking',
            'Minimal Remaining Value',
        ],
        borderColour=BLACK, colour=GRAY, values=[0, 1], direction='down', textHAlign='left', 
        font = self.baseFont
    )
    self.randomButton = Button(        
      self.screen,
      600,  # X-coordinate of top left corner
      470,  # Y-coordinate of top left corner
      200,  # Width
      25,  # Height
      text='Randomize Board',  
      font = self.baseFont,
      margin=20, 
      inactiveColour= GRAY,  
      hoverColour=(150, 150, 150),  
      pressedColour=(100, 100, 100), 
      radius=0,
      onClick= self.randomizeBoard
    )

    self.currentAlgo =  None
    self.prevIndex = -1

  # Only allow numbers to be inputted into the textboxes
  def handleInputChange(self, i, j):
    self.board[i][j].textColour = BLACK
    try: 
      num = int(self.board[i][j].getText())
      if num > 9 or num < 1: 
        raise Exception("Invalid Number")
      self.board[i][j].setText(str(num))
    except ValueError:
      self.board[i][j].setText("")
    except:
      self.board[i][j].setText(self.board[i][j].getText()[:-1])
    

  def updateScreen(self): self.screen.fill(WHITE)

  def renderText(self):
    self.screen.blit(self.surface, (600, 410))
    self.screen.blit(self.secondFont.render('Delay', True, BLACK), (605, 170))


  def iterate(self): 
    try:
      self.numCalls = next(self.currentAlgo)
    except: 
      self.finish()


  def updateBoard(self, new_board):
    for i in range(9):
        for j in range(9):
            self.board[i][j].setText(new_board[i][j].getText())
    
  
  def setupBoard(self):
    for i in range(9):
      for j in range(9):
          self.board[i][j] = TextBox(self.screen, 10 + j * 55,  10 + i * 55, 50, 50, fontSize=30,
                      borderColour=(255, 255, 255), textColour=BLACK,
                      radius=10, borderThickness=2, onTextChanged=self.handleInputChange, onTextChangedParams=(i, j))

  def parseToBoard(self, defBoard): 
    for i in range(0,9):
      for j in range(0,9):
        if defBoard[i][j] != ".": 
          self.board[i][j].setText(defBoard[i][j])


  def drawBoardLines(self):
    pygame.draw.line(self.screen, BLACK, (5, 5), (5, 500), 2)
    pygame.draw.line(self.screen, BLACK, (500, 5), (500, 500), 2)
    pygame.draw.line(self.screen, BLACK, (5, 5), (500, 5), 2)
    pygame.draw.line(self.screen, BLACK, (5, 500), (500, 500), 2)

    pygame.draw.line(self.screen, BLACK, (171, 5), (171, 500), 2)
    pygame.draw.line(self.screen, BLACK, (335, 5), (335, 500), 2)
    pygame.draw.line(self.screen, BLACK, (5, 171), (500, 171), 2)
    pygame.draw.line(self.screen, BLACK, (5, 335), (500, 335), 2)


  def startStopHandler(self):
    self.changeAlgorithm()
    if not self.checkStartingConditions(self.dropdown.getSelected()): return

    self.surface = self.baseFont.render('', True, BLACK)
    self.startButton.text = self.baseFont.render("Start", True, BLACK) if self.runAlgo else self.baseFont.render("Stop", True, BLACK)
    self.runAlgo = not self.runAlgo

  def checkStartingConditions(self, index):
    if index is None:
      self.surface = self.baseFont.render('Please select an algorithm', True, RED)
      return False
    elif not isBoardValid(self.board):
      self.surface = self.baseFont.render('Invalid Board State', True, RED)
      return False
    return True

  def finish(self): 
    self.runAlgo = False
    self.startButton.text = self.baseFont.render("Start", True, BLACK)
    self.surface = self.baseFont.render(f'Number of calls: {self.numCalls}', True, GREEN)
    self.changeAlgorithm(True)

  def changeAlgorithm(self, finished = False): 
    index = self.dropdown.getSelected()
    if finished: index = -1 # always change if algorithm changed
    if index == self.prevIndex or index is None or self.runAlgo: return
    self.currentAlgo = algorithmsList[index](self.board, 0, 0)
    self.prevIndex = index


  def clearBoard(self):
    for i in range(len(self.board)):
      for j in range(len(self.board[i])):
        self.board[i][j].setText("")

  def randomizeBoard(self):
    self.clearBoard()
    boardGenerator(self.board, 0, 0, [1, 2, 3, 4, 5, 6, 7, 8, 9])
    pokeHoles(self.board)
    # print(isBoardValid(self.board))
