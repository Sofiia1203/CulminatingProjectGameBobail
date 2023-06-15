import game_move_rules as gmr
import text_ui as tu
import moves_generator as mg
import sys
import constants as cnst
import best_move as bm

#2D list that represents the game board
pos = [
[1,1,1,1,1],
[0,0,0,0,0],
[0,0,3,0,0],
[0,0,0,0,0],
[2,2,2,2,2]]

print(".----------------. .----------------. .----------------. .----------------. .----------------. .----------------.") 
print("| .--------------. | .--------------. | .--------------. | .--------------. | .--------------. | .--------------. |")
print("| |   ______     | | |     ____     | | |   ______     | | |      __      | | |     _____    | | |   _____      | |")
print("| |  |_   _ \    | | |   .'    `.   | | |  |_   _ \    | | |     /  \     | | |    |_   _|   | | |  |_   _|     | |")
print("| |    | |_) |   | | |  /  .--.  \  | | |    | |_) |   | | |    / /\ \    | | |      | |     | | |    | |       | |")
print("| |    |  __'.   | | |  | |    | |  | | |    |  __'.   | | |   / ____ \   | | |      | |     | | |    | |   _   | |")
print("| |   _| |__) |  | | |  \  `--'  /  | | |   _| |__) |  | | | _/ /    \ \_ | | |     _| |_    | | |   _| |__/ |  | |")
print("| |  |_______/   | | |   `.____.'   | | |  |_______/   | | ||____|  |____|| | |    |_____|   | | |  |________|  | |")
print("| |              | | |              | | |              | | |              | | |              | | |              | |")
print("| '--------------' | '--------------' | '--------------' | '--------------' | '--------------' | '--------------' |")
print("'----------------' '----------------' '----------------' '----------------' '----------------' '----------------' ")

print("\n------------------------------- Welcome to the fascinating world of a game BOBAIL! -------------------------------")
print("\n")
level = tu.enter_level()
print("\nGood Luck!")
tu.print_position(pos)

try:
    #User makes their first move
    r1,c1,r2,c2 = tu.enter_regular_move(pos,cnst.user_player,"Enter your first move. ")
except Exception:
    sys.exit()

# Set the value of the starting position cell to 0
pos[r1][c1] = 0
# Set the value of the destination position cell to the user player value
pos[r2][c2] = cnst.user_player
# Print updated position
tu.print_position(pos)

#Main game loop
while True:
    print("Let me think...")
    #Computer makes a move
    
    _ , pos = bm.find_best_move(pos, level, cnst.comp_player)

    if pos != None:
        tu.print_position(pos)
        check_result = gmr.check_terminal_position(cnst.user_player, pos)
        if check_result == 1:
            print("Congratulations! You won!")
            break
        elif check_result == -1:
            print("You lost! Game over!")
            break
    else:
        print("There are no moves for me. You win!")
        break
    
    try:
        # The next player's move
        # The yellow move
        r1,c1,r2,c2 = tu.enter_yellow_move(pos, "Make a move with the cross. ") 
        pos[r1][c1] = 0
        pos[r2][c2] = 3
        tu.print_position(pos)
        
        # Ask for user's input of regular move if yellow move not to the first or last row
        if not (r2 == 0 or r2 == 4): 
            # The move with regular stone
            r1,c1,r2,c2 = tu.enter_regular_move(pos,cnst.user_player,"Enter your first move. ")
            pos[r1][c1] = 0
            pos[r2][c2] = cnst.user_player
            tu.print_position(pos)
    except Exception:
        break

    check_result = gmr.check_terminal_position(cnst.comp_player,pos)
    if check_result ==-1:
        print("Congratulations! You won!")
        break
    elif check_result == 1:
        print("You lost! Game over!")
        break