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

def droneGrid(width, height, fnc, maxDrones = None):
  if maxDrones == None:
    maxDrones = max_drones() - 1
  maxDrones = min(maxDrones, min(width, height))
  grids = utils.calculateSubgrids(width, height, maxDrones)
  for coords in grids:
    x, y, width, height = coords
    utils.moveTo(x, y)
    spawnDrone(fnc(coords))

  # def __spawnAndExecute(fnc):
  # return __spawnAndExecute