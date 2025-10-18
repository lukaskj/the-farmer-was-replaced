from globals import SEEDS_TO_GROUND, ITEM_TO_SEED, SEED_TO_ITEM

def isEven(n):
  return n % 2 == 0

def getPos():
  return get_pos_x(), get_pos_y()

def getPosWithNext(maxX = None, maxY = None):
  curX, curY = getPos()
  nextX, nextY = getNextPos(maxX, maxY, curX, curY)
  return nextX, nextY, curX, curY

def getNextPos(maxW = None, maxH = None, curX = None, curY = None):
  global w
  global h
  if curX == None or curY == None:
    x, y = getPos()
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

def canUseWater(plots):
  return num_items(Items.Water) >= plots and get_water() < 0.5

# function to sort a list of tuples by x-coordinate only, using an optimized bubble sort
def sortCoordinates(tuples):
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

def moveTo(toX, toY):
  w, h = get_world_size(), get_world_size()
  curX, curY = getPos()  
  halfX = w / 2
  halfY = h / 2

  if toX >= w:
    toX = toX % w
  if toY >= h:
    toY = toY % w

  if curX != toX:
    dx = toX - curX
    while toX != get_pos_x():
      if dx > 0:
        if dx > halfX:
          move(West)
        else:
          move(East)
      elif dx < 0:
        if abs(dx) > halfX:
          move(East)
        else:
          move(West)

  if curY != toY:
    dy = toY - curY
    while toY != get_pos_y():
      if dy > 0:
        if dy > halfY:
          move(South)
        else:
          move(North)
      elif dy < 0:
        if abs(dy) > halfY:
          move(North)
        else:
          move(South)

def moveToOld(x, y):
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
    moveTo(x, y)
  else:
    return

def getGroundToPlant(seed):
  curGround = get_ground_type()
  ground = Grounds.Grassland
  if seed in SEEDS_TO_GROUND:
    ground = SEEDS_TO_GROUND[seed]
  
  return curGround != ground, ground

def plantSeed(seed, force = False):
  souldTill, _ = getGroundToPlant(seed)
  if souldTill:
    till()
  planted = plant(seed)

  return planted

def itemToSeed(item):
  if not item in ITEM_TO_SEED:
    quick_print("No item found in ITEM_TO_SEED map: " + str(item))
    return None
  return ITEM_TO_SEED[item]

def seedToItem(seed):
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

def waitFor(fnc, _sleep = 0.2):
  result = fnc()
  while result == None or result == False:
    result = fnc()
    if _sleep > 0:
      sleep(_sleep)
  return result


# Sort - Quicksort
def __default_compare(a, b):
  return a <= b

def _partition(arr, low, high, compareFn):
  # Choose rightmost element as pivot
  pivot = arr[high]
  # Pointer for greater element
  i = low - 1
  
  # Compare each element with pivot using compare_fn
  for j in range(low, high):
    if compareFn(arr[j], pivot):
      # If element should come before pivot according to compare_fn
      # swap it with the greater element pointed by i
      i += 1
      arr[i], arr[j] = arr[j], arr[i]
  
  # Swap the pivot element with the greater element specified by i
  arr[i + 1], arr[high] = arr[high], arr[i + 1]
  # Return the partition point
  return i + 1

def __quicksortHelper(arr, low, high, compare_fn):
  if low < high:
    # Find pivot element such that
    # elements that compare true are on the left
    # elements that compare false are on the right
    pi = _partition(arr, low, high, compare_fn)
    
    # Recursively sort elements before and after partition
    __quicksortHelper(arr, low, pi - 1, compare_fn)
    __quicksortHelper(arr, pi + 1, high, compare_fn)

def sort(list, compareFn=None):
  if not list:
    return list
  
  # Use default comparison if none provided
  if compareFn == None:
    compareFn = __default_compare
    
  __quicksortHelper(list, 0, len(list) - 1, compareFn)
  return list

