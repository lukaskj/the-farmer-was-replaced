import utils
import drones
from globals import ORIENTATION_LEFTRIGHT, ORIENTATION_UPDOWN

def _sort_line_two_way(startPos, maxLen, orientation = ORIENTATION_LEFTRIGHT):
  _min = startPos
  _max = min(_min + maxLen, get_world_size())

  increasingDirection = East
  decreasingDirection = West
  if orientation == ORIENTATION_UPDOWN:
    increasingDirection = North
    decreasingDirection = South

  direction = increasingDirection

  while _min < _max:
    swappedForward = False
    swappedBackward = False

    # Forward pass - move in increasing direction
    for _ in range(_max - _min):
      measureSelf = measure()
      measureNext = measure(direction)

      if measureSelf != None and measureNext != None and measureSelf > measureNext:
        swap(direction)
        swappedForward = True

      # Check if we've reached max boundary
      if orientation == ORIENTATION_LEFTRIGHT:
        pos = get_pos_x()
      else:
        pos = get_pos_y()
      
      if pos >= _max - 2:
        break

      move(direction)

    # Update boundary and change direction
    _max -= 1
    direction = decreasingDirection

    # Early exit if sorted
    if not swappedForward:
      break

    # Backward pass - move in decreasing direction
    for _ in range(_max - _min):
      measureSelf = measure()
      measureNext = measure(direction)

      if measureSelf != None and measureNext != None and measureSelf < measureNext:
        swap(direction)
        swappedBackward = True

      # Check if we've reached min boundary
      if orientation == ORIENTATION_LEFTRIGHT:
        pos = get_pos_x()
      else:
        pos = get_pos_y()
      
      if pos <= _min + 1:
        break

      move(direction)

    # Update boundary and change direction
    _min += 1
    direction = increasingDirection

    # Early exit if sorted
    if not swappedBackward:
      break

def dronePlant(startX, startY, length):
  utils.moveTo(startX, startY)
  for y in range(length):
    if startY + y != startY:
      utils.moveTo(startX, startY + y)
    utils.plantSeed(Entities.Cactus)
    measureSelf = measure()
    measureSouth = measure(South)

    if measureSouth != None and measureSelf != None and measureSouth > measureSelf:
      swap(South)
  utils.moveTo(startX, startY)
  _sort_line_two_way(startY, length, ORIENTATION_UPDOWN)


def sortRows(startX, startY, length):
  utils.moveTo(startX, startY)
  _sort_line_two_way(startX, length, ORIENTATION_LEFTRIGHT)


def spawnDrone(startX, startY, w, h):
  droneId = None
  for x in range(w):
    droneId = drones.spawnDrone(drones.wrapper(dronePlant, startX + x, startY, h))
  if droneId == None and num_drones() == w:
    dronePlant(w - 1, startY, h)
  drones.waitForAllDronesToFinish()

  # Sort rows
  for y in range(h):
    droneId = drones.spawnDrone(drones.wrapper(sortRows, startX, startY + y, w))
  if droneId == None and num_drones() == max_drones():
    sortRows(startX, startY + h - 1, w)
  utils.moveTo(startX, startY)
  drones.waitForAllDronesToFinish()
  harvest()


def main():
  w = get_world_size()
  h = get_world_size()

  utils.moveTo(0, 0)
  startItems = num_items(Items.Cactus)
  startTime = get_time()

  spawnDrone(0, 0, w, h)

  endTime = get_time()
  endItems = num_items(Items.Cactus)

  totalHarvested = endItems - startItems
  totalTime = endTime - startTime

  quick_print("Harvested", totalHarvested, "in", totalTime, "seconds. Avg:", totalHarvested / totalTime, "per second")

  
  # utils.moveTo(0, 4)

if __name__ == "__main__":
  clear()
  # set_execution_speed(2)
  # set_world_size(5)
  main()