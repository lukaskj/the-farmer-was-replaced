import utils
import drones
#till()
# set_execution_speed(0.7)
# Test each drone spawn location with till

def fncWithArgs(arg1, arg2):
  quick_print("Fnc with args", arg1, arg2)
  pass
  # while True:
  #   utils.sleep(1)

def _droneCode(startX, startY, width, height, shared):
  firstDrone = startX == 0 and startY == 0
  # if firstDrone:
  #   change_hat(Hats.Wizard_Hat)
  utils.sleep(5)
  quick_print("Drone code started", shared)
  while True:
    quick_print(shared)
    utils.sleep(0.2)  

def __newDrone():
  shared = {
    "data": False
  }
  def __init(grid, mainDrone = False):
    startX, startY, width, height = grid
    def __():
      quick_print("Started", shared)
      _droneCode(startX, startY, width, height, shared)
      if mainDrone:
        shared["data"] = True
    return __
  return __init

def exec():
  dddd = __newDrone()
  drones.spawnDroneInGrid(dddd, get_world_size(), get_world_size(), 2)
  quick_print("Starting main drone")
  dddd((0, 5, 1, 1), True)

if __name__ == "__main__":
  startTicks = get_tick_count()
  
  drones.spawnDrone(drones.wrapper(fncWithArgs, 1, 2))
  # utils.sleep(1)
  endTicks = get_tick_count()

  quick_print("Ticks spent", endTicks - startTicks)