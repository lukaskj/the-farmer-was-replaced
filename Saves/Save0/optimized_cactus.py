import utils
import drones
from globals import WORLD_SIZE, ORIENTATION_UPDOWN, ORIENTATION_LEFTRIGHT

def _drone_plant_and_sort_cols(maxX, maxY, startX, startY):
  seed = Entities.Cactus
  def run():
    addFertilizer = num_items(Items.Weird_Substance) < 10000
    for _ in range(maxX * maxY):
      nextX, nextY = utils.getNextSubgridPos(startX, startY, maxX, maxY)
      
      if can_harvest():
        harvest()
      utils.plantSeed(seed, addFertilizer)

      utils.moveTo(nextX, nextY)
    
    utils.moveTo(startX, startY)
    _sort_line_two_way(startY, maxY, ORIENTATION_UPDOWN)
    # _sort_columns(maxX, maxY, startX, startY)
        
  return run

def _drone_sort_rows(maxX, maxY, startX, startY):
  def run():
    utils.moveTo(startX, startY)
    _sort_line_two_way(startX, maxX, ORIENTATION_LEFTRIGHT)
    # _sort_rows(maxX, maxY, startX, startY)
  return run

def _sort_line_two_way(startPos, maxLen, orientation = ORIENTATION_LEFTRIGHT):
  _min = startPos
  _max = maxLen

  increasingDirection = East
  decreasingDirection = West
  if orientation == ORIENTATION_UPDOWN:
    increasingDirection = North
    decreasingDirection = South
  
  direction = increasingDirection

  while _min < _max:
    swappedMin = False
    swappedMax = False
    for _ in range(_max - _min):
      measureSelf = measure()
      measureNext = measure(direction)
      
      if orientation == ORIENTATION_LEFTRIGHT:
        pos = get_pos_x()
      else:
        pos = get_pos_y()
      
      if (direction == increasingDirection and pos >= _max - 1) or (direction == decreasingDirection and pos <= _min - 1):
        continue
      
      # quick_print("Orientation", orientation, "direction", direction, "measureSelf", measureSelf, "measureNext", measureNext, "pos", pos)
      if direction == increasingDirection and measureSelf > measureNext:
        swap(direction)
        swappedMax = True
      elif direction == decreasingDirection and measureSelf < measureNext:
        swap(direction)
        swappedMin = True
      move(direction)
    
    # Exit if it's already sorted
    if not swappedMax and not swappedMin:
      break

    # Decrease boundaries once reaching them
    if direction == increasingDirection:
      _max -= 1
      direction = decreasingDirection
    else:
      _min += 1
      direction = increasingDirection

def start(_maxWidth, _maxHeight, _maxDrones = None):
  utils.moveTo(0, 0)
  if _maxDrones == None:
    maxDrones = max_drones()
  else:
    maxDrones = min(_maxDrones, max_drones())  # Fixed maximum number of drones
  maxWidth = min(_maxWidth, WORLD_SIZE)
  maxHeight = min(_maxHeight, WORLD_SIZE)

  for x in range(maxWidth):
    utils.moveTo(x,0)
    while True:
      numDrones = num_drones()
      if numDrones <= maxDrones:
        droneId = drones.spawnDrone(_drone_plant_and_sort_cols(1, maxHeight, x, 0))
        if droneId != None:
          break
      else:
        drones.waitForIdleDrone(maxDrones)

  # _drone_plant_and_sort_cols(1, maxHeight, get_pos_x(), 0)
  drones.waitForAllDronesToFinish()

  for y in range(maxHeight):
    utils.moveTo(0,y)
    while True:
      numDrones = num_drones()
      if numDrones <= maxDrones:
        droneId = drones.spawnDrone(_drone_sort_rows(maxWidth, 1, 0, y))
        if droneId != None:
          break
      else:
        drones.waitForIdleDrone(maxDrones)
  
  drones.waitForAllDronesToFinish()

  beforeCount = num_items(Items.Cactus)
  if can_harvest():
    harvest()
  return num_items(Items.Cactus) - beforeCount

def _exec():
  global maxDrones
  global width
  global height
  global runs

  harvested = 0
  startTime = get_time()
  # while num_items(Items.Cactus) < minCactus:
  for _ in range(runs):
    harvested += start(width, height, maxDrones)
  end = get_time()
  quick_print("Harvested", harvested, "(" + str(width*height) + " plots)", "in", end - startTime, "seconds using", maxDrones, "drones")

if __name__ == "__main__":
  quick_print("### DISABLE FOR SIMULATION ###")
  runs = 1
  maxDrones = max_drones()
  width = get_world_size()
  height = get_world_size()
  
  _exec()
  
  