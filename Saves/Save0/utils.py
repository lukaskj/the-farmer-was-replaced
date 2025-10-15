from globals import w, h, SEEDS_TO_GROUND, ITEM_TO_SEED, SEED_TO_ITEM

def is_even(n):
  return n % 2 == 0

def get_pos():
  return get_pos_x(), get_pos_y()

def get_pos_with_next(maxX = None, maxY = None):
  curX, curY = get_pos()
  nextX, nextY = get_next_pos(maxX, maxY, curX, curY)
  return nextX, nextY, curX, curY

def get_next_pos(maxW = None, maxH = None, curX = None, curY = None):
  global w
  global h
  if curX == None or curY == None:
    x, y = get_pos()
  else:
     x, y = curX, curY
  if maxW == None or maxH == None:
    maxW = w
    maxH = h

  nextX = x + 1
  nextY = y
  if nextX >= maxW:
    nextX = 0
    nextY = y + 1
  
  # If we've gone past maxH, stay at current position
  if nextY >= maxH:
    nextX, nextY = x, y
    
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

def wait_for(fnc, max = 1000000000):
  i = 0
  while not fnc() and i < max:
    i += 1
  return True


# Sort - Quicksort
def __default_compare(a, b):
  return a <= b

def _partition(arr, low, high, compare_fn):
  # Choose rightmost element as pivot
  pivot = arr[high]
  # Pointer for greater element
  i = low - 1
  
  # Compare each element with pivot using compare_fn
  for j in range(low, high):
    if compare_fn(arr[j], pivot):
      # If element should come before pivot according to compare_fn
      # swap it with the greater element pointed by i
      i += 1
      arr[i], arr[j] = arr[j], arr[i]
  
  # Swap the pivot element with the greater element specified by i
  arr[i + 1], arr[high] = arr[high], arr[i + 1]
  # Return the partition point
  return i + 1

def __quicksort_helper(arr, low, high, compare_fn):
  if low < high:
    # Find pivot element such that
    # elements that compare true are on the left
    # elements that compare false are on the right
    pi = _partition(arr, low, high, compare_fn)
    
    # Recursively sort elements before and after partition
    __quicksort_helper(arr, low, pi - 1, compare_fn)
    __quicksort_helper(arr, pi + 1, high, compare_fn)

def sort(list, compare_fn=None):
  if not list:
    return list
  
  # Use default comparison if none provided
  if compare_fn == None:
    compare_fn = __default_compare
    
  __quicksort_helper(list, 0, len(list) - 1, compare_fn)
  return list