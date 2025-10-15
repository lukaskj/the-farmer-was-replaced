import utils
from globals import WORLD_SIZE

def _sort_compare(a, b):
  return a[2] >= b[2]

def start(maxX, maxY):
  utils.move_to(0,0)
  sunflowerPetals = []
  canUseWater = utils.can_use_water(maxX * maxY)
  for _ in range(maxX * maxY):
    nextX, nextY, curX, curY = utils.get_pos_with_next(maxX, maxY)

    if can_harvest():
      harvest()      

    souldTill, _ = utils.get_ground_to_plant(Entities.Sunflower)
    if souldTill:
      till()
    plant(Entities.Sunflower)
    if canUseWater:
      use_item(Items.Water)

    power = measure()
    if power != None:
      sunflowerPetals.append((curX, curY, power))    

    utils.move_to(nextX, nextY)
  
  before = num_items(Items.Power)
  utils.sort(sunflowerPetals, _sort_compare)
  for i in range(len(sunflowerPetals)):
    x, y, _ = sunflowerPetals[i]
    utils.move_to(x, y)
    if not can_harvest() and get_entity_type() != None:
      utils.wait_for(can_harvest)
    harvest()
  return num_items(Items.Power) - before
    

if __name__ == "__main__":
  utils.move_to(0, 0)
  x = 8
  y = 8
  totalHarvested = 0
  for _ in range(3):
    totalHarvested += start(x, y)
  quick_print("Total harvested:", totalHarvested)