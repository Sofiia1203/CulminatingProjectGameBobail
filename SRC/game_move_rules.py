def sign(a):
  if a > 0:
    return 1
  elif a < 0:
    return -1
  else:
    return 0

def is_correct_move(pos,player,row1,col1,row2,col2):
  #check that correct stone in row1 col1
  if pos[row1][col1] != player:
    return False

  #check that row2 col2 is empty cell
  if pos[row2][col2] != 0:
    return False

  #check that row1 col1 and row2 col2 are different cells
  if row1==row2 and col1==col2:
    return False
    
  #check that row1 col1 and row2 col2 are on the same line: vertical or horizontal or diagonal
  if not (row1 == row2 or col1 == col2 or row1+col1 == row2+col2 or row1-col1 == row2-col2):
    return False
    
  #check that all cells of the line are empty
  delta_row = sign(row2-row1)
  delta_col = sign(col2-col1)
  r = row1
  c = col1
  while True:
    r += delta_row
    c += delta_col
    if pos[r][c] != 0:
      return False
    if r == row2 and c == col2:
      break

  #check that r c are on the edge of the board
  if r == 0 or r == 4 or c == 0 or c ==4:
    return True
    
  #check that the next cell in line is occupied
  r += delta_row
  c += delta_col
  if pos[r][c] != 0:
    return True
  else: 
    return False

def is_correct_yellow_move(pos,row1,col1,row2,col2):
  if pos[row1][col1] == 3:
    if pos[row2][col2] == 0:
      if abs(row1-row2) <= 1 and abs(col1-col2) <= 1 and not (row1==row2 and col1==col2):
        return True
  return False
