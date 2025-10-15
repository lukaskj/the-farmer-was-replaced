import utils
from globals import WORLD_SIZE

def _sort_columns(maxX, maxY, startX, startY):
  # sort columns
  for x in range(maxX):
    n = maxY
    swapped = True
    while swapped:
      swapped = False
      utils.moveTo(startX, startY)
      for y in range(n - 1):
        if not _is_next_cactus_bigger(North):
          swap(North)
          swapped = True
        move(North)
      n -= 1
      if not swapped:
        break

    


def _sort_rows(maxX, maxY, startX, startY):
  for x in range(maxY):
    n = maxX
    swapped = True
    while swapped:
      swapped = False
      utils.moveTo(startX, startY)
      for y in range(n - 1):
        if not _is_next_cactus_bigger(East):
          swap(East)
          swapped = True
        move(East)
      n -= 1
      if not swapped:
        break

def _drone_plant_and_sort_cols(maxX, maxY, startX, startY):
  seed = Entities.Cactus
  def run():
    for _ in range(maxX * maxY):
      nextX, nextY = utils.getNextSubgridPos(maxX, maxY, startX, startY)
      
      souldTill, _ = utils.getGroundToPlant(seed)
      if souldTill:
        till()
      plant(seed)

      utils.moveTo(nextX, nextY)
    
    _sort_columns(maxX, maxY, startX, startY)
        
  return run

def _drone_sort_rows(maxX, maxY, startX, startY):
  def run():
    _sort_rows(maxX, maxY, startX, startY)
  return run


def _is_next_cactus_bigger(direction):
  selfSize = measure()
  nextSize = measure(direction)
  if nextSize != None and selfSize <= nextSize:
    return True
  return False 

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
        droneId = utils.spawnDrone(_drone_plant_and_sort_cols(1, maxHeight, x, 0))
        if droneId != None:
          break
      else:
        utils.waitForIdleDrone(maxDrones)

  # _drone_plant_and_sort_cols(1, maxHeight, get_pos_x(), 0)
  utils.waitForAllDronesToFinish()

  for y in range(maxHeight):
    utils.moveTo(0,y)
    while True:
      numDrones = num_drones()
      if numDrones <= maxDrones:
        droneId = utils.spawnDrone(_drone_sort_rows(maxWidth, 1, 0, y))
        if droneId != None:
          break
      else:
        utils.waitForIdleDrone(maxDrones)
  
  utils.waitForAllDronesToFinish()

  beforeCount = num_items(Items.Cactus)
  if can_harvest():
    harvest()
  return num_items(Items.Cactus) - beforeCount

if __name__ == "__main__":
  runs = 20
  width = WORLD_SIZE
  height = WORLD_SIZE
  maxDrones = max_drones()

  harvested = 0
  startTime = get_time()
  for _ in range(runs):
    harvested += start(width, height, maxDrones)
  end = get_time()
  quick_print("Harvested", harvested, "(" + str(width*height) + " plots)", "in", end - startTime, "seconds using", maxDrones, "drones")