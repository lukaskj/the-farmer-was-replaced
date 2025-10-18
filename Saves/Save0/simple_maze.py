import utils
clear()

quick_print(clear.__code__ )


# sharedData = {
#   "listeners": {},
# }

# change_hat(Hats.Cactus_Hat)
# def ____():
#   return sharedData
# drone = spawn_drone(____)

# def on(event, fnc):
#   if fnc == None:
#     return False
#   shared2 = wait_for(drone)
#   if not event in shared2["listeners"]:
#     shared2["listeners"][event] = []
#   shared2["listeners"][event].append(fnc)
#   return True
  

# def emit(event, args = None):
#   shared2 = wait_for(drone)
#   if not event in shared2["listeners"]:
#     return False
#   for listener in shared2["listeners"][event]:
#     if args == None:
#       listener()
#     else:
#       listener(args)
#   quick_print("Emit", shared2)
#   return True


# def worker():
#   started = False

#   def onStart(args):
#     global started
#     quick_print("On start received", args)
#     started = True
#   on("start", onStart)

#   def onTill():
#     quick_print("ON TILL")
#     till()
#     utils.moveTo(7, 7)
#   on("till", onTill)

#   def onChange_hat(hat):
#     quick_print("ON CHANGE_HAT", hat)
#     change_hat(hat)
#   on("change_hat", onChange_hat)

#   # def on(event, args):
#   #   global started
#   #   quick_print("Received event", event, "args", args)
#   #   if event == "start":
#   #     started = True
#   # addListener(on)

#   # while not started:
#   till()
#   utils.sleep(1)
#   move(North)
#   till()
#   utils.sleep(1)
#   quick_print("Start working!!")


# def main():
#   change_hat(Hats.Wizard_Hat)
#   utils.moveTo(2, 5)
#   # emit("start", "worked")
#   # utils.sleep(2)
#   def onNewDrones(args):
#     quick_print("onNewDrones", args)
#   on("new-drones", onNewDrones)

#   emit("start", 1)
#   emit("till")
#   emit("till")
#   emit("till")
#   emit("till")
#   utils.sleep(2)
#   # emit("start", "worked2")
#   emit("till")
#   utils.sleep(2)
#   emit("change_hat", Hats.Cactus_Hat)
#   utils.sleep(3)

#   # shared["start"] = True
  
# spawn_drone(main)
# for i in range(3):
#   spawn_drone(worker)
#   utils.moveTo(i, i)

# utils.sleep(0.5)
# quick_print("New drones")
# for i in range(1):
#   spawn_drone(worker)
#   utils.moveTo(5, i)

# emit("new-drones", 1)


# utils.sleep(10)
