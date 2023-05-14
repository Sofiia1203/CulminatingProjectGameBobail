import best_move as bm
import constants as cnst
import text_ui as tu
from timeit import default_timer as timer

pos = [
[1,1,0,1,1],
[2,2,0,0,0],
[2,0,2,0,0],
[0,3,0,0,1],
[0,0,0,2,0]]

start = timer()

value , new_pos = bm.find_best_move(pos, 2, cnst.comp_player)
end = timer()
print(f"Time:{end - start}") 

tu.print_position(pos)
print(value)
tu.print_position(new_pos)