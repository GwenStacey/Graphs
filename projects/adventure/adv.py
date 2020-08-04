from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

#pick a room from the graph to start in
starting_room = world.starting_room
starting_exits = starting_room.get_exits()
trav_graph = {starting_room.id:{x:'?' for x in starting_exits}}
#If there are valid exits, they need to be explored
trav_stack = []
trav_stack.append(starting_room)
trav_visited = set()
while len(trav_visited)<len(world.rooms):
    print(trav_stack)
    current_room = trav_stack.pop()
    #print(current_room.id)
    if current_room is not None:
        trav_visited.add(current_room.id)
    print(f'Visited: {trav_visited}')
    exits = current_room.get_exits()
    for ex in exits:
        neighbor = current_room.get_room_in_direction(ex)
        if neighbor.id not in trav_graph:
            trav_graph[neighbor.id] = {x:'?' for x in neighbor.get_exits()}
        if trav_graph[current_room.id][ex] == '?':
            trav_graph[current_room.id][ex] = neighbor.id
            traversal_path.append(ex)
            print(traversal_path)
            print(trav_graph)
            trav_stack.append(neighbor)
            break
        if ex in trav_graph[neighbor.id] and trav_graph[neighbor.id][ex] == '?':
            trav_graph[current_room.id][ex] = neighbor.id
            print(trav_graph)
            traversal_path.append(ex)
            trav_stack.append(neighbor) 
            break
        else:
            west_room = current_room.get_room_in_direction('w')
            east_room = current_room.get_room_in_direction('e')
            north_room = current_room.get_room_in_direction('n')
            south_room = current_room.get_room_in_direction('s')

            if west_room is not None and west_room.id not in trav_graph:
                trav_graph[west_room.id] = {x:'?' for x in west_room.get_exits()}
            if east_room is not None and east_room.id not in trav_graph:
                trav_graph[east_room.id] = {x:'?' for x in east_room.get_exits()}
            if north_room is not None and north_room.id not in trav_graph:
                trav_graph[north_room.id] = {x:'?' for x in north_room.get_exits()}
            if south_room is not None and south_room.id not in trav_graph:
                trav_graph[south_room.id] = {x:'?' for x in south_room.get_exits()}

            if '?' in trav_graph[current_room.id].values():
                val_list = list(trav_graph[current_room.id].values())
                key_list = list(trav_graph[current_room.id].keys())
                direction = key_list[val_list.index('?')]
                print(direction)
                neighbor = current_room.get_room_in_direction(direction)
                if neighbor is not None:
                    trav_graph[current_room.id][direction] = neighbor.id
                    traversal_path.append(direction)
                    trav_stack.append(neighbor)
                print(traversal_path)
                print(trav_graph)
                print(trav_stack)
                break

            
            if west_room is not None and '?' in trav_graph[west_room.id].values():
                trav_graph[current_room.id][direction] = west_room.id
                traversal_path.append('w')
                trav_stack.append(west_room)
                print(traversal_path)
                print(trav_graph)
                print(trav_stack)
                break
            
            if east_room is not None and '?' in trav_graph[east_room.id].values():
                trav_graph[current_room.id][direction] = east_room.id
                traversal_path.append('e')
                trav_stack.append(east_room)
                print(traversal_path)
                print(trav_graph)
                print(trav_stack)
                break
            if north_room is not None and '?' in trav_graph[north_room.id].values():
                trav_graph[current_room.id][direction] = north_room.id
                traversal_path.append('n')
                trav_stack.append(north_room)
                print(traversal_path)
                print(trav_graph)
                print(trav_stack)
                break
            
            if south_room is not None and '?' in trav_graph[south_room.id].values():
                trav_graph[current_room.id][direction] = south_room.id
                traversal_path.append('s')
                trav_stack.append(south_room)
                print(traversal_path)
                print(trav_graph)
                print(trav_stack)
                break
            
            
            if any('?' in d.values() for d in trav_graph.values()):
                print(current_room.id)
                print(current_room.get_exits())
                ex = random.sample(current_room.get_exits(), 1)
                print(ex)
                neighbor = current_room.get_room_in_direction(ex)
                if neighbor is not None:
                    print(f'New Room :{neighbor}')
                    traversal_path.append(ex)
                    trav_stack.append(neighbor)
                    print(f'New Stack :{trav_stack}')
                    break
                else:
                    ex2 = random.sample(current_room.get_exits(), 1)
                    traversal_path.append(ex2)
                    trav_stack.append(current_room.get_room_in_direction(ex2))
                    print(f'New Stack :{trav_stack}')
                    break
                #print(f'Items:{trav_graph[neighbor.id].items()}')
            continue
            
    
        
        

print(trav_graph)
# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
#player.current_room.print_room_description(player)
#while True:
#    cmds = input("-> ").lower().split(" ")
#    if cmds[0] in ["n", "s", "e", "w"]:
#        player.travel(cmds[0], True)
#    elif cmds[0] == "q":
#        break
#    else:
#        print("I did not understand that command.")
