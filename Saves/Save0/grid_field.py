from globals import w, h
import utils

farm = [
  [Entities.Sunflower, Entities.Grass     , Entities.Grass     , Entities.Grass  , Entities.Grass  , Entities.Grass  , Entities.Grass  , Entities.Grass   ],
  [Entities.Grass    , Entities.Grass     , Entities.Grass     , Entities.Carrot , Entities.Carrot , Entities.Carrot , Entities.Carrot , Entities.Carrot  ],
  [Entities.Grass    , Entities.Grass     , Entities.Grass     , Entities.Carrot , Entities.Pumpkin, Entities.Pumpkin, Entities.Pumpkin, Entities.Pumpkin ],
  [Entities.Tree     , Entities.Bush      , Entities.Tree      , Entities.Carrot , Entities.Pumpkin, Entities.Pumpkin, Entities.Pumpkin, Entities.Pumpkin ],
  [Entities.Bush     , Entities.Tree      , Entities.Bush      , Entities.Carrot , Entities.Pumpkin, Entities.Pumpkin, Entities.Pumpkin, Entities.Pumpkin ],
  [Entities.Tree     , Entities.Bush      , Entities.Tree      , Entities.Carrot , Entities.Pumpkin, Entities.Pumpkin, Entities.Pumpkin, Entities.Pumpkin ],
  [Entities.Grass    , Entities.Grass     , Entities.Grass     , Entities.Grass  , Entities.Grass  , Entities.Carrot , Entities.Carrot , Entities.Carrot  ],
  [Entities.Grass    , Entities.Grass     , Entities.Grass     , Entities.Grass  , Entities.Grass  , Entities.Grass  , Entities.Grass  , Entities.Grass  ],
]

def start():
  global farm
  lenY = len(farm)
  lenX = len(farm[0])
  
  x, y = utils.get_pos()
  while True:
    col = x % lenX
    row = y % lenY
    
    # seedRow = lenX - 1 - row
    # seedCol = col
    # seed = farm[seedRow][seedCol]
    seed = farm[row][col]
    if can_harvest():
      harvest()
    shouldTill, ground = utils.get_ground_to_plant(seed)


    if shouldTill:
      till()
    
    plant(seed)
    x, y = utils.get_next_pos()
    utils.move_to(x, y)

if __name__ == "__main__":
  start()