import utils
import drones
# from globals import WORLD_SIZE

totalGrown = 0
addFertilizer = False

def _droneCode(seed, startX, startY, width, height):
  utils.moveTo(startX, startY)
  plots = width * height
  visited = 0
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
  seed = Entities.Pumpkin
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
  if leaderboardMin > 0:
    while total < leaderboardMin:
      partial = num_items(Items.Pumpkin)
      startTimePartial = get_time()
      start(Entities.Pumpkin, width, height, maxDrones, 1)
      endTimePartial = get_time()
      timeTakenPartial = endTimePartial - startTimePartial
      partial = num_items(Items.Pumpkin) - partial
      total += partial
      quick_print("  (partial) Harvested", partial, "pumpkins in", timeTakenPartial, "seconds. Avg:", partial / timeTakenPartial, "per second")
  else:
    start(Entities.Pumpkin, width, height, maxDrones, runs)
  
  endTime = get_time()
  timeTakenTotal = endTime - startTime
  # drones.waitForAllDronesToFinish()
  quick_print("Harvested", total, "pumpkins in", timeTakenTotal, "seconds. Avg:", total / timeTakenTotal, "per second")

  leaderboardTime = 200000000 / total * timeTakenTotal / 60
  quick_print("Full leaderboard run: around", leaderboardTime, "minutes")

if __name__ == "__main__":
  quick_print("### DISABLE FOR SIMULATION ###")

  leaderboardMin = 20000000
  # leaderboardMin = 200000000
  runs = 1
  maxDrones = max_drones()
  maxDrones = 32
  width = get_world_size()
  height = get_world_size()

  _exec()
  # _start = num_items(Items.Pumpkin)
  
    # drones.waitForAllDronesToFinish()
  #   utils.sleep(100)
  # quick_print("Harvested", _start, str(num_items(Items.Pumpkin) - _start))

  # clear()
  # harvest()