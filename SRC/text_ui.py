import game_move_rules as gmr

board_cell_to_string = {
    0:" ",
    1:"*",
    2:"@",
    3:"+"
}

def ps(pos,r,c):
    return board_cell_to_string[pos[r][c]]

#The design of the displayed board
def print_position(pos):
    
    print(" ")
    print("  ---------------------")
    print(f"5 | {ps(pos,4,0)} | {ps(pos,4,1)} | {ps(pos,4,2)} | {ps(pos,4,3)} | {ps(pos,4,4)} |")
    
    print("  ---------------------")
    print(f"4 | {ps(pos,3,0)} | {ps(pos,3,1)} | {ps(pos,3,2)} | {ps(pos,3,3)} | {ps(pos,3,4)} |")
    
    print("  ---------------------")
    print(f"3 | {ps(pos,2,0)} | {ps(pos,2,1)} | {ps(pos,2,2)} | {ps(pos,2,3)} | {ps(pos,2,4)} |")

    print("  ---------------------")
    print(f"2 | {ps(pos,1,0)} | {ps(pos,1,1)} | {ps(pos,1,2)} | {ps(pos,1,3)} | {ps(pos,1,4)} |")
    
    print("  ---------------------")
    print(f"1 | {ps(pos,0,0)} | {ps(pos,0,1)} | {ps(pos,0,2)} | {ps(pos,0,3)} | {ps(pos,0,4)} |")
    
    print("  ---------------------")
    print("    1   2   3   4   5")
    print(" ")


def parse_move(user_input):
    # Splits the user's input into a list using whitespace as the separator 
    coordinates = user_input.split(maxsplit = 4) 
    # Convert the strings to integers and return as a tuple
    return (int(coordinates[0]), int(coordinates[1]), int(coordinates[2]), int(coordinates[3])) 

def parse_yellow_move(user_input):
    # Splits the user's input into a list using whitespace as the separator
    coordinates = user_input.split(maxsplit = 4) 
    # Transform the strings to integers and return as a tuple
    return (int(coordinates[0]), int(coordinates[1])) 

# Ask the user to enter a regular move
def enter_regular_move(pos,player,move_description):
    while True:
        user_input = input(f"{move_description}ex. 1 1 4 1, means move a stone from cell 1 1 (row=1, col=1) to cell 4 1 (row=4, col=1): ")
        # Check if the user wants to stop the game
        if user_input.lower() == "stop":
            raise Exception("User stopped the game")
        try:
            # Parse the user's input into separate integers
            r1,c1,r2,c2 = parse_move(user_input) 
        except ValueError:
            print("Input was not recognized! Try again!")
            continue
        if gmr.is_correct_move(pos,player,r1-1,c1-1,r2-1,c2-1): # Checks if the move is correct
            print("Great move!") 
            # Returns the coordinates of the move as a tuple and makes them 0-based 
            return (r1-1,c1-1,r2-1,c2-1)
        else: 
            print("Invalid move!")

# Ask the user to enter a move with the yellow stone
def enter_yellow_move(pos,move_description):
    yellow_r,yellow_c = gmr.find_yellow_stone(pos)
    while True:
        # Ask the user to enter where to move the yellow stone
        user_input = input(f"{move_description}The cross is placed in {yellow_r+1} {yellow_c+1}. Enter the coordinates of a destination cell. Ex. 3 4, means move to row 3, col 4: ")
        # Check if the user wants to stop the game
        if user_input.lower() == "stop": 
            raise Exception("User stopped the game")
        try:
            # Parse the user's input into separate integers
            r2,c2 = parse_yellow_move(user_input)
        except ValueError: 
            print("Input was not recognized! Try again!")
            continue
        if gmr.is_correct_yellow_move(pos,yellow_r,yellow_c,r2-1,c2-1): # Checks if the move is correct according to "is_correct_yellow_move"
            print("Great move!")
            return (yellow_r,yellow_c,r2-1,c2-1)
        else: 
            print("Incorrect move!")

# Ask user to enter the level of difficulty
def enter_level():
    while True:
        level_str = input("Enter the level of difficulty(1. Rookie 2.Intermidiate 3.Expert): ")
        # Check if the user wants to stop the game
        if level_str.lower() == "stop": 
            raise Exception("User stopped the game")
        try:
            # Transform the input to an integer
            level = int(level_str) 
        except ValueError: 
            print("Input was not recognized! Try again!")
            continue
        # Check if the level is within the specific range
        if level >= 1 and level <= 3: 
            return level
        else: 
            print("Input is incorrect! Try again!")