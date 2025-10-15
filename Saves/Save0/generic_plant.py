import utils

def start(seed, maxW, maxH, item = None):
  itemToHarvest = utils.seed_to_item(seed)
  if not seed:
    quick_print("No seed selected!")
    return
  
  addFertilizer = num_items(Items.Weird_Substance) < 5000
  _plant(seed, maxW, maxH, item, addFertilizer)
  
  startAmount = num_items(itemToHarvest)
  
  _harvest(maxW, maxH, seed)
  

  return num_items(itemToHarvest) - startAmount
  
  

def _plant(seed, maxW, maxH, item = None, addFertilizer = False):
  startTime = get_time()
  utils.move_to(0, 0)
  totalPlots = maxW * maxH
  for _ in range(totalPlots):
    x, y = utils.get_next_pos(maxW, maxH)

    if can_harvest():
      harvest()
    souldTill, _ = utils.get_ground_to_plant(seed)
    if souldTill:
      till()
    if item == Items.Wood:
      curX, curY = utils.get_pos()
      if (curX + curY) % 2 == 0:
        plant(Entities.Tree)
      else:
        plant(seed)
    else:
      plant(seed)

    if addFertilizer:
      curX, curY = utils.get_pos()
      if ((curX + curY) % 2) == 1:
        use_item(Items.Fertilizer)

    utils.move_to(x, y)
  quick_print("Planted " + str(totalPlots) + " seeds in " + str(get_time() - startTime) + " seconds")

def _harvest(maxW, maxH, seed):
  totalPlots = maxW * maxH
  harvestedPlots = 0
  utils.move_to(0, 0)
  notHarvested = []
  for _ in range(totalPlots):
    if can_harvest():
      harvest()
      harvestedPlots += 1
    else:
      notHarvested.append(utils.get_pos())
    x, y = utils.get_next_pos(maxW, maxH)
    utils.move_to(x, y)

  # Loop to harvest not harvested plots
  while harvestedPlots < totalPlots:
    tmpNotHarvested = notHarvested[:]

    # wait to grow
    do_a_flip()
    if seed == Entities.Sunflower:
      do_a_flip()
    # quick_print("Loop - Harvested: " + str(harvested) + ", Total: " + str(totalPlots) + " - " + str(notHarvested))
    for (col, row) in tmpNotHarvested:
      utils.move_to(col, row)
      plotUnderDrone = get_entity_type()
      if can_harvest() or plotUnderDrone == None or plotUnderDrone == Entities.Dead_Pumpkin:
        harvestedPlots += 1
        harvest()
        notHarvested.remove((col, row))
  
  return harvestedPlots

if __name__ == "__main__":
  seedToPlant = Entities.Bush
  expectedItem = Items.Wood
  runs = 1
  fieldW = get_world_size()
  fieldH = get_world_size()
  for _ in range(runs):
    utils.move_to(0, 0)
    start(seedToPlant, fieldW, fieldH, expectedItem)