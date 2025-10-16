import utils
import drones
# from globals import w, h

totalGrown = 0
addFertilizer = False
deadPlants = []

def _plantPunpkins(seed, startX, startY, width, height):
  # quick_print(seed, startX, startY, width, height)
  pass

def __spawnDrone():
  def run(gridData):
    seed = Entities.Pumpkin
    startX, startY, width, height = gridData
    def __():
      for _ in range(width * height):
        _plantPunpkins(seed, startX, startY, width, height)
        utils.plantSeed(seed)
        nextX, nextY = utils.getNextSubgridPos(width, height, startX, startY)
        utils.moveTo(nextX, nextY)
      
      # utils.sleep(10)
    return __
  return run


def _plant_pumpkin_field(maxW, maxH):
  seed = Entities.Pumpkin
  for row in range(maxH):
    for col in range(maxW):
      utils.moveTo(col, row)
      if get_entity_type() == seed:
        continue
      plant_and_fertilize(col, row)
      # if (col % 2 == 0 and row % 2 != 0) or (col % 2 != 0 and row % 2 == 0):

def _calculate_dead_plants(maxW, maxH):
  global totalGrown
  global deadPlants
  deadPlants = []
  totalGrown = 0
  for row in range(maxH):
    for col in range(maxW):
      utils.moveTo(col, row)
      if can_harvest():
        totalGrown += 1
      elif get_entity_type() == Entities.Dead_Pumpkin:
        plant_and_fertilize(col, row)
        deadPlants.append((col, row))
        if get_water() < 0.11:
          use_item(Items.Water)
  # utils.sort_coordinates(deadPlants)
  # quick_print("Total grown: " + str(totalGrown) + "/" + str(maxW * maxH))
  # quick_print("Dead plants at: " + str(deadPlants))

def _replant_dead():
  global deadPlants
  global totalGrown
  
  while len(deadPlants) > 0:
    # if len(deadPlants) > 1:
    #   quick_print("Replanting dead plants, left: " + str(deadPlants))
    for (col, row) in deadPlants:
      utils.moveTo(col, row)
      if can_harvest() and get_entity_type() == Entities.Pumpkin:
        deadPlants.remove((col, row))
        totalGrown += 1
        continue
      plant_and_fertilize(col, row)
      if get_water() < 0.11:
        use_item(Items.Water)

def plant_and_fertilize(col, row):
  seed = Entities.Pumpkin
  shouldTill, _ = utils.getGroundToPlant(seed)
  if shouldTill:
    till()
  plant(seed)
  _add_fertilizer(col, row)

def _add_fertilizer(col, row):
  if addFertilizer and col % 2 == 0 and row % 2 == 0:
    use_item(Items.Fertilizer)

def start(maxW, maxH):
  global totalGrown
  global addFertilizer
  harvested = False
  totalHarvested = 0
  while not harvested:
    # addFertilizer = num_items(Items.Weird_Substance) < 100 and num_items(Items.Fertilizer) > 100
    quick_print("Add fertilizer: " + str(addFertilizer))
    # _plant_pumpkin_field(maxW, maxH)
    drones.droneGrid(maxW, maxH, __spawnDrone(), None)
    drones.waitForAllDronesToFinish()
    _calculate_dead_plants(maxW, maxH)
    _replant_dead()
    if can_harvest():
      # do_a_flip()
      before = num_items(Items.Pumpkin)
      totalGrown = 0
      harvest()
      harvested = True
      totalHarvested += num_items(Items.Pumpkin) - before
      
  return totalHarvested


if __name__ == "__main__":
  maxW2 = 10
  maxH2 = 10
  runs = 10
  for _ in range(runs):
    start(maxW2, maxH2)
  # clear()
  # harvest()