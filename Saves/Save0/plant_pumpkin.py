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


def __spawnDrone(seed):
  def _start(grid):
    startX, startY, width, height = grid
    def __():
      _droneCode(seed, startX, startY, width, height)
    return __
  return _start

def start(seed, w, h, maxDrones = None, runs = 1):
  seed = Entities.Pumpkin
  for _ in range(runs):
    drones.droneGrid(w, h, __spawnDrone(seed), maxDrones)
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

  clear()
  utils.moveTo(0, 0)

  startTime = get_time()
  _start = num_items(Items.Pumpkin)
  start(Entities.Pumpkin, width, height, maxDrones, runs)
  drones.waitForAllDronesToFinish()
  quick_print("Harvested", str(num_items(Items.Pumpkin) - _start), "pumpkins in", get_time() - startTime, "seconds")
    

if __name__ == "__main__":
  quick_print("### DISABLE FOR SIMULATION ###")
  runs = 1
  maxDrones = max_drones()
  width = get_world_size()
  height = get_world_size()

  _exec()
  # _start = num_items(Items.Pumpkin)
  
    # drones.waitForAllDronesToFinish()
  #   utils.sleep(100)
  # quick_print("Harvested", _start, str(num_items(Items.Pumpkin) - _start))

  # clear()
  # harvest()