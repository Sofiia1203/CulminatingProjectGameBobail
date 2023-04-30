import game_move_rules as gmr

board_cell_to_string = {
    0:" ",
    1:"*",
    2:"@",
    3:"+"
}

def ps(pos,r,c):
    return board_cell_to_string[pos[r][c]]


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
    coordinates = user_input.split(maxsplit = 4)
    return (int(coordinates[0]), int(coordinates[1]), int(coordinates[2]), int(coordinates[3]))

def parse_yellow_move(user_input):
    coordinates = user_input.split(maxsplit = 4)
    return (int(coordinates[0]), int(coordinates[1]))

def enter_regular_move(pos,player,move_description):
    while True:
        user_input = input(f"{move_description}ex. 1 1 4 1, means move a stone from cell 1 1 (row=1, col=1) to cell 4 1 (row=4, col=1): ")
        r1,c1,r2,c2 = parse_move(user_input)
        if gmr.is_correct_move(pos,player,r1-1,c1-1,r2-1,c2-1):
            print("Great move!")
            return (r1-1,c1-1,r2-1,c2-1)
        else: 
            print("Incorrect move!")

#find the yellow stone's cell
def find_yellow_stone(pos):
    for r in range(0,5):
        for c in range(0,5):
            if pos[r][c] == 3:
                return (r,c)

def enter_yellow_move(pos,move_description):
    yellow_r,yellow_c = find_yellow_stone(pos)
    while True:
        user_input = input(f"{move_description} Yellow stone is placed in {yellow_r+1} {yellow_c+1}. Enter where to move. Ex. 3 4, means move to row 3, col 4: ")
        r2,c2 = parse_yellow_move(user_input)
        if gmr.is_correct_yellow_move(pos,yellow_r,yellow_c,r2-1,c2-1):
            print("Great move!")
            return (yellow_r,yellow_c,r2-1,c2-1)
        else: 
            print("Incorrect move!")
