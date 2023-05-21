import best_move as bm

errors_found = 0

positions = [
([
[1,1,0,1,1],
[2,2,0,0,0],
[2,0,2,0,0],
[0,3,0,0,1],
[0,0,0,2,0]],800),

([
[1,1,1,1,1],
[0,0,0,0,0],
[0,0,3,0,0],
[0,0,0,0,0],
[2,2,2,2,2]],0)]

for pos, expected_heuristic_value in positions:
    actual_value = bm.heuristic_value(pos)

    if actual_value != expected_heuristic_value:
        print("Test failed because")
        print(f"    Actual value = {actual_value}")
        print(f"    Expected value = {expected_heuristic_value}")
        errors_found += 1

if errors_found == 0:
    print("Test passed successufully")