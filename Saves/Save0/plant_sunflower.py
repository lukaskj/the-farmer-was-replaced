import utils
from globals import WORLD_SIZE

def compare(a, b):
  return a[2] >= b[2]

def start(maxX, maxY):
  sunflowerPetals = []
  for _ in range(maxX * maxY):
    nextX, nextY, curX, curY = utils.get_pos_with_next(maxX, maxY)

    if can_harvest():
      harvest()      

    souldTill, _ = utils.get_ground_to_plant(Entities.Sunflower)
    if souldTill:
      till()
    plant(Entities.Sunflower)

    power = measure()
    if power != None:
      sunflowerPetals.append((curX, curY, power))    

    utils.move_to(nextX, nextY)
  
  before = num_items(Items.Power)
  utils.sort(sunflowerPetals, compare)
  for i in range(len(sunflowerPetals)):
    x, y, _ = sunflowerPetals[i]
    utils.move_to(x, y)
    if not can_harvest():
      utils.wait_for(can_harvest)
    harvest()
  return num_items(Items.Power) - before
    

if __name__ == "__main__":
  utils.move_to(0, 0)
  x = 10
  y = 5
  start(x, y)