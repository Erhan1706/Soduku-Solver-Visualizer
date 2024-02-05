import random 
from algorithms.validCheckers import insertChecker

def shuffle(arr):
  for i in range(len(arr)):
    j = random.randint(0, i)
    arr[i], arr[j] = arr[j], arr[i]
  return arr

def printBoard(board):
    for i in range(len(board)):
      for j in range(len(board[i])):
        print(board[i][j].getText(),end="")
      print()


# Should be provided with an empty board
def boardGenerator(board, i, j, numArr):
  if i == 9: return True 
  elif j == 9: return boardGenerator(board, i + 1, 0, numArr) # end of row
  numArr = shuffle(numArr)
  for num in range(len(numArr)):
    if insertChecker(i, j, numArr[num], board):
      board[i][j].textColour = (0, 0, 0)
      board[i][j].setText(str(numArr[num]))
      if boardGenerator(board, i, j + 1, numArr): return True
      board[i][j].setText("")
  return False

def pokeHoles(board):
  numHoles = random.randint(20, 80)
  indexes = shuffle([*range(1,81)])
  removed = 0
  while removed < numHoles:
    i = indexes[removed] // 9
    j = indexes[removed] % 9
    board[i][j].setText("")
    removed += 1


