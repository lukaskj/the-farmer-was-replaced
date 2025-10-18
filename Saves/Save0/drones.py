import utils

_drones = []
def spawnDrone(fnc):
  droneId = spawn_drone(fnc)
  if droneId != None:
    _drones.append(droneId)
  return droneId

def spawnDroneInGrid(fnc, width, height, maxDrones = None):
  if maxDrones == None:
    maxDrones = max_drones()
  maxDrones = min(maxDrones, min(width, height))

  grids = utils.calculateSubgrids(width, height, maxDrones)
  i = 0
  droneToCoords = {}
  for coords in grids:
    i += 1
    x, y, width, height = coords
    utils.moveTo(x, y)
    droneId = spawnDrone(fnc(coords))
    executeLastAsMainDrone = droneId == None and i == len(grids)
    if executeLastAsMainDrone:
      quick_print("WARNING: Execute the last grid as main drone")
      # fnc(coords)()
    else:
      droneToCoords[droneId] = coords
  return droneToCoords, executeLastAsMainDrone

def wrapper(fnc, arg1=None, arg2=None, arg3=None, arg4=None, arg5=None, arg6=None):
  def __():
    if arg1==None:
      return fnc()
    if arg2==None:
      return fnc(arg1)
    if arg3==None:
      return fnc(arg1, arg2)
    if arg4==None:
      return fnc(arg1, arg2, arg3)
    if arg5==None:
      return fnc(arg1, arg2, arg3, arg4)
    if arg6==None:
      return fnc(arg1, arg2, arg3, arg4, arg5)
  return __

def waitForIdleDrone(maxDrones = None):
  global _drones
  if maxDrones == None:
    maxDrones = max_drones()
  def fnc():
    if maxDrones > len(_drones):
      return True
    hasIdle = False
    for drone in _drones:
      if has_finished(drone):
        _drones.remove(drone)
        hasIdle = True
    return hasIdle
  utils.waitFor(fnc)

# Check if any drone is idle and returns it's ID if so
def waitForIdleDroneAndReturnId(maxDrones = None):
  global _drones
  if len(_drones) == 0:
    return False
  def fnc():
    for drone in _drones:
      if has_finished(drone):
        _drones.remove(drone)
        return drone
    return False
  return utils.waitFor(fnc, 0.01)

def waitForAllDronesToFinish():
  global _drones
  def fnc():
    totalFinished = 0
    for drone in _drones:
      if has_finished(drone):
        totalFinished += 1
    return len(_drones) == totalFinished

  utils.waitFor(fnc, 0.01)
  _drones = []