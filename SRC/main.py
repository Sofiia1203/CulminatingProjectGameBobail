import game_move_rules as gmr
import text_ui as tu
import moves_generator as mg
import random

user_player = 1
comp_player = 2

#2D list that represents the game board
pos = [
[1,1,1,1,1],
[0,0,0,0,0],
[0,0,3,0,0],
[0,0,0,0,0],
[2,2,2,2,2]]

print("Welcome to the fascinating world of a game BOBAIL!")
tu.print_position(pos)

#User makes their first move
r1,c1,r2,c2 = tu.enter_regular_move(pos,user_player,"Enter first move....")

pos[r1][c1] = 0
pos[r2][c2] = user_player
tu.print_position(pos)

#Main game loop
while True:
    print("Let me think...")
    #Computer makes a move
    comp_positions = mg.generate_all_moves(pos,comp_player,False) #Generates all possible moves for the computer using "pos" which is the game board, and indicates that it's not the user's turn, which determines what pieces can move
    number_of_positions = len(comp_positions) #Determine the number of possible positions to choose from
    selected_position_index = random.randint(0,number_of_positions-1) #Randomly selects one possible position to display as the computer's next move
    pos = comp_positions[selected_position_index] #Updates the "pos"
    tu.print_position(pos)
    
    check_result = gmr.check_terminal_position(user_player,pos)
    if check_result == 1:
        print("Congratulations! You won!")
        break
    elif check_result == -1:
        print("You lost! Game over!")

    #The next player's move
    #The yellow move
    r1,c1,r2,c2 = tu.enter_yellow_move(pos,"Make a move with the yellow stone....") 
    pos[r1][c1] = 0
    pos[r2][c2] = 3
    tu.print_position(pos)

    #The move with regular stone
    r1,c1,r2,c2 = tu.enter_regular_move(pos,user_player,"Enter first move....")
    pos[r1][c1] = 0
    pos[r2][c2] = user_player
    tu.print_position(pos)

    check_result = gmr.check_terminal_position(comp_player,pos)
    if check_result ==-1:
        print("Congratulations! You won!")
        break
    elif check_result == 1:
        print("You lost! Game over!")
