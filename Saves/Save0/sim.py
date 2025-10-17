import utils
speed = 64
scriptName = "z_test"
scriptName = "polyculture"
# scriptName = "plant_pumpkin"


sim_globals = {
  "seed": Entities.Grass,
  "maxDrones": max_drones(),
  "width": get_world_size(),
  "height": get_world_size(),
  "runs": 1,
}
simSeed = 0

utils.moveTo(0, 0)
sim_items = {}
for item in Items:
  sim_items[item] = 10000000


# sim_items = {Items.Carrot : 10000, Items.Hay : 50}
simTime = simulate(scriptName, Unlocks, sim_items, sim_globals, simSeed, speed)
quick_print("--")
quick_print("Simulation finished. Simulation time:", simTime)
