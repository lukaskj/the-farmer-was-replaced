from globals import w, h, SEEDS_TO_GROUND, ITEM_TO_SEED, SEED_TO_ITEM

def is_even(n):
  return n % 2 == 0

def harvest_column():
  for _ in range(get_world_size()):
    harvest()
    move(North)

def get_pos():
  return get_pos_x(), get_pos_y()

def get_pos_with_next(maxX = None, maxY = None):
  nextX, nextY = get_next_pos(maxX, maxY)
  return nextX, nextY

def get_next_pos(maxW = None, maxH = None):
  global w
  global h
  x, y = get_pos()
  if maxW == None or maxH == None:
    maxW = w
    maxH = h
  nextX = (x + 1) % maxW
  nextY = y
  if nextX == 0:
    nextY = (y + 1) % maxH
  return nextX, nextY

# function to sort a list of tuples by x-coordinate only, using an optimized bubble sort
def sort_coordinates(tuples):
  n = len(tuples)
  swapped = True
  while swapped:
    swapped = False
    for i in range(n - 1):
      if tuples[i][0] > tuples[i + 1][0]:
        tuples[i], tuples[i + 1] = tuples[i + 1], tuples[i]
        swapped = True
    n -= 1  # Last element is already in place after each pass
  return tuples

def move_to(x, y):
    width = w
    dx = x - get_pos_x()
    dy = y - get_pos_y()
    
    if dx > 0:
        if dx > width/2:
            move(West)    
        else:
            move(East)
    elif dx < 0:
        if abs(dx) > width/2:
            move(East)        
        else:
            move(West)
                    
    if dy > 0:
        if dy > width/2:
            move(South)        
        else:
            move(North)
    elif dy < 0:
        if abs(dy) > width/2:
            move(North)
        else:
            move(South)
    
    if not (get_pos_x() == x and get_pos_y() == y):
        move_to(x, y)
    else:
        return

def get_ground_to_plant(seed):
  curGround = get_ground_type()
  ground = Grounds.Grassland
  if seed in SEEDS_TO_GROUND:
    ground = SEEDS_TO_GROUND[seed]
  
  return curGround != ground, ground

def item_to_seed(item):
  if not item in ITEM_TO_SEED:
    quick_print("No item found in ITEM_TO_SEED map: " + str(item))
    return None
  return ITEM_TO_SEED[item]

def seed_to_item(seed):
  if not seed in SEED_TO_ITEM:
    quick_print("No item found in SEED_TO_ITEM map: " + str(seed))
    return None
  return SEED_TO_ITEM[seed]

def sleep(secondsToWait):
  start = get_time()
  elapsed = 0
  while elapsed < secondsToWait:
    elapsed = get_time() - start
  return

def wait_for(fnc):
  while not fnc():
    pass
  return True