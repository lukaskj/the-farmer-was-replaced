WORLD_SIZE = get_world_size()
w, h = WORLD_SIZE, WORLD_SIZE

ORIENTATION_UPDOWN = 1
ORIENTATION_LEFTRIGHT = 2

SEEDS_TO_GROUND = {
  Entities.Bush: Grounds.Grassland,
  Entities.Tree: Grounds.Grassland,
  Entities.Grass: Grounds.Grassland,
  Entities.Carrot: Grounds.Soil,
  Entities.Pumpkin: Grounds.Soil,
  Entities.Sunflower: Grounds.Soil,
  Entities.Cactus: Grounds.Soil,
}

ITEM_TO_SEED = {
  Items.Power: Entities.Sunflower,
  Items.Hay: Entities.Grass,
  Items.Wood: Entities.Bush,
  Items.Carrot: Entities.Carrot,
  Items.Cactus: Entities.Cactus,
  Items.Pumpkin: Entities.Pumpkin,
}

SEED_TO_ITEM = {
  Entities.Sunflower: Items.Power,
  Entities.Grass: Items.Hay,
  Entities.Bush: Items.Wood,
  Entities.Tree: Items.Wood,
  Entities.Carrot: Items.Carrot,
  Entities.Cactus: Items.Cactus,
  Entities.Pumpkin: Items.Pumpkin,
}