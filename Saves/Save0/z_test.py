import utils


# nextPos = utils.get_next_pos(1, 3)
# quick_print(nextPos)
# x, y = get_pos_x(), get_pos_y()
# utils.move_to(nextPos[0] + x, nextPos[1] + y)
# nextPos = utils.get_next_pos(1, 3)
# quick_print(nextPos)

#utils.move_to(0, 0)
subgridX = 3
subgridY = 2
maxX = 3
maxY = 3

x, y = utils.get_next_subgrid_pos(maxX, maxY, subgridX, subgridY)
quick_print(x, y)
utils.move_to(x, y)