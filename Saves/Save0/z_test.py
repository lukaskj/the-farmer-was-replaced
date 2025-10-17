import utils
import drones
#till()
clear()

# Test each drone spawn location with till

def _droneCode(startX, startY, width, height):
  utils.moveTo(startX, startY)
  utils.plantSeed(Entities.Bush)
  utils.moveTo(startX + width - 1, startY + height - 1)  
  utils.plantSeed(Entities.Carrot)

def __newDrone():
  def __init(grid):
    startX, startY, width, height = grid
    def __():
      _droneCode(startX, startY, width, height)
    return __
  return __init

def exec():
  drones.spawnDroneInGrid(__newDrone(), get_world_size(), get_world_size(), max_drones())

if __name__ == "__main__":
  clear()
  exec()

  # gridX, gridY, width, height = 3, 3, 3, 3
  # x, y = 3, 3
  
  # utils.moveTo(gridX, gridY)
  # for i in range(width * height):
  #   curX, curY = utils.getPos()
  #   quick_print({
  #     "curY": curY, "gridY + height": gridY + height - 1, "curY - gridY": curY - gridY
  #   })
  #   if (curX - gridX == 0) or (curY - gridY == 0) or (curX == (gridX + width - 1)) or (curY == (gridY + height - 1)):
  #     till()
  #   # utils.sleep(1)
  #   nextX, nextY = utils.getNextSubgridPos(gridX, gridY, width, height)
  #   utils.moveTo(nextX, nextY)
  
  # utils.moveTo(x, y)
  # utils.plantSeed(Entities.Cactus)
  # print(utils.isInsideSubgrid(x, y, gridX, gridY, width, height))

  # sim_items = {Items.Carrot : 10000, Items.Hay : 50}
  # sim_globals = {"a" : 13}
  # seed = 0
  # speed = 64
  # simulate("polyculture", Unlocks, sim_items, sim_globals, seed, speed)
  # utils.moveTo(0, 0)

  # totalTwoWayTime = 0
  # totalBubbleTime = 0

  # totalTwoWayEnergy = 0
  # totalBubbleEnergy = 0
  # for _ in range(1):
  #   clear()
  #   twoWayTime, twoWayEnergy = testTwoUpDown()
  #   totalTwoWayTime += twoWayTime
  #   totalTwoWayEnergy += twoWayEnergy

  #   # bubbleTime, bubbleEnergy = testBubble()
  #   # totalBubbleTime += bubbleTime
  #   # totalBubbleEnergy += bubbleEnergy

  #   quick_print("----------------------------")
  
  # quick_print("----------------------------")
  # quick_print(" * Two Way sort total time:", totalTwoWayTime, "seconds. Energy spent total: ", totalTwoWayEnergy)
  # quick_print(" * Bubble sort total time:", totalBubbleTime, "seconds. Energy spent total: ", totalBubbleEnergy)