import utils
speed = 1000
#scriptName = "z_test"
scriptName = "optimized_cactus"
scriptName = "plant_pumpkin"
scriptName = "leaderboard_cactus"
scriptName = "polyculture"
# scriptName = "docs1"


sim_globals = {
  "seed": Entities.Tree,
  "maxDrones": max_drones(),
  "width": get_world_size(),
  "height": get_world_size(),
  "runs": 1,
  "leaderboardMin": 33554432,
}
simSeed = 22091989
# simSeed = -1

utils.moveTo(0, 0)
sim_items = {}
for item in Items:
  sim_items[item] = 1000000000


# sim_items = {Items.Carrot : 10000, Items.Hay : 50}
simTime = simulate(scriptName, Unlocks, sim_items, sim_globals, simSeed, speed)
quick_print("--")
quick_print("Simulation finished. Simulation time:", simTime)
