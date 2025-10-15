import utils
from globals import w, h

def start():
  lenY = h
  lenX = w

  col, row = utils.getPos()
  x = col % lenX
  y = row % lenY
  seed = Entities.Grass
  while True:
    if x < 6 and y < 6:
      seed = Entities.Pumpkin
    elif x >= 13 or y >= 13:
      if (x + y) % 2 == 0:
        seed = Entities.Tree
      else:
        seed = Entities.Bush
    elif x >= 10 or y >= 10:
      seed = Entities.Carrot
    elif (x + y) % 2 == 0:
      seed = Entities.Grass
    
    if can_harvest():
      harvest()

    souldTill, _ = utils.getGroundToPlant(seed)
    if souldTill:
      till()
    plant(seed)

    x, y = utils.getNextPos()
    utils.moveTo(x, y)


if __name__ == "__main__":
  utils.moveTo(0, 0)
  start()