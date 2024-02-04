import numpy as np 
from algorithms.validCheckers import insertChecker

class Calls:
    callNum = 0

c = Calls()

def mrvBacktracking(board, *args):
  c.callNum += 1
  validVals = []
  done = True

  for i in range(0, 9):
    for j in range(0, 9):
      if board[i][j].getText() != "":
          continue
      done = False
      counter = 0
      for num in range(1, 10):
          if insertChecker(i, j, num, board):
              counter += 1
      validVals.append((i, j, counter))

  if done:
      print(c.callNum)
      yield board
      raise StopIteration
  else:
    third_vals = [t[2] for t in validVals]
    i = np.argmin(third_vals)
    if third_vals[i] == 0:
      return False

    row = validVals[i][0]
    col = validVals[i][1]

    for i in range(1, 10):
      if insertChecker(row, col, i, board):
        board[row][col].textColour = (250, 10, 10)
        board[row][col].setText(str(i))
        yield board
        yield from mrvBacktracking(board)
        board[row][col].setText("")
