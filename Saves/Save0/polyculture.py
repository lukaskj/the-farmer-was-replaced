import utils
import drones
from globals import WORLD_SIZE


def _dronePolyculture(seed, startX, startY, width, height):
  crops = []
  utils.moveTo(startX, startY)
  for _ in range(3):
    curPos = utils.getPos()
    # nextX, nextY = utils.getNextSubgridPos(width, height, startX, startY)
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
      
      # utils.sleep(10)
    return __
  return run



def start(seed, w, h, maxDrones = None):
  drones.droneGrid(w, h, __testDrone(seed), maxDrones)

if __name__ == "__main__":
  utils.moveTo(0, 0)
  seed = Entities.Pumpkin
  runs = 5

  item = utils.seedToItem(seed)
  startAmount = num_items(item)
  startTime = get_time()
  for _ in range(runs):
    start(seed, WORLD_SIZE, WORLD_SIZE, max_drones())
    drones.waitForAllDronesToFinish()
  endTime = get_time()
  endAmount = num_items(item)

  quick_print("Harvested", endAmount - startAmount, "of", item, "from", seed, "in", endTime - startTime, "seconds and", runs, "runs")
