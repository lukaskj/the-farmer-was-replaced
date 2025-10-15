from globals import WORLD_SIZE
import utils

def start(seed, w, h, runs = 1, maxDrones = None):
  if maxDrones == None:
    maxDrones = max_drones() - 1
  grids = utils.calculateSubgrids(w, h, maxDrones)
  
  for coords in grids:
    x, y, width, height = coords
    utils.moveTo(x, y)
    
    utils.spawnDrone(_spawn_drone(seed, x, y, width, height, runs))

def _spawn_drone(seed, startX, startY, width, height, runs = 1):
  def run():
    for _ in range(runs):
      _loop_grid(seed, startX, startY, width, height)
  return run

def _loop_grid(seed, startX, startY, width, height):
  utils.moveTo(startX, startY)
  notHarvested = []
  
  for _ in range(width * height):
    nextX, nextY = utils.getNextSubgridPos(width, height, startX, startY)
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
    if seed == Entities.Sunflower and utils.canUseWater(width * height):
      use_item(Items.Water)
      

    utils.moveTo(nextX, nextY)

  harvestedTotal = 0
  toHarvestTotal = width * height
  utils.moveTo(startX, startY)
  for _ in range(toHarvestTotal):
    nextX, nextY = utils.getNextSubgridPos(width, height, startX, startY)
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
      if can_harvest() or get_entity_type() == None:
        harvest()
        harvestedTotal += 1
        notHarvested.remove(pos)
    if len(notHarvested) > 0:
      utils.sleep(0.1)
    
  

if __name__ == "__main__":
  clear()
  seed = Entities.Bush
  utils.moveTo(0, 0)
  runs = 10
  
  start(seed, WORLD_SIZE, WORLD_SIZE, runs, None)
  # utils.waitForAllDronesToFinish()