import copy
import game_move_rules as gmr

def generate_all_moves(pos,player,is_first_move):
    inter_result = []
    result = []

    if is_first_move: 
        inter_result.append(pos) #Adds the current position to the intermediate result list.
    else:
        #Generates all moves with the yellow stone
        for r1 in range(0,5): #checks if the first coordinate of starting position meets all requirements according to function "is_correct_move" in columns from 0 to 5
            for c1 in range(0,5): #checks if the second coordinate of starting position meets all requirements according to function "is_correct_move" in rows from 0 to 5
                for r2 in range(0,5): #checks if the first coordinate of the destination position meets all requirements according to function "is_correct_move" in columns from 0 to 5
                    for c2 in range(0,5): #checks if the second coordinate of destination position meets all requirements according to function "is_correct_move" in rows from 0 to 5
                        if gmr.is_correct_yellow_move(pos,r1,c1,r2,c2):
                            new_pos = copy.deepcopy(pos) #If the move is valid, makes a copy of the position and updates it on the board.
                            new_pos[r1][c1] = 0 #changes the value of starting position to zero
                            new_pos[r2][c2] = 3 #changes the value of destination position to the value of yellow stone
                            if r2 == 0 or r2 == 4:
                                result.append(new_pos)
                            else:
                                inter_result.append(new_pos) 
                        

    for inter_pos in inter_result:
        #Generate all moves with players' stones
        for r1 in range(0,5): #checks if the first coordinate of starting position meets all requirements according to function "is_correct_move" in columns from 0 to 5
            for c1 in range(0,5): #checks if the second coordinate of starting position meets all requirements according to function "is_correct_move" in rows from 0 to 5
                for r2 in range(0,5): #checks if the first coordinate of the destination position meets all requirements according to function "is_correct_move" in columns from 0 to 5
                    for c2 in range(0,5): #checks if the second coordinate of destination position meets all requirements according to function "is_correct_move" in rows from 0 to 5
                        if gmr.is_correct_move(inter_pos,player,r1,c1,r2,c2):
                            new_pos = copy.deepcopy(inter_pos) #if the move is valid, makes a copy of the position and updates it on the board.
                            new_pos[r1][c1] = 0 #changes the value of starting position to zero
                            new_pos[r2][c2] = player #changes the value of destination position to the player's number
                            result.append(new_pos) 
    return result                     
