neighbouring_cells = ((-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1))

# Indicates the number by which the value of column and row is need to be changed 
def sign(a):
  if a > 0:
    return 1
  elif a < 0:
    return -1
  else:
    return 0

def is_correct_move(pos,player,row1,col1,row2,col2):
  # Check that correct stone in row1 col1
  if pos[row1][col1] != player:
    return False

  # check that row2 col2 is empty cell
  if pos[row2][col2] != 0:
    return False

  # check that row1 col1 and row2 col2 are different cells
  if row1==row2 and col1==col2:
    return False
    
  # check that row1 col1 and row2 col2 are on the same line: vertical or horizontal or diagonal
  if not (row1 == row2 or col1 == col2 or row1+col1 == row2+col2 or row1-col1 == row2-col2):
    return False
    
  # check that all cells of the line are empty
  # vector (delta_row,delta_col) represents the direction from starting to the destination position
  delta_row = sign(row2-row1) # applies the function "sign" to the difference of distination and starting position to get direction
  delta_col = sign(col2-col1) # applies the function "sign" to the difference of distination and starting position to get direction
  r = row1
  c = col1
  while True:
    # cell with coordinates(r,c) is the next cell in the line
    r += delta_row 
    c += delta_col
    if pos[r][c] != 0: # if any cell in the line is not equal to zero(means not empty) then move on this line is incorrect
      return False
    if r == row2 and c == col2:
      break

  # check that r c are on the edge of the board
  if r == 0 or r == 4 or c == 0 or c ==4:
    return True
    
  # check that the next cell in line is occupied
  r += delta_row
  c += delta_col
  if pos[r][c] != 0: # if coordinates(r and c) of a cell are not equal to zero, means that the cell is occupied 
    return True
  else: 
    return False

# Checks if the move with the yellow stone was properly done
def is_correct_yellow_move(pos,row1,col1,row2,col2):
  if pos[row1][col1] == 3: # checks that the a yellow stone is present in the starting cell
    if pos[row2][col2] == 0: # check that the destination cell is empty
      if abs(row1-row2) <= 1 and abs(col1-col2) <= 1 and not (row1==row2 and col1==col2): # checks if the destination cell is a neighbour to the starting cell and not the same cell.
        return True
  return False

# Find the yellow stone's cell
def find_yellow_stone(pos):
    # checks each row and column on the game board
    for r in range(0,5): 
        for c in range(0,5):
            if pos[r][c] == 3: # if a cell, where the value is 3, is found, returns its row and column indices as a tuple
                return (r,c)

# Checks according to rules of the game whether a player won or not
# returns: 
#   1: player wins
#   0: nobody wins. game continues
#   -1: player loses 
def check_terminal_position(player,pos):
  r_yellow,c_yellow = find_yellow_stone(pos)
  if r_yellow == 0:
    if player == 1:
      return -1
    else:
      return 1
  
  if r_yellow == 4:
    if player == 2:
      return -1
    else:
      return 1
    
  
  for cell in neighbouring_cells:
    r = r_yellow + cell[0]
    c = c_yellow + cell[1]
    if r >= 0 and c >= 0 and r <= 4 and c <= 4:
      if pos[r][c] == 0:
        return 0 # nobody wins: game continues
    
  return -1 # means lost because the yellow stone has no way to go
