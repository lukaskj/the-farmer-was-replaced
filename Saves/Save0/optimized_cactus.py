import utils
import drones
from globals import ORIENTATION_UPDOWN, ORIENTATION_LEFTRIGHT

def _drone_plant_and_sort_cols(maxX, maxY, startX, startY):
  seed = Entities.Cactus
  def run():
    for _ in range(maxX * maxY):
      
      utils.plantSeed(seed)

      utils.moveToNextSubgridPos(startX, startY, maxX, maxY)
    
    utils.moveTo(startX, startY)
    _sort_line_two_way(startY, maxY, ORIENTATION_UPDOWN)
        
  return run

def _drone_sort_rows(maxX, maxY, startX, startY):
  def run():
    utils.moveTo(startX, startY)
    _sort_line_two_way(startX, maxX, ORIENTATION_LEFTRIGHT)
    # _sort_rows(maxX, maxY, startX, startY)
  return run

def _sort_line_two_way(startPos, maxLen, orientation = ORIENTATION_LEFTRIGHT):
  _min = startPos
  _max = min(_min + maxLen, get_world_size())

  increasingDirection = East
  decreasingDirection = West
  if orientation == ORIENTATION_UPDOWN:
    increasingDirection = North
    decreasingDirection = South

  direction = increasingDirection

  while _min < _max:
    swappedForward = False
    swappedBackward = False

    # Forward pass - move in increasing direction
    for _ in range(_max - _min):
      measureSelf = measure()
      measureNext = measure(direction)

      if measureSelf != None and measureNext != None and measureSelf > measureNext:
        swap(direction)
        swappedForward = True

      # Check if we've reached max boundary
      if orientation == ORIENTATION_LEFTRIGHT:
        pos = get_pos_x()
      else:
        pos = get_pos_y()
      
      if pos >= _max - 2:
        break

      move(direction)

    # Update boundary and change direction
    _max -= 1
    direction = decreasingDirection

    # Early exit if sorted
    if not swappedForward:
      break

    # Backward pass - move in decreasing direction
    for _ in range(_max - _min):
      measureSelf = measure()
      measureNext = measure(direction)

      if measureSelf != None and measureNext != None and measureSelf < measureNext:
        swap(direction)
        swappedBackward = True

      # Check if we've reached min boundary
      if orientation == ORIENTATION_LEFTRIGHT:
        pos = get_pos_x()
      else:
        pos = get_pos_y()
      
      if pos <= _min + 1:
        break

      move(direction)

    # Update boundary and change direction
    _min += 1
    direction = increasingDirection

    # Early exit if sorted
    if not swappedBackward:
      break

def start(_maxWidth, _maxHeight, _maxDrones = None):
  utils.moveTo(0, 0)
  if _maxDrones == None:
    maxDrones = max_drones()
  else:
    maxDrones = min(_maxDrones, max_drones())  # Fixed maximum number of drones
  maxWidth = min(_maxWidth, get_world_size())
  maxHeight = min(_maxHeight, get_world_size())

  for x in range(maxWidth):
    utils.moveTo(x,0)
    
    numDrones = num_drones()
    if numDrones <= maxDrones:
      droneId = drones.spawnDrone(_drone_plant_and_sort_cols(1, maxHeight, x, 0))
      if droneId == None and x == maxWidth - 1 and numDrones == maxDrones:
        _drone_plant_and_sort_cols(1, maxHeight, x, 0)()

  # _drone_plant_and_sort_cols(1, maxHeight, get_pos_x(), 0)
  drones.waitForAllDronesToFinish()

  for y in range(maxHeight):
    utils.moveTo(0,y)
    numDrones = num_drones()
    if numDrones <= maxDrones:
      droneId = drones.spawnDrone(_drone_sort_rows(maxWidth, 1, 0, y))
      if droneId == None and y == maxHeight - 1 and numDrones == maxDrones:
        _drone_sort_rows(maxWidth, 1, 0, y)()
  
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
  global leaderboardMin

  harvested = 0
  startTime = get_time()
  # while num_items(Items.Cactus) < minCactus:
  if leaderboardMin != None and leaderboardMin > 0:
    quick_print("Is leaderboard run. Min resouces:", leaderboardMin)
    while harvested < leaderboardMin:
      harvested += start(width, height, maxDrones)
  else:
    for _ in range(runs):
      harvested += start(width, height, maxDrones)
  
  totalTime = get_time() - startTime
  quick_print("Harvested (new)", harvested, "(" + str(width*height) + " plots)", "in", totalTime, "seconds using", maxDrones, "drones")
  quick_print("Average:", harvested / totalTime, "per second")


def _exec2():
  clear()
  set_world_size(12)
  startX = 0
  startY = 5
  lineLength = get_world_size()
  utils.moveTo(startX, startY)
  for _ in range(lineLength):
    utils.plantSeed(Entities.Cactus)
    move(East)
  utils.moveTo(startX, startY)
  set_execution_speed(3)
  _sort_line_two_way(startX, lineLength, ORIENTATION_LEFTRIGHT)
  


if __name__ == "__main__":
  # quick_print("### DISABLE FOR SIMULATION ###")
  
  
  leaderboardMin = 33554432
  runs = 1
  maxDrones = max_drones()
  width = get_world_size()
  height = get_world_size()
  
  # width = 8
  # height = 8
  # set_world_size(8)
  # set_execution_speed(2)
  # maxDrones = 1
  # leaderboardMin = 131072
  
  _exec()


  
  