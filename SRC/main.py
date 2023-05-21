import game_move_rules as gmr
import text_ui as tu
import moves_generator as mg
import random
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

print("Welcome to the fascinating world of a game BOBAIL!")

level = tu.enter_level()

tu.print_position(pos)

try:
    #User makes their first move
    r1,c1,r2,c2 = tu.enter_regular_move(pos,cnst.user_player,"Enter first move....")
except Exception:
    sys.exit()

pos[r1][c1] = 0
pos[r2][c2] = cnst.user_player
tu.print_position(pos)

#Main game loop
while True:
    print("Let me think...")
    #Computer makes a move
    
    _ , pos = bm.find_best_move(pos, level, cnst.comp_player)

    if pos != None:
        tu.print_position(pos)
    
    check_result = gmr.check_terminal_position(cnst.user_player,pos)
    if check_result == 1:
        print("Congratulations! You won!")
        break
    elif check_result == -1:
        print("You lost! Game over!")
        break

    try:
        #The next player's move
        #The yellow move
        r1,c1,r2,c2 = tu.enter_yellow_move(pos,"Make a move with the yellow stone....") 
        pos[r1][c1] = 0
        pos[r2][c2] = 3
        tu.print_position(pos)
        
        if not (r2 == 0 or r2 == 4): # ask for user's input of regular move if yellow move not to the first or last row
            #The move with regular stone
            r1,c1,r2,c2 = tu.enter_regular_move(pos,cnst.user_player,"Enter your move....")
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