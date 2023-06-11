import best_move as bm
import constants as cnst
import text_ui as tu

test_data = (
    (
        # Position to analize
        [
        [1,1,0,1,1],
        [2,2,0,0,0],
        [2,0,2,0,0],
        [0,3,0,0,1],
        [0,0,0,2,0]],

        # Depth
        1,

        # Expected position
        [
        [1,1,0,1,1],
        [2,2,0,0,0],
        [2,0,2,0,0],
        [0,0,0,0,1],
        [3,0,0,2,0]],

        # Expected evaluation of the position
        cnst.max_int
    ),

(
        # Position to analize
        [
        [1,2,0,2,0],
        [2,0,0,0,3],
        [0,0,2,1,1],
        [0,0,0,0,1],
        [0,0,2,1,0]],
        
        # Depth
        2,

        # Expected position
        [
        [1,2,0,2,0],
        [2,0,0,3,0],
        [0,0,2,1,1],
        [0,0,0,0,1],
        [0,2,0,1,0]],

        # Expected evaluation of the position
        cnst.min_int
    ),

)

def test_fun(pos, depth, expected_position, expected_value):
    errors_found = 0
    value , new_pos = bm.find_best_move(pos, depth, cnst.comp_player)

    if value != expected_value:
        print("Test failed because")
        print(f"    Actual value = {value}")
        print(f"    Expected value = {expected_value}")
        errors_found += 1

    if new_pos != expected_position:
        print("Test failed because")
        print("    Actual position = ")
        tu.print_position(new_pos)
        print("    Expected position = ")
        tu.print_position(expected_position)
        errors_found += 1

    if errors_found == 0:
        print("Test passed successufully")

#print(test_data)
for element in test_data:
    pos, depth, expected_position, expected_value = element
    test_fun(pos, depth, expected_position, expected_value)