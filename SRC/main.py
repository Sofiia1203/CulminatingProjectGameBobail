import game_move_rules as gmr
import text_ui as tu
import moves_generator as mg
import random

user_player = 1
comp_player = 2

pos = [
[1,1,1,1,1],
[0,0,0,0,0],
[0,0,3,0,0],
[0,0,0,0,0],
[2,2,2,2,2]]

print("Welcome.....")
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
    comp_positions = mg.generate_all_moves(pos,comp_player,False)
    number_of_positions = len(comp_positions)
    selected_position_index = random.randint(0,number_of_positions-1)
    pos = comp_positions[selected_position_index]
    tu.print_position(pos)
    
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
