import utils
from globals import WORLD_SIZE

shouldStart = False
varTest = {}

def _can_walk(direction, maxLen = WORLD_SIZE):
  x, y = utils.get_pos()
  if direction == West:
    return x > 0
  if direction == South:
    return y > 0
  if direction == East:
    return x < min(maxLen - 1, WORLD_SIZE - 1)
  if direction == North:
    return y < min(maxLen - 1, WORLD_SIZE - 1)

def plant_and_sort(maxX, maxY, startX, startY):
  seed = Entities.Cactus
  def run():
    for _ in range(maxX * maxY):
      cur_x, cur_y = utils.get_pos()
      nextX, nextY = utils.get_next_subgrid_pos(maxX, maxY, startX, startY)
      
      souldTill, _ = utils.get_ground_to_plant(seed)
      if souldTill:
        till()
      plant(seed)

      utils.move_to(nextX, nextY)
    # sort columns
    for x in range(maxX):
      n = maxY
      swapped = True
      while swapped:
        swapped = False
        utils.move_to(startX, startY)
        for y in range(n - 1):
          if not _is_next_cactus_bigger(North):
            swap(North)
            swapped = True
          move(North)
        n -= 1
        if not swapped:
          break
        
  return run

def sort_rows(maxX, maxY, startX, startY):
  def run():
    # sort rows
    for x in range(maxY):
      n = maxX
      swapped = True
      while swapped:
        swapped = False
        utils.move_to(startX, startY)
        for y in range(n - 1):
          if not _is_next_cactus_bigger(East):
            swap(East)
            swapped = True
          move(East)
        n -= 1
        if not swapped:
          break
  return run


def _is_next_cactus_bigger(direction):
  selfSize = measure()
  nextSize = measure(direction)
  if nextSize != None and selfSize <= nextSize:
    return True
  return False 

def start(_maxWidth, _maxHeight, _maxDrones):
  utils.move_to(0, 0)
  droneList = []
  maxDrones = min(_maxDrones, max_drones())  # Fixed maximum number of drones
  maxWidth = min(_maxWidth, WORLD_SIZE)
  maxHeight = min(_maxHeight, WORLD_SIZE)

  for x in range(maxWidth):
    utils.move_to(x,0)
    while True:
      numDrones = num_drones()
      if numDrones <= maxDrones:
        droneId = spawn_drone(plant_and_sort(1, maxHeight, x, 0))
        if droneId != None:
          droneList.append(droneId)
          break
      else:
        # quick_print("Waiting for idle drones")
        utils.wait_for(_has_idle_drone(droneList, maxWidth))
  
  # quick_print("Waiting for all drones to finish")
  utils.wait_for(_all_drones_finised(droneList))

  for y in range(maxHeight):
    utils.move_to(0,y)
    while True:
      numDrones = num_drones()
      if numDrones <= maxDrones:
        droneId = spawn_drone(sort_rows(maxWidth, 1, 0, y))
        if droneId != None:
          droneList.append(droneId)
          break
      else:
        # quick_print("Waiting for idle drones")
        utils.wait_for(_has_idle_drone(droneList, maxWidth))
  
  utils.wait_for(_all_drones_finised(droneList))

  beforeCount = num_items(Items.Cactus)
  if can_harvest():
    harvest()
  return num_items(Items.Cactus) - beforeCount

def _has_idle_drone(droneList, maxSize):
  def fnc():
    tmpDroneList = droneList[:]    
    hasIdleDrone = False
    for drone in tmpDroneList:
      if has_finished(drone):
        hasIdleDrone = True
        droneList.remove(drone)
    return hasIdleDrone
  return fnc

def _all_drones_finised(droneList):
  def fnc():
    totalFinished = 0
    for drone in droneList:
      if has_finished(drone):
        totalFinished += 1
    return len(droneList) == totalFinished

  return fnc


if __name__ == "__main__":
  startTime = get_time()
  harvested = start(10, 10, max_drones())
  end = get_time()
  quick_print("Harvested", harvested, "in", end - startTime, "seconds")