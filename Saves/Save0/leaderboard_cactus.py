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

  while _min < _max - 1:
    lastSwapPosForward = _min
    lastSwapPosBackward = _max

    # Forward pass - move in increasing direction
    # Get current position
    if orientation == ORIENTATION_LEFTRIGHT:
      pos = get_pos_x()
    else:
      pos = get_pos_y()
    
    while pos < _max - 1:
      measureSelf = measure()
      measureNext = measure(direction)

      if measureSelf != None and measureNext != None and measureSelf > measureNext:
        swap(direction)
        lastSwapPosForward = pos

      move(direction)
      
      # Update position
      if orientation == ORIENTATION_LEFTRIGHT:
        pos = get_pos_x()
      else:
        pos = get_pos_y()

    # Update boundary to last swap position (elements after are already sorted)
    new_max = lastSwapPosForward + 1
    direction = decreasingDirection

    # Early exit if sorted (no swaps made)
    if new_max <= _min:
      break
    
    _max = new_max

    # Backward pass - move in decreasing direction
    # Get current position
    if orientation == ORIENTATION_LEFTRIGHT:
      pos = get_pos_x()
    else:
      pos = get_pos_y()
    
    while pos > _min:
      measureSelf = measure()
      measureNext = measure(direction)

      if measureSelf != None and measureNext != None and measureSelf < measureNext:
        swap(direction)
        lastSwapPosBackward = pos

      move(direction)
      
      # Update position
      if orientation == ORIENTATION_LEFTRIGHT:
        pos = get_pos_x()
      else:
        pos = get_pos_y()

    # Update boundary to last swap position (elements before are already sorted)
    new_min = lastSwapPosBackward - 1
    direction = increasingDirection

    # Early exit if sorted (no swaps made)
    if new_min >= _max:
      break
    
    _min = new_min

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
  # w, h = 22,22
  leaderboardMin = 33554432

  utils.moveTo(0, 0)
  
  startItems = num_items(Items.Cactus)
  startTime = get_time()
  totalHarvested = 0
  totalRuns = 0

  while totalHarvested < leaderboardMin:
    totalRuns += 1
    startItems = num_items(Items.Cactus)
    spawnDrone(0, 0, w, h)
    partial = num_items(Items.Cactus) - startItems
    totalHarvested += partial

  endTime = get_time()

  # totalHarvested = endItems - startItems
  totalTime = endTime - startTime

  quick_print("--")
  quick_print("Runs: " + str(totalRuns))
  quick_print("Harvested", totalHarvested, "in", totalTime, "seconds.")
  quick_print("Avg:", totalHarvested / totalTime, "per second")
  quick_print("Avg per run:", totalHarvested / totalRuns)

  
  # utils.moveTo(0, 4)

if __name__ == "__main__":
  clear()
  # set_execution_speed(2)
  # set_world_size(5)
  main()