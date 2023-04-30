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

while True:
    user_input = input("Enter first move....ex. 1 1 4 1, means move a stone from cell 1 1 (row=1, col=1) to cell 4 1 (row=4, col=1): ")
    r1,c1,r2,c2 = tu.parse_move(user_input)
    if gmr.is_correct_move(pos,user_player,r1-1,c1-1,r2-1,c2-1):
        print("Great move!")
        break
    else: 
        print("Incorrect move!")

pos[r1-1][c1-1] = 0
pos[r2-1][c2-1] = user_player
tu.print_position(pos)
print("Let me think...")

while True:
    comp_positions = mg.generate_all_moves(pos,comp_player,False)
    number_of_positions = len(comp_positions)
    selected_position_index = random.randint(0,number_of_positions-1)
    pos = comp_positions[selected_position_index]
    tu.print_position(pos)
    break