import utils
# from globals import w, h

totalGrown = 0
addFertilizer = False
deadPlants = []

def _plant_pumpkin_field(maxW, maxH):
  for row in range(maxH):
    for col in range(maxW):
      seed = Entities.Pumpkin
      utils.move_to(col, row)
      if get_entity_type() == Entities.Pumpkin:
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
      utils.move_to(col, row)
      if can_harvest():
        totalGrown += 1
      elif get_entity_type() == Entities.Dead_Pumpkin:
        plant_and_fertilize(col, row)
        deadPlants.append((col, row))
        if get_water() < 0.11:
          use_item(Items.Water)
  # utils.sort_coordinates(deadPlants)
  quick_print("Total grown: " + str(totalGrown) + "/" + str(maxW * maxH))
  quick_print("Dead plants at: " + str(deadPlants))

def _replant_dead():
  global deadPlants
  global totalGrown
  
  while len(deadPlants) > 0:
    if len(deadPlants) > 1:
      quick_print("Replanting dead plants, left: " + str(deadPlants))
    for (col, row) in deadPlants:
      utils.move_to(col, row)
      if can_harvest() and get_entity_type() == Entities.Pumpkin:
        deadPlants.remove((col, row))
        totalGrown += 1
        continue
      plant_and_fertilize(col, row)
      if get_water() < 0.11:
        use_item(Items.Water)

def plant_and_fertilize(col, row):
  seed = Entities.Pumpkin
  shouldTill, _ = utils.get_ground_to_plant(seed)
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
  while not harvested:
    # addFertilizer = num_items(Items.Weird_Substance) < 100 and num_items(Items.Fertilizer) > 100
    quick_print("Add fertilizer: " + str(addFertilizer))
    _plant_pumpkin_field(maxW, maxH)
    _calculate_dead_plants(maxW, maxH)
    _replant_dead()
    if can_harvest() and totalGrown == maxW * maxH:
      # do_a_flip()
      before = num_items(Items.Pumpkin)
      totalGrown = 0
      harvest()
      harvested = True
      after = num_items(Items.Pumpkin)
      quick_print("Harvested " + str(after - before) + " pumpkins!")


if __name__ == "__main__":
  maxW2 = 10
  maxH2 = 10
  start(maxW2, maxH2)
  # clear()
  # harvest()