
# Function that checks if the whole board is valid
def isBoardValid(board): 
  for i in range(0,9):
    for j in range(0,9):
      if not indexChecker(i, j, board): return False
  return True


# Function that checks if for a specific index, the row, column and 3x3 grid are valid
def indexChecker(i, j, board):
    seen = set()
    for index in range(0, 9):
      cur = board[i][index].getText()
      if cur == "": continue
      elif not cur in seen: seen.add(cur)
      else: return False
    seen.clear()
    for index in range(0, 9):
      cur = board[index][j].getText()
      if cur == "": continue
      elif not cur in seen: seen.add(cur)
      else: return False
    seen.clear()
    startIndexCol = i // 3 * 3
    startIndexRow = j // 3 * 3 
    for index in range(0, 3):
      for index2 in range(0,3):
        cur =  board[startIndexCol + index][startIndexRow + index2].getText()
        if cur == "": continue
        elif not cur in seen: 
            seen.add(cur)
        else: return False
    return True

# Function that checks if a number can be inserted in a specific index
def insertChecker(i : int, j : int, num: int, board) -> bool:
    num = str(num)
    for index in range(0, 9):
        cur = board[i][index].getText()
        if board[i][index].getText() == "": continue
        elif board[i][index].getText() == num: return False
    for index in range(0, 9):
        cur = board[index][j].getText()
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
