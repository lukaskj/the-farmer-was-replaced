import utils
from globals import WORLD_SIZE

shouldStart = False
varTest = {}

def _can_walk(direction, maxLen = WORLD_SIZE):
  x, y = utils.get_pos()
  if direction == West:
    return x > 0
  if direction == South:
    return y > 0
  if direction == East:
    return x < min(maxLen - 1, WORLD_SIZE - 1)
  if direction == North:
    return y < min(maxLen - 1, WORLD_SIZE - 1)

def spawn_drone_and_walk(direction, maxLen = WORLD_SIZE):

  def walk():
    canWalk = _can_walk(direction, maxLen)
    utils.sleep(1)
    while canWalk:
      utils.sleep(0.2)
      # quick_print("Can walk", direction, canWalk)
      move(direction)
      canWalk = _can_walk(direction, maxLen)
  return walk

def start(_maxSize, _maxDrones):
  droneList = []
  maxDrones = min(_maxDrones, max_drones())  # Fixed maximum number of drones
  maxSize = min(_maxSize, WORLD_SIZE)  # Ensure we don't exceed world size
  
  quick_print("Drones test ", str(maxSize), "Max drones:", maxDrones)
  for i in range(maxSize):
    utils.move_to(i,0)
    while True:
      numDrones = num_drones()
      if numDrones <= maxDrones:
        droneId = spawn_drone(spawn_drone_and_walk(North))
        if droneId != None:
          droneList.append(droneId)
          break
      else:
        quick_print("Start waiting for idle drones")
        utils.wait_for(_has_idle_drone(droneList, maxSize))
  
  utils.sleep(1)
  utils.move_to(0,0)

def _has_idle_drone(droneList, maxSize):
  def fnc():
    tmpDroneList = droneList[:]    
    hasIdleDrone = False
    for drone in tmpDroneList:
      if has_finished(drone):
        hasIdleDrone = True
        droneList.remove(drone)
    return hasIdleDrone
  return fnc



if __name__ == "__main__":
  utils.move_to(0, 0)
  start(16, 1000)