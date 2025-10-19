import utils
import drones
# from globals import WORLD_SIZE

totalGrown = 0
addFertilizer = False

def _droneCode(seed, startX, startY, width, height):
  utils.moveTo(startX, startY)
  plots = width * height
  for i in range(plots):
    if can_harvest():
      harvest()
    utils.plantSeed(seed)
    utils.moveToNextSubgridPos(startX, startY, width, height)


  deadPlants = []
  utils.moveTo(startX, startY)
  for i in range(plots):
    groundEntity = get_entity_type()
    if groundEntity == None or groundEntity == Entities.Dead_Pumpkin or (groundEntity == Entities.Pumpkin and not can_harvest()):
      if groundEntity == None or groundEntity == Entities.Dead_Pumpkin:
        utils.plantSeed(seed)
        use_item(Items.Water)
      deadPlants.append((get_pos_x(), get_pos_y()))
    utils.moveToNextSubgridPos(startX, startY, width, height)
  
  while len(deadPlants) > 0:
    for x, y in deadPlants:
      utils.moveTo(x, y)
      groundEntity = get_entity_type()
      
      if groundEntity == None or groundEntity == Entities.Dead_Pumpkin or (groundEntity != None and not can_harvest()):
        if groundEntity == None or groundEntity == Entities.Dead_Pumpkin:
          utils.plantSeed(seed)
          use_item(Items.Water)
      elif can_harvest():
        deadPlants.remove((x, y))

def __newDrone(seed):
  def _init(grid):
    startX, startY, width, height = grid
    def __():
      _droneCode(seed, startX, startY, width, height)
    return __
  return _init

def start(seed, w, h, maxDrones = None, runs = 1):
  for _ in range(runs):
    controller = __newDrone(seed)
    shouldExecuteLastAsMainDrone, lastGrid, _ = drones.spawnDronesInGrid(controller, w, h, maxDrones)
    if shouldExecuteLastAsMainDrone:
      controller(lastGrid)()
    drones.waitForAllDronesToFinish()
    if can_harvest():
      harvest()
    else:
      print("ERROR: Cannot Harvest")
      quick_print("ERROR: Cannot Harvest")
      quick_print("ERROR: Cannot Harvest")
      quick_print("ERROR: Cannot Harvest")
      quick_print("ERROR: Cannot Harvest")


startPositions = []
x, y = 0, 0 
while x < max_drones():
  y = 0
  while y < max_drones():
    startPositions.append((x + 4, y + 8))
    y += 8
  x += 4

# startPositions = [(0,0), (4,0), (0, 8)]

gridDirections = [
  North,
  North,
  North,
  North,
  North,
  North,
  North,
  East,
  East,
  East,
  South,
  South,
  South,
  South,
  South,
  South,
  South,
  West,
  North,
  North,
  North,
  North,
  North,
  North,
  West,
  South,
  South,
  South,
  South,
  South,
  South,
  West,
]

directionsLen = len(gridDirections)

def _optDrone(startPos):
  utils.moveTo(startPos[0], startPos[1])
  for i in range(directionsLen):
    utils.plantSeed(Entities.Pumpkin)
    # use_item(Items.Water)
    move(gridDirections[i % directionsLen])
  
  # pumpkins = 0
  # while pumpkins < directionsLen:
  #   pumpkins = directionsLen
  #   for i in range(directionsLen):
  #     planted = get_entity_type()
  #     if planted == Entities.Dead_Pumpkin or (planted == Entities.Pumpkin and not can_harvest()):
  #       pumpkins -= 1
  #       utils.plantSeed(Entities.Pumpkin)
  #       if pumpkins >= directionsLen:
  #         break
  #     move(gridDirections[i % directionsLen])
  
  
  deads = []
  for i in range(directionsLen):
    planted = get_entity_type()
    if planted == Entities.Dead_Pumpkin or (planted == Entities.Pumpkin and not can_harvest()):
      deads.append(utils.getPos())
      utils.plantSeed(Entities.Pumpkin)
    move(gridDirections[i % directionsLen])
  
  newPumpkins = len(deads)
  while newPumpkins > 0:
    for pos in deads:
      if utils.getPos() != pos:
        utils.moveTo(pos[0], pos[1])
      planted = get_entity_type()
      if planted == Entities.Pumpkin and can_harvest():
        deads.remove(pos)
      else:
        utils.plantSeed(Entities.Pumpkin)
        if get_water() < 0.2:
          use_item(Items.Water)
    newPumpkins = len(deads)

def _startOpt():  
  utils.moveTo(0, 0)
  for i in range(max_drones()):
    droneId = drones.spawnDrone(drones.wrapper(_optDrone, startPositions[len(gridDirections) - i - 1]))
    if droneId == None:
      _optDrone(startPositions[len(gridDirections) - i - 1])
  # maybe useless
  drones.waitForAllDronesToFinish()
  
  if can_harvest():
    harvest()



def _exec():
  global maxDrones
  global width
  global height
  global runs
  global leaderboardMin

  clear()
  utils.moveTo(0, 0)

  startTime = get_time()
  partial = 0
  total = 0
  if leaderboardMin != None and leaderboardMin > 0:
    while total < leaderboardMin:
      partial = num_items(Items.Pumpkin)
      startTimePartial = get_time()
      start(Entities.Pumpkin, width, height, maxDrones, 1)
      endTimePartial = get_time()
      timeTakenPartial = endTimePartial - startTimePartial
      partial = num_items(Items.Pumpkin) - partial
      total += partial
      quick_print("  (partial) Harvested", partial, "pumpkins in", timeTakenPartial, "seconds. Avg:", partial / timeTakenPartial, "per second")
    endTime = get_time()
    timeTakenTotal = endTime - startTime
    quick_print("Harvested", total, "pumpkins in", timeTakenTotal, "seconds. Avg:", total / timeTakenTotal, "per second")
    if total > 0 and timeTakenTotal > 0:
      leaderboardTime = 200000000 / total * timeTakenTotal / 60
      quick_print("Full leaderboard run: around", leaderboardTime, "minutes")
  else:
    utils.reportStart(Items.Pumpkin, runs)
    start(Entities.Pumpkin, width, height, maxDrones, runs)
    utils.reportEnd()
  
  # drones.waitForAllDronesToFinish()


utils.reportStart(Items.Pumpkin, 1)
_startOpt()
# _exec()
utils.reportEnd()

# if __name__ == "__main__":
#   quick_print("### DISABLE FOR SIMULATION ###")

#   leaderboardMin = None
#   # leaderboardMin = 200000000
#   runs = 1
#   maxDrones = max_drones()
#   maxDrones = 32
#   width = get_world_size()
#   height = get_world_size()
  
  
  # _start = num_items(Items.Pumpkin)
  
    # drones.waitForAllDronesToFinish()
  #   utils.sleep(100)
  # quick_print("Harvested", _start, str(num_items(Items.Pumpkin) - _start))

  # clear()
  # harvest()