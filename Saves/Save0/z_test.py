import utils


# nextPos = utils.get_next_pos(1, 3)
# quick_print(nextPos)
# x, y = get_pos_x(), get_pos_y()
# utils.move_to(nextPos[0] + x, nextPos[1] + y)
# nextPos = utils.get_next_pos(1, 3)
# quick_print(nextPos)

utils.move_to(0, 0)
for i in range(get_world_size() * get_world_size()):
  x, y = utils.get_next_pos()
  utils.move_to(x, y)