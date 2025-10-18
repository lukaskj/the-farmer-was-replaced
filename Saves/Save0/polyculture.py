import utils
import drones

def _dronePolyculture(seed, startX, startY, width, height, plotsPerDrone):
  crops = []
  sources = []  

  middleX = utils.round((startX + ((width - 1) / 2)))
  middleY = utils.round((startY + ((height - 1) / 2)))
  
  utils.moveTo(middleX, middleY)  
  for i in range(plotsPerDrone):
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

def __newDrone(seed, plotsPerDrone = 5, runs = 1):
  def __init(gridData):
    startX, startY, width, height = gridData
    def __():
      for _ in range(runs):
        _dronePolyculture(seed, startX, startY, width, height, plotsPerDrone)
    return __
  return __init

def start(seed, w, h, runs = 1, maxDrones = None, plotsPerDrone = 5):
  shouldExecuteLastAsMainDrone, lastGrid, _ = drones.spawnDronesInGrid(__newDrone(seed, plotsPerDrone, runs), w, h, maxDrones)
  if shouldExecuteLastAsMainDrone:
    __newDrone(seed, plotsPerDrone, runs)(lastGrid)()

  

def _exec():
  global seed
  global maxDrones
  global width
  global height
  global runs
  global plotsPerDrone

  clear()
  utils.moveTo(0, 0)

  item = utils.seedToItem(seed)
  startAmount = num_items(item)
  startTime = get_time()

  start(seed, width, height, runs, maxDrones, plotsPerDrone)
  drones.waitForAllDronesToFinish()
  
  endTime = get_time()
  endAmount = num_items(item)

  totalTime = endTime - startTime
  totalAmount = endAmount - startAmount

  utils.printReport(totalAmount, totalTime, item, runs)
  quick_print("---")
  quick_print("Harvested", totalAmount, "of", item, "from", seed, "in", totalTime, "seconds and", runs, "runs")
  
  # quick_print('"' + str(item)  + '"|"' + str(maxDrones)  + '"|"' + str(plotsPerDrone)  + '"|"' + str(totalAmount)  + '"|"' + str(totalTime)+ '"|"' + str(totalAmount / totalTime) + '"')

def execAndReportMultiple():
  global seed
  global maxDrones
  global width
  global height
  global runs
  global plotsPerDrone

  width = get_world_size()
  height = get_world_size()
  runs = 20
  plotsPerDrone = 1
  seedss = [Entities.Grass, Entities.Bush, Entities.Tree, Entities.Carrot]
  for seeeed in seedss:
    seed = seeeed
    for plots in range(5):
      plotsPerDrone = plots + 1
      for d in range(32):
        maxDrones = min(d + 1, max_drones())
        _exec()

if __name__ == "__main__":
  quick_print("### DISABLE FOR SIMULATION ###")
  seed = Entities.Carrot
  maxDrones = 32
  plotsPerDrone = 5

  runs = 100
  # maxDrones = utils.round((max_drones() / 2))
  # maxDrones = max_drones()
  width = get_world_size()
  height = get_world_size()
  # set_execution_speed(1)

  _exec()


