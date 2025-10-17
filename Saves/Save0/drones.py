import utils

_drones = []
def spawnDrone(fnc):
  droneId = spawn_drone(fnc)
  if droneId != None:
    _drones.append(droneId)
  return droneId

def waitForIdleDrone(maxDrones = None):
  global _drones
  if maxDrones == None:
    maxDrones = max_drones()
  def fnc():
    if maxDrones > len(_drones):
      return True
    for drone in _drones:
      if has_finished(drone):
        return True
    return False

  utils.waitFor(fnc)

def waitForAllDronesToFinish():
  global _drones
  def fnc():
    totalFinished = 0
    for drone in _drones:
      if has_finished(drone):
        totalFinished += 1
    return len(_drones) == totalFinished

  utils.waitFor(fnc)
  _drones = []

def spawnDroneInGrid(fnc, width, height, maxDrones = None):
  if maxDrones == None:
    maxDrones = max_drones()
  maxDrones = min(maxDrones, min(width, height))
  grids = utils.calculateSubgrids(width, height, maxDrones)
  quick_print("grids", len(grids), "maxDrones", maxDrones, grids)
  i = 0
  
  for coords in grids:
    i += 1
    x, y, width, height = coords
    utils.moveTo(x, y)
    droneId = spawnDrone(fnc(coords))
    if droneId == None and i == len(grids):
      fnc(coords)()
      quick_print("DEBUG: Executing the last grid as main drone")

  # def __spawnAndExecute(fnc):
  # return __spawnAndExecute