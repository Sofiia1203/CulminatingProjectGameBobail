import game_move_rules as gmr
import constants as cnst
import moves_generator as mg


def heuristic_value(pos):
    result = 0
    yellow_r, yellow_c = gmr.find_yellow_stone(pos) 
    result += (yellow_r-2)*500

    for r in range(5):
        for c in range(5):
            if pos[r][c] == cnst.comp_player:
                if r < yellow_r:
                    result += 50
            if pos[r][c] == cnst.user_player:
                if r > yellow_r:
                    result -= 50

    if pos[2][2] == cnst.comp_player:
        result += 100
    if pos[2][2] == cnst.user_player:
        result -= 100
    
    return result
#recursion
def find_best_comp_move(pos,depth):
    if depth == 0:
        return (heuristic_value(pos),None)
    
    result_position = None
    result_value = cnst.min_int

    comp_positions = mg.generate_all_moves(pos,cnst.comp_player,False)
    for child_position in comp_positions:
        position_value, _ = find_best_comp_move(child_position,depth-1)
        if position_value > result_value:
            result_value = position_value
            result_position = child_position
    
    return (result_value,result_position)


