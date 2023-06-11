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
def find_best_move(pos, depth, player):
    terminal_position_result = gmr.check_terminal_position(player, pos)

    if terminal_position_result == 0:
        if depth == 0:
            return (heuristic_value(pos), None)
        
        result_position = None
        result_value = cnst.min_int if player == cnst.comp_player else cnst.max_int 

        comp_positions = mg.generate_all_moves(pos, player, False)

        for child_position in comp_positions:
            position_value, _ = find_best_move(child_position, depth-1, 3 - player) #Change one player to opposite (3-1=2,3-2=1)

            if player == cnst.comp_player:
                if position_value >= result_value:
                    result_value = position_value
                    result_position = child_position
            else:
                if position_value <= result_value:
                    result_value = position_value
                    result_position = child_position
            
        
        return (result_value, result_position)
    
    else:
        if terminal_position_result == 1 and player == 2:
            result = cnst.max_int
        elif terminal_position_result == 1 and player == 1:
            result = cnst.min_int
        elif terminal_position_result == -1 and player == 2:
            result = cnst.min_int
        else:
            result = cnst.max_int
        
        return (result, None)
    





