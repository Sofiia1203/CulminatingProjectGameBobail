import game_move_rules as gmr
import constants as cnst
import moves_generator as mg


def heuristic_value(pos):
    # A variable to store the calculated heuristic value
    result = 0

    # Find the row and column of the yellow stone
    yellow_r, yellow_c = gmr.find_yellow_stone(pos) 
    # Adds the new values to the result based on the distance of the yellow stone from the center row (2)
    result += (yellow_r-2)*500

    # Iterate over the game board
    for r in range(5):
        for c in range(5):
            # Check if the cell contains the computer player's stone
            if pos[r][c] == cnst.comp_player:
                # Check if the stone is above the yellow stone on the game board
                if r < yellow_r:
                    # Increase the result by 50
                    result += 50
            # Check if the cell contains the user player's stone
            if pos[r][c] == cnst.user_player:
                # Check if the stone is below the yellow stone on the game board
                if r > yellow_r:
                    # Decrease the result by 50
                    result -= 50

    # Check the center cell
    # Check if the center cell contains the computer player's stone
    if pos[2][2] == cnst.comp_player:
        # Increase the result by 100
        result += 100
        # Check if the center cell contains the user player's stone
    if pos[2][2] == cnst.user_player:
        # Decrease the result by 100
        result -= 100
    
    return result

def find_best_move(pos, depth, player):
    # Check if it is a terminal position
    terminal_position_result = gmr.check_terminal_position(player, pos)

    if terminal_position_result == 0:
        # Reached the maximum dept
        if depth == 0:
            return (heuristic_value(pos), None)
        
        result_position = None

        if player == cnst.comp_player:
            result_value = cnst.min_int
        else:
            result_value = cnst.max_int

        # Generate all possible moves for the current player
        comp_positions = mg.generate_all_moves(pos, player, False)

        # Iterate over the child positions
        for child_position in comp_positions:
            # Recursively call find_best_move to estimate the child position
            position_value, _ = find_best_move(child_position, depth-1, 3 - player) #Change one player to opposite (3-1=2,3-2=1)

            # Update the best move based on the player
            if player == cnst.comp_player:
                if position_value >= result_value:
                    result_value = position_value
                    result_position = child_position
            else:
                if position_value <= result_value:
                    result_value = position_value
                    result_position = child_position
            
        # Return the best value and corresponding position
        return (result_value, result_position)
    
    else:
        # Determine the result value based on the terminal position and a player
        if terminal_position_result == 1 and player == 2:
            result = cnst.max_int
        elif terminal_position_result == 1 and player == 1:
            result = cnst.min_int
        elif terminal_position_result == -1 and player == 2:
            result = cnst.min_int
        else:
            result = cnst.max_int
        
        # Return the result value and no position
        return (result, None)
    





