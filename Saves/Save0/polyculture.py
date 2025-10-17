import utils
import drones

def _dronePolyculture(seed, startX, startY, width, height):
  isFirstDrone = startX == 0 and startY == 0
  crops = []
  sources = []  

  middleX = (startX + ((width - 1) / 2)) // 1
  middleY = (startY + ((height - 1) / 2)) // 1
  
  utils.moveTo(middleX, middleY)  
  for i in range(5):
    curPos = utils.getPos()
    sources.append(curPos)

    _maxInsideGridIteration = 10
    for _ in range(_maxInsideGridIteration):
      utils.plantSeed(seed)
      if utils.canUseWater(1):
        use_item(Items.Water)
      companion = get_companion()
      if companion != None:
        companionSeed, companionPos = companion
        if companionPos in sources:
          continue
        if not utils.isInsideSubgrid(companionPos[0], companionPos[1], startX, startY, width, height):
          continue
        crops.append((curPos, companionSeed, companionPos))
        break
    
    # if utils.isInsideSubgrid(curX + i, curY + i, startX, startY, width, height):
    #   utils.moveTo(curX + 1, curY + 1)
    utils.moveToNextSubgridPos(startX, startY, width, height)
  
  # Plant all companions
  for companion in crops:
    (sourceX, sourceY), companionSeed, (companionX, companionY) = companion

    utils.moveTo(companionX, companionY)

    groundCrop = get_entity_type()
    if groundCrop != companionSeed:
      if can_harvest():
        harvest()
      utils.plantSeed(companionSeed, True)
  
  # Harvest all sources
  for source in sources:
    (sourceX, sourceY) = source
    
    utils.moveTo(sourceX, sourceY)
    if not can_harvest() and get_entity_type() != None:
      utils.waitFor(can_harvest)
    harvest()

def __newDrone(seed, runs = 1):
  def __init(gridData):
    startX, startY, width, height = gridData
    def __():
      for _ in range(runs):
        _dronePolyculture(seed, startX, startY, width, height)
    return __
  return __init

def start(seed, w, h, runs = 1, maxDrones = None):
  drones.spawnDroneInGrid(__newDrone(seed, runs), w, h, maxDrones)
  

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

  start(seed, width, height, runs, maxDrones)
  drones.waitForAllDronesToFinish()
  
  endTime = get_time()
  endAmount = num_items(item)
  quick_print("Harvested", endAmount - startAmount, "of", item, "from", seed, "in", endTime - startTime, "seconds and", runs, "runs")
    

if __name__ == "__main__":
  quick_print("### DISABLE FOR SIMULATION ###")
  seed = Entities.Carrot
  runs = 1000
  maxDrones = (max_drones() / 2) // 1
  width = get_world_size()
  height = get_world_size()
  # set_execution_speed(1)

  _exec()


