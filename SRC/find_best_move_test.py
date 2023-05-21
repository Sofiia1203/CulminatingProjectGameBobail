import best_move as bm
import constants as cnst
import text_ui as tu

errors_found = 0

pos = [
[1,1,0,1,1],
[2,2,0,0,0],
[2,0,2,0,0],
[0,3,0,0,1],
[0,0,0,2,0]]

expected_position = [
[1,1,0,1,1],
[2,2,0,0,0],
[2,0,2,0,0],
[0,0,0,0,1],
[3,0,0,2,0]]

expected_value = cnst.max_int 

value , new_pos = bm.find_best_move(pos, 1, cnst.comp_player)

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