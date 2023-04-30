import game_move_rules as gmr

pos = [[1,1,1,1,1],                                                                            [0,0,0,0,0],                                                                                    [0,0,3,0,0],                                                                                      [0,0,0,0,0],                                                                                   [2,2,2,2,2],]

green = 1
red = 2
empty = 0
yellow = 3

#is_correct_move(pos,1,0,0,2,2)
#print(is_correct_yellow_move(pos,2,2,3,1))
print(gmr.is_correct_move(pos,1,0,0,3,0))