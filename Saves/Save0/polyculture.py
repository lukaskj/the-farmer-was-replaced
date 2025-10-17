import utils
import drones
from globals import WORLD_SIZE

def _dronePolyculture(seed, startX, startY, width, height):
  crops = []
  utils.moveTo(startX, startY)
  for _ in range(3):
    # continue
    curPos = utils.getPos()
    # nextX, nextY = utils.getNextSubgridPos(startX, startY, width, height)
    nextX, nextY = curPos

    utils.plantSeed(seed)
    if utils.canUseWater(1):
      use_item(Items.Water)

    companion = get_companion()
    if companion != None:
      crops.append((curPos, companion[0], companion[1]))
    utils.moveTo(nextX + 1, nextY + 1)
  
  for companion in crops:
    (sourceX, sourceY), companionSeed, (companionX, companionY) = companion
    utils.moveTo(companionX, companionY)

    groundCrop = get_entity_type()
    if groundCrop != seed:
      if can_harvest():
        harvest()
      else:
        till()
      utils.plantSeed(companionSeed)
    
    utils.moveTo(sourceX, sourceY)    
    if not can_harvest() and get_entity_type() != None:
      utils.waitFor(can_harvest)    
    harvest()

def __testDrone(seed):
  def run(gridData):
    startX, startY, width, height = gridData
    def __():
      _dronePolyculture(seed, startX, startY, width, height)
    return __
  return run

def start(seed, w, h, maxDrones = None):
  drones.droneGrid(w, h, __testDrone(seed), maxDrones)
  drones.waitForAllDronesToFinish()

def _exec():
  global seed
  global maxDrones
  global width
  global height
  global runs

  clear()
  utils.moveTo(0, 0)

  item = utils.seedToItem(seed)
  startAmount = num_items(item)
  startTime = get_time()

  for _ in range(runs):
    start(seed, width, height, maxDrones)
  
  endTime = get_time()
  endAmount = num_items(item)
  quick_print("Harvested", endAmount - startAmount, "of", item, "from", seed, "in", endTime - startTime, "seconds and", runs, "runs")
    

if __name__ == "__main__":
  # quick_print("### DISABLE FOR SIMULATION ###")
  # seed = Entities.Grass
  # runs = 1
  # maxDrones = max_drones()
  # width = get_world_size()
  # height = get_world_size()

  _exec()


