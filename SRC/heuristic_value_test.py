import best_move as bm

# Variable that counts errors
errors_found = 0

# A list of positions and their corresponding value
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

    # Check if the actual value matches the expected value
    if actual_value != expected_heuristic_value:
        # Print the test failure details
        print("Test failed because")
        print(f"    Actual value = {actual_value}")
        print(f"    Expected value = {expected_heuristic_value}")
        errors_found += 1

# Check if any errors were found during the tests
if errors_found == 0:
    print("Test passed successufully")