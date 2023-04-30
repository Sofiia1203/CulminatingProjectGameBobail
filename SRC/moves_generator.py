import copy
import game_move_rules as gmr

def generate_all_moves(pos,player,is_first_move):
    result = []

    if not is_first_move:
        #generates all moves with the yellow stone
         for r1 in range(0,4):
              for c1 in range(0,4):
                    for r2 in range(0,4):
                        for c2 in range(0,4):
                             if gmr.is_correct_yellow_move(pos,r1,c1,r2,c2):
                                new_pos = copy.deepcopy(pos)
                                new_pos[r1][c1] = 0
                                new_pos[r2][c2] = 3
                                result.append(new_pos) 