def getNextSubgridPos(offset_x, offset_y, subgrid_width, subgrid_height):
  cur_x, cur_y = getPos()
  # Convert current position to subgrid coordinates
  local_x = cur_x - offset_x
  local_y = cur_y - offset_y
  
  # Calculate next position within subgrid
  next_local_x = local_x + 1
  next_local_y = local_y
  
  # If we've reached the end of the row, wrap to next row
  if next_local_x >= subgrid_width:
    next_local_x = 0
    next_local_y = local_y + 1
  
  # If we've gone past the last row, stay at current position
  if next_local_y >= subgrid_height:
    next_local_x = local_x
    next_local_y = local_y
  
  # Convert back to parent grid coordinates
  next_x = next_local_x + offset_x
  next_y = next_local_y + offset_y
  
  return next_x, next_y

def moveToNextSubgridPosSimple(gridCoords):
  startX, startY, subgridWidth, subgridHeight = gridCoords
  return moveToNextSubgridPos(startX, startY, subgridWidth, subgridHeight)

def moveToNextSubgridPos(startX, startY, subgridWidth, subgridHeight):
  nextX, nextY = getNextSubgridPos(startX, startY, subgridWidth, subgridHeight)
  moveTo(nextX, nextY)
  return nextX, nextY

# AI generated
def calculateSubgrids(gridWidth, gridHeight, maxSubgrids):
  # Calculate optimal subgrid divisions for a given grid size and maximum number of subgrids.
  # 
  # Args:
  #   gridWidth: Width of the parent grid
  #   gridHeight: Height of the parent grid
  #   maxSubgrids: Maximum number of subgrids to create
  # 
  # Returns:
  #   List of subgrids, each as [offset_x, offset_y, width, height]
  
  # If maxSubgrids is 1 or less, return the entire grid
  if maxSubgrids <= 1:
    return [[0, 0, gridWidth, gridHeight]]
  
  # Find the best factorization for dividing the grid
  # Try to find factors closest to square root for most balanced division
  best_rows = 1
  best_cols = maxSubgrids
  
  # Find divisors of maxSubgrids that are closest to each other
  i = 1
  while i * i <= maxSubgrids:
    if maxSubgrids % i == 0:
      rows = i
      cols = maxSubgrids // i
      # Prefer more balanced divisions
      if abs(rows - cols) < abs(best_rows - best_cols):
        best_rows = rows
        best_cols = cols
    i = i + 1
  
  # Calculate subgrid dimensions
  subgrid_width = gridWidth // best_cols
  subgrid_height = gridHeight // best_rows
  
  # Create subgrids
  subgrids = []
  for row in range(best_rows):
    for col in range(best_cols):
      offset_x = col * subgrid_width
      offset_y = row * subgrid_height
      
      # Handle remainder pixels for last column/row
      width = subgrid_width
      height = subgrid_height
      
      if col == best_cols - 1:
        width = gridWidth - offset_x
      if row == best_rows - 1:
        height = gridHeight - offset_y
      
      subgrids.append([offset_x, offset_y, width, height])
  
  return subgrids

def isInsideSubgrid(x, y, gridX, gridY, width, height):
  return x >= gridX and x <= (width + gridX - 1) and y >= gridY and y <= (height + gridY - 1)


def round(floatN):
  return floatN // 1


##### REPORTS #####

_reports = {}
def reportStart(item, runs = None, id = "total"):
  _reports[id] = {
    "item": item,
    "runs": runs,
    "startTime": get_time(),
    "startItems": num_items(item)
  }

def reportEnd(id = "total"):
  if not id in _reports:
    quick_print("Not found")
    return False
  _reports[id]["endTime"] = get_time()
  _reports[id]["endItems"] = num_items(_reports[id]["item"])
  _reports[id]["totalTime"] = _reports[id]["endTime"] - _reports[id]["startTime"]
  _reports[id]["totalItems"] = _reports[id]["endItems"] - _reports[id]["startItems"]
  printReport(_reports[id]["totalItems"], _reports[id]["totalTime"], _reports[id]["item"], _reports[id]["runs"])

  return _reports[id]




def printReport(totalAmount, totalTime, entityOrItem = None, runs = None):
  quick_print("--")
  if runs != None and runs > 1:
    quick_print("Runs: " + str(runs))
  if entityOrItem != None:
    quick_print("Harvested", totalAmount, "of", entityOrItem, "in", totalTime, "seconds.")
  else:
    quick_print("Harvested", totalAmount, "in", totalTime, "seconds.")
  quick_print("Avg:", totalAmount / totalTime, "per second")
  if runs != None and runs > 1:
    quick_print("Avg per run:", totalAmount / runs)