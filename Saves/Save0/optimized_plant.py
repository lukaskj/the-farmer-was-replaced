import utils
import drones

def start(seed, w, h, runs = 1, maxDrones = None):
  drones.spawnDronesInGrid(__newDrone(seed, runs), w, h, maxDrones)

def __newDrone(seed, runs = 1):
  def __init(coords):
    startX, startY, width, height = coords
    def __():
      for _ in range(runs):
        _loop_grid(seed, startX, startY, width, height)
    return __
  return __init

def _loop_grid(seed, startX, startY, width, height):
  utils.moveTo(startX, startY)
  notHarvested = []
  
  for _ in range(width * height):
    nextX, nextY = utils.getNextSubgridPos(startX, startY, width, height)
    if can_harvest():
      harvest()
    if seed == Entities.Bush:
      curX, curY = utils.getPos()
      if (curX + curY) % 2 == 0:
        utils.plantSeed(Entities.Tree)
      else:
        utils.plantSeed(seed)
    else:      
      utils.plantSeed(seed)
    if (seed == Entities.Sunflower or seed == Entities.Bush or seed == Entities.Tree) and utils.canUseWater(width * height):
      use_item(Items.Water)
    utils.moveTo(nextX, nextY)

  harvestedTotal = 0
  toHarvestTotal = width * height
  utils.moveTo(startX, startY)
  for _ in range(toHarvestTotal):
    nextX, nextY = utils.getNextSubgridPos(startX, startY, width, height)
    crop = get_entity_type()
    if can_harvest():
      harvest()
      harvestedTotal += 1
    elif crop != None:
      notHarvested.append(utils.getPos())

    utils.moveTo(nextX, nextY)
  
  while harvestedTotal < toHarvestTotal and len(notHarvested) > 0:
    for pos in notHarvested:
      utils.moveTo(pos[0], pos[1])
      plotUnderDrone = get_entity_type()
      if can_harvest() or plotUnderDrone == None or plotUnderDrone == Entities.Dead_Pumpkin:
        harvest()
        harvestedTotal += 1
        notHarvested.remove(pos)
    if len(notHarvested) > 0:
      utils.sleep(0.1)
    
  
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

  start(seed, width, height, runs, None)  
  drones.waitForAllDronesToFinish()

  endAmount = num_items(item)
  quick_print("Harvested", endAmount - startAmount, "of", item)

if __name__ == "__main__":
  quick_print("### DISABLE FOR SIMULATION ###")
  seed = Entities.Sunflower
  runs = 1500
  maxDrones = max_drones()
  width = get_world_size()
  height = get_world_size()

  _exec()