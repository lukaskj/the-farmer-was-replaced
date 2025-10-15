import utils

def start(maxX, maxY):
  utils.move_to(0, 0)
  _plant(maxX, maxY)
  _sort_cols(maxX, maxY)
  _sort_rows(maxX, maxY)
  
  return _harvest()

def _plant(maxX, maxY):
  seed = Entities.Cactus
  for _ in range(maxX * maxY):
    x, y = utils.get_next_pos(maxX, maxY)
    
    souldTill, _ = utils.get_ground_to_plant(seed)
    if souldTill:
      till()
    plant(seed)

    utils.move_to(x, y)

def _sort_cols(maxX, maxY):
  quick_print("Sorting columns")
  for y in range(maxY):
    n = maxX
    swapped = True
    while swapped:
      swapped = False
      utils.move_to(0, y)
      for x in range(n - 1):
        if can_harvest():
          if not _is_next_cactus_bigger(East):
            swap(East)
            swapped = True
        move(East)
      n -= 1  # Last element is in place after each pass
      if not swapped:  # Early termination if no swaps needed
        break

def _sort_rows(maxX, maxY):
  quick_print("Sorting rows")
  for x in range(maxX):
    n = maxY
    swapped = True
    while swapped:
      swapped = False
      utils.move_to(x, 0)
      for y in range(n - 1):
        if not _is_next_cactus_bigger(North):
          swap(North)
          swapped = True
        move(North)
      n -= 1  # Last element is in place after each pass
      if not swapped:  # Early termination if no swaps needed
        break
      
    # utils.move_to(x, y)

def _is_next_cactus_bigger(direction):
  selfSize = measure()
  nextSize = measure(direction)
  if nextSize != None and selfSize <= nextSize:
    return True
  return False 

def _harvest():
  if can_harvest():
    before = num_items(Items.Cactus)
    harvest()
    after = num_items(Items.Cactus)
    return after - before



if __name__ == "__main__":
  runs = 1
  maxX = get_world_size()
  maxY = get_world_size()
  maxX = 10
  maxY = 10

  startTime = get_time()
  harvested = start(maxX, maxY)
  end = get_time()

  quick_print("(old) Harvested", harvested, "in", end - startTime, "seconds")