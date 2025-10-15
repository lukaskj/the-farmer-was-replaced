from utils import moveTo

def generate_maze():
    plant(Entities.Bush)
    substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
    use_item(Items.Weird_Substance, substance)
    
def random_sign():
    num = random()
    if num >= 0.5:
        return 1
    else:
        return -1
        
def solve_maze():
    sign = random_sign()
    dirs = [East, North, West, South]
    currentDir = 1
    while get_entity_type() != Entities.Treasure:
        if num_items(Items.Gold) >= 9863168:
            return
        if not move(dirs[currentDir - 1]):
            if num_drones() < max_drones() and random() > 0.9:
                spawn_drone(solve_maze)
            currentDir = (currentDir - (1*sign)) % 4
        else:
            currentDir = (currentDir + (1*sign)) % 4  
            
    harvest()
    generate_maze()
        
def wait_then_maze_solve():
    while get_entity_type() != Entities.Hedge:
        pass
    solve_maze()
    
def main():
    clear()
    for i in range(get_world_size()):
        moveTo(i,i)
        if num_drones() < max_drones():
            spawn_drone(wait_then_maze_solve)
            
    till()
    generate_maze()
    while num_items(Items.Gold) < 9863168:
        solve_maze()
    
if __name__ == "__main__":
    main()