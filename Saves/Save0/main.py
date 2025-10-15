from globals import w, h
import utils
import generic_plant
import plant_cactus
import plant_pumpkin

change_hat(Hats.Wizard_Hat)

logPrefix = "[*]"
quick_print(logPrefix, "World size: " + str(w) + "x" + str(h))
quick_print("")
# clear()


size = get_world_size()

minItems = {
  Items.Power: {
    "amount": 1000,
    "w": 10,
    "h": 10,
  },
  Items.Hay: {
    "amount": 450000,
    "w": size,
    "h": size,
  },
  Items.Wood: {
    "amount": 500000,
    "w": size,
    "h": size,
  },
  Items.Carrot: {
    "amount": 220000,
    "w": size,
    "h": size,
  },
  Items.Pumpkin: {
    "amount": 300000,
    "w": 10,
    "h": 10,
  },
  Items.Cactus: {
    "amount": 4000000,
    "w": size,
    "h": size,
  },
}

def harvest_power():
  item = Items.Power
  seed = Entities.Sunflower
  minAmount = 100
  expectedAmount, currentAmount, fieldW, fieldH = _get_config(item)
  if currentAmount < minAmount:
    plant_crop(item, expectedAmount, fieldW, fieldH, True)
    currentAmount = num_items(item)

def _get_config(item):
  expectedAmount = 0
  currentAmount = 0
  fieldWidth = 0
  fieldHeight = 0

  if item in minItems:
    config = minItems[item]
    expectedAmount = config["amount"]
    currentAmount = num_items(item)
    fieldWidth = config["w"]
    fieldHeight = config["h"]
  
  return expectedAmount, currentAmount, fieldWidth, fieldHeight

def plant_crop(item, expectedAmount, fieldW, fieldH, bypassCosts = False, isCost = False):  
  seed = utils.item_to_seed(item)
  if seed == None:
    return
  currentTotal = num_items(item)
  if isCost:
    quick_print("  ", logPrefix, "Planting " + str(seed) + ". Total: " + str(currentTotal) + "/" + str(expectedAmount))
  else:
    quick_print(logPrefix, "Planting " + str(seed) + ". Total: " + str(currentTotal) + "/" + str(expectedAmount))    

  while currentTotal < expectedAmount:
    prevTotal = currentTotal
    if item != Items.Power:
      harvest_power()
    
    if not bypassCosts:
      _handle_costs(seed, item)

    if item == Items.Cactus:
      plant_cactus.start(1, fieldW, fieldH)
    elif item == Items.Pumpkin:
      plant_pumpkin.start(fieldW, fieldH)
    else:
      generic_plant.start(seed, 1, fieldW, fieldH, item)
    currentTotal = num_items(item)
    quick_print(logPrefix, "Harvested", str(currentTotal - prevTotal), "of", str(item))

def _handle_costs(seed, item):
  cost = get_cost(seed)
  if cost != None:
    for costItem in cost:
      if costItem in minItems:
        expectedCostAmount, currentCostAmount, costFieldW, costFieldH = _get_config(costItem)
        expectedCostAmount /= 2
        if currentCostAmount < expectedCostAmount:
            quick_print(logPrefix, "------ Planting costs for", str(item), ":", str(costItem), "(" + str(expectedCostAmount) + "/" + str(currentCostAmount) + ")", "------")
            plant_crop(costItem, expectedCostAmount, costFieldW, costFieldH, False, True)
            quick_print(logPrefix, "------------------------------------------------------------------------------")

def start():
  # plant_crop(Items.Pumpkin, 261000, 6, 6, True, False)
  allDone = False
  while not allDone:
    allDone = True
    for item in minItems:
      expectedAmount, currentAmount, fieldW, fieldH = _get_config(item)
      if currentAmount < expectedAmount:
        allDone = False
        plant_crop(item, expectedAmount, fieldW, fieldH)
  quick_print(logPrefix, "All finished!")


if __name__ == "__main__":
  utils.move_to(0, 0)
  start()
  # start(seed, fieldW, fieldH)