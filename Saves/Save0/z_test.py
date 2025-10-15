import utils
#till()
clear()

ORIENTATION_UPDOWN = 1
ORIENTATION_LEFTRIGHT = 2

def setup(startX, startY, maxX, maxY, orientation):
  utils.moveTo(startX, startY)

  _max = maxX
  direction = East
  if orientation == ORIENTATION_UPDOWN:
    _max = maxY
    direction = North
  

  for _ in range(_max):
    utils.plantSeed(Entities.Cactus)
    move(direction)
  utils.moveTo(startX, startY)


def _sort_line_two_way(startPos, maxLen, orientation = ORIENTATION_LEFTRIGHT):
  _min = startPos
  _max = maxLen

  increasingDirection = East
  decreasingDirection = West
  if orientation == ORIENTATION_UPDOWN:
    increasingDirection = North
    decreasingDirection = South
  
  direction = increasingDirection

  while _min < _max:
    swappedMin = False
    swappedMax = False
    for _ in range(_max - _min):
      measureSelf = measure()
      measureNext = measure(direction)
      
      if orientation == ORIENTATION_LEFTRIGHT:
        pos = get_pos_x()
      else:
        pos = get_pos_y()
      
      if (direction == increasingDirection and pos >= _max - 1) or (direction == decreasingDirection and pos <= _min - 1):
        continue
      
      # quick_print("Orientation", orientation, "direction", direction, "measureSelf", measureSelf, "measureNext", measureNext, "pos", pos)
      if direction == increasingDirection and measureSelf > measureNext:
        swap(direction)
        swappedMax = True
      elif direction == decreasingDirection and measureSelf < measureNext:
        swap(direction)
        swappedMin = True
      move(direction)
    
    # Exit if it's already sorted
    if not swappedMax and not swappedMin:
      break

    # Decrease boundaries once reaching them
    if direction == increasingDirection:
      _max -= 1
      direction = decreasingDirection
    else:
      _min += 1
      direction = increasingDirection

def _sort_bubble(maxX, maxY, startX, startY):
  for x in range(maxY):
    n = maxX
    swapped = True
    while swapped:
      swapped = False
      utils.moveTo(startX, startY)
      for y in range(n - 1):
        if not _is_next_cactus_bigger(East):
          swap(East)
          swapped = True
        move(East)
      n -= 1
      if not swapped:
        break

def _is_next_cactus_bigger(direction):
  selfSize = measure()
  nextSize = measure(direction)
  if nextSize != None and selfSize <= nextSize:
    return True
  return False 



def testTwoWay():
  startX = 0
  startY = 1
  maxX = get_world_size()
  maxY = 1

  setup(startX, startY, maxX, maxY, ORIENTATION_LEFTRIGHT)

  startTime = get_time()
  startEnergy = num_items(Items.Power)
  _sort_line_two_way(startX, maxX, ORIENTATION_LEFTRIGHT)
  endEnergy = num_items(Items.Power)
  endTime = get_time()

  quick_print("Two way sort time:", endTime - startTime, "seconds. Energy spent: ", startEnergy - endEnergy)

  return endTime - startTime, startEnergy - endEnergy

def testTwoUpDown():
  startX = 1
  startY = 0
  maxX = 1
  maxY = get_world_size()

  setup(startX, startY, maxX, maxY, ORIENTATION_UPDOWN)

  startTime = get_time()
  startEnergy = num_items(Items.Power)
  _sort_line_two_way(startY, maxY, ORIENTATION_UPDOWN)
  endEnergy = num_items(Items.Power)
  endTime = get_time()

  quick_print("Two way sort time:", endTime - startTime, "seconds. Energy spent: ", startEnergy - endEnergy)

  return endTime - startTime, startEnergy - endEnergy

def testBubble():
  startX = 0
  startY = 3
  maxX = get_world_size()
  maxY = 1

  setup(startX, startY, maxX, maxY, ORIENTATION_LEFTRIGHT)

  startTime = get_time()
  startEnergy = num_items(Items.Power)
  _sort_bubble(maxX, maxY, startX, startY)
  endEnergy = num_items(Items.Power)
  endTime = get_time()

  quick_print("Bubble sort time:", endTime - startTime, "seconds. Energy spent: ", startEnergy - endEnergy)

  return endTime - startTime, startEnergy - endEnergy

if __name__ == "__main__":
  utils.moveTo(0, 0)

  totalTwoWayTime = 0
  totalBubbleTime = 0

  totalTwoWayEnergy = 0
  totalBubbleEnergy = 0
  for _ in range(1):
    clear()
    twoWayTime, twoWayEnergy = testTwoUpDown()
    totalTwoWayTime += twoWayTime
    totalTwoWayEnergy += twoWayEnergy

    # bubbleTime, bubbleEnergy = testBubble()
    # totalBubbleTime += bubbleTime
    # totalBubbleEnergy += bubbleEnergy

    quick_print("----------------------------")
  
  quick_print("----------------------------")
  quick_print(" * Two Way sort total time:", totalTwoWayTime, "seconds. Energy spent total: ", totalTwoWayEnergy)
  quick_print(" * Bubble sort total time:", totalBubbleTime, "seconds. Energy spent total: ", totalBubbleEnergy)