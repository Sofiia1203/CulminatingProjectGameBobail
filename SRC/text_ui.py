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