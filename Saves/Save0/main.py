from globals import w, h
import utils
import drones
import optimized_cactus
import optimized_plant
import plant_pumpkin
import plant_sunflower

change_hat(Hats.Wizard_Hat)

logPrefix = "[*]"
quick_print(logPrefix, "World size: " + str(w) + "x" + str(h))
quick_print("")
# clear()


size = get_world_size()

minItems = {
  Items.Power: {
    "amount": 1000,
    "w": 8,
    "h": 8,
  },
  Items.Hay: {
    "amount": 5000000,
    "w": size,
    "h": size,
  },
  Items.Wood: {
    "amount": 1000000,
    "w": size,
    "h": size,
  },
  Items.Carrot: {
    "amount": 1200000,
    "w": size,
    "h": size,
  },
  Items.Pumpkin: {
    "amount": 800000,
    "w": 10,
    "h": 10,
  },
  Items.Cactus: {
    "amount": 2000000,
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
  seed = utils.itemToSeed(item)
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
      optimized_cactus.start(fieldW, fieldH)
    elif item == Items.Pumpkin:
      plant_pumpkin.start(fieldW, fieldH)
    elif item == Items.Power:
      # plant_sunflower.start(fieldW, fieldH)
      optimized_plant.start(Entities.Sunflower, fieldW, fieldH, 5)
    else:
      optimized_plant.start(seed, fieldW, fieldH, 5)
    utils.moveTo(0, 0)
    drones.waitForAllDronesToFinish()
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
  utils.moveTo(0, 0)
  start()

  # startPower = num_items(Items.Power)
  # plant_crop(Items.Power, 10000, 5, 5, True)
  # quick_print("Harvested", str(num_items(Items.Power)))
  # startPower = num_items(Items.Power)
  # plant_sunflower.start(5, 5)
  # quick_print("Harvested", str(num_items(Items.Power)))

  # start(seed, fieldW, fieldH)