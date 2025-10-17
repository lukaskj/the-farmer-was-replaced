import utils
import drones

# [
#   [0,0,8,8],
#   [8,0,8,8],
#   [16,0,8,8],
#   [24,0,8,8],
#   [0,8,8,8],
#   [8,8,8,8],
#   [16,8,8,8],
#   [24,8,8,8],
#   [0,16,8,8],
#   [8,16,8,8],
#   [16,16,8,8],
#   [24,16,8,8],
#   [0,24,8,8],
#   [8,24,8,8],
#   [16,24,8,8],
#   [24,24,8,8]
# ]
def _dronePolyculture(seed, startX, startY, width, height):
  crops = []
  sources = []

  middleX = (startX + ((width - 1) / 2)) // 1
  middleY = (startY + ((height - 1) / 2)) // 1
  
  utils.moveTo(middleX, middleY)  
  for i in range(5):
    curPos = utils.getPos()
    sources.append(curPos)

    _maxInsideGridIteration = 10
    
    foundCompanionInGrid = False
    for i in range(_maxInsideGridIteration):
      utils.plantSeed(seed)
      if utils.canUseWater(1):
        use_item(Items.Water)
      companion = get_companion()
      if companion != None:
        companionSeed, companionPos = companion
        if companionPos in sources or not utils.isInsideSubgrid(companionPos[0], companionPos[1], startX, startY, width, height):
          continue
        
        foundCompanionInGrid = True        
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
  runs = 1500
  maxDrones = (max_drones() / 2) // 1
  width = get_world_size()
  height = get_world_size()

  _exec()


