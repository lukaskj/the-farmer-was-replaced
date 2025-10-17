import utils

def zigzag():
  change_hat(Hats.Dinosaur_Hat)
  
  
  maxX = get_world_size() - 1
  maxY = get_world_size() - 1
  
  directions = {
    (0,0): North,
    (0,maxY): East,
    (1,1): East,
    (maxX,1): South,
    (maxX,0): West,
  }

  i = 0
  while i < maxY - 1:
    directions[(1, maxY - i)] = East
    directions[(1, maxY - i - 1)] = South
    directions[(maxX, maxY - i)] = South
    directions[(maxX, maxY - i - 1)] = West  
    i += 2


  for k in directions:
    quick_print(k, directions[k])



  direction = directions[(0,0)]
  while True:
    curPos = utils.getPos()
    if curPos in directions:
      direction = directions[curPos]
    moved = move(direction)
    if not moved:
      harvest()

def start():
  zigzag()

def _exec():
  global maxDrones
  global width
  global height
  global runs

  clear()
  set_world_size(10)
  # set_execution_speed(2)

  # startTime = get_time()
  # _start = num_items(Items.Bone)

  start()
  # quick_print("Found", str(num_items(Items.Bone) - _start), "pumpkins in", get_time() - startTime, "seconds")



if __name__ == "__main__":
  quick_print("### DISABLE FOR SIMULATION ###")
  seed = Entities.Sunflower
  runs = 1
  maxDrones = max_drones()
  width = get_world_size()
  height = get_world_size()

  _exec()