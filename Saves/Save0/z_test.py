import utils
import drones
#till()
# set_execution_speed(0.7)
# Test each drone spawn location with till

def fncWithArgs(arg1, arg2):
  quick_print("Fnc with args", arg1, arg2)
  pass

def _droneCode(gridCoords):
  startX, startY, width, height = gridCoords
  utils.moveTo(startX, startY)

  for _ in range(width * height):
    utils.plantSeed(Entities.Cactus)
    utils.moveToNextSubgridPos(startX, startY, width, height)

def Drone():
  def __init(gridCoords):
    def __():
      _droneCode(gridCoords)
    return __
  return __init

def getRowValues(startY):
  def _():
    row = []
    utils.moveTo(0, startY)
    for i in range(get_world_size()):
      row.append(measure())
      move(East)
    quick_print(row, ",")
  return _


  # get grid
def _getGrid():
  
  def init(gridCoords):
    def _():
      startX, startY, width, height = gridCoords
      
    return _
  return init

def sortAllRows(grid):
  pass

def sortAllCols(grid):
  pass

def sort(grid):
  changesMade = True
  iterations = 0
  maxIterations = get_world_size() * get_world_size() * 10 # Safety

  while (changesMade and iterations < maxIterations):
    changesMade = False

    if sortAllRows(grid):
      changesMade = True

    if sortAllCols(grid):
      changesMade = True
    
    iterations += 1
  if iterations >= maxIterations:
    quick_print("[WARN] Maximum iterations reached. Grid may not be fully sorted.")

  return grid

def printGrid(grid):
  wSize = get_world_size()
  for y in range(wSize):
    row = []
    for x in range(wSize):
      row.append(grid[(x, wSize - y - 1)])
    quick_print(row)

def exec():
  clear()
  wSize = get_world_size()
  droneController = Drone()

  shouldExecuteAsMainDrone, lastGrid, droneMap = drones.spawnDronesInGrid(droneController, wSize, wSize, max_drones())  
  if shouldExecuteAsMainDrone:
    droneController(lastGrid)()  
  utils.moveTo(0,0)

  drones.waitForAllDronesToFinish()
  
  # set_execution_speed(3)
  
  grid = {}
  y = 0
  _rowDebug = []
  _rowDebug2 = []
  while True:
    utils.moveTo(0,y)
    for _ in range(wSize):
      curX, curY = utils.getPos()
      measureUp = measure(North)
      measureDown = measure(South)
      measureSelf = measure()

      grid[(curX, curY)] = measureSelf
      if curY == 0:
        _rowDebug.append(measureSelf)
      if curY == wSize - 1:
        _rowDebug2.append(measureSelf)
      if measureDown != None and (curY - 1) >= 0:
        grid[(curX, (curY - 1))] = measureDown
      if measureUp != None and (curY + 1) < wSize:
        grid[(curX, (curY + 1))] = measureUp

      move(East)
    y += 3
    if y >= wSize:
      break

  printGrid(grid)
  quick_print("end")


if __name__ == "__main__":
  set_world_size(10)
  exec()
  # startTicks = get_tick_count()
  
  # drones.spawnDrone(drones.wrapper(fncWithArgs, 1, 2))
  # # utils.sleep(1)
  # endTicks = get_tick_count()

  # quick_print("Ticks spent", endTicks - startTicks)