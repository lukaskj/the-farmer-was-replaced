import utils
from globals import WORLD_SIZE

def _sort_compare(a, b):
  return a[2] >= b[2]

def start(maxX, maxY):
  utils.moveTo(0,0)
  sunflowerPetals = []
  canUseWater = utils.canUseWater(maxX * maxY)
  for _ in range(maxX * maxY):
    nextX, nextY, curX, curY = utils.getPosWithNext(maxX, maxY)

    if can_harvest():
      harvest()      

    souldTill, _ = utils.getGroundToPlant(Entities.Sunflower)
    if souldTill:
      till()
    plant(Entities.Sunflower)
    if canUseWater:
      use_item(Items.Water)

    power = measure()
    if power != None:
      sunflowerPetals.append((curX, curY, power))    

    utils.moveTo(nextX, nextY)
  
  before = num_items(Items.Power)
  utils.sort(sunflowerPetals, _sort_compare)
  for i in range(len(sunflowerPetals)):
    x, y, _ = sunflowerPetals[i]
    utils.moveTo(x, y)
    if not can_harvest() and get_entity_type() != None:
      utils.waitFor(can_harvest)
    harvest()
  return num_items(Items.Power) - before
    

if __name__ == "__main__":
  utils.moveTo(0, 0)
  x = 12
  y = 12
  totalHarvested = 0
  power = 0
  while power < 20000:
    totalHarvested += start(x, y)
    power = num_items(Items.Power)
    quick_print("Power:", power)
  quick_print("Total harvested:", totalHarvested)