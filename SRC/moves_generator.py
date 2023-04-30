import copy
import game_move_rules as gmr

def generate_all_moves(pos,player,is_first_move):
    inter_result = []

    if is_first_move:
        inter_result.append(pos)
    else:
        #generates all moves with the yellow stone
        for r1 in range(0,5):
            for c1 in range(0,5):
                for r2 in range(0,5):
                    for c2 in range(0,5):
                        if gmr.is_correct_yellow_move(pos,r1,c1,r2,c2):
                            new_pos = copy.deepcopy(pos)
                            new_pos[r1][c1] = 0
                            new_pos[r2][c2] = 3
                            inter_result.append(new_pos) 

    result = []
    for inter_pos in inter_result:
        #generate all moves with players' stones
        for r1 in range(0,5):
            for c1 in range(0,5):
                for r2 in range(0,5):
                    for c2 in range(0,5):
                        if gmr.is_correct_move(pos,player,r1,c1,r2,c2):
                            new_pos = copy.deepcopy(inter_pos)
                            new_pos[r1][c1] = 0
                            new_pos[r2][c2] = player
                            result.append(new_pos)                      
