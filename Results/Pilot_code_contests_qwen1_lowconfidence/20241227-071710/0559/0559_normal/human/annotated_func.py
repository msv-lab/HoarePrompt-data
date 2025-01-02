#State of the program right berfore the function call: coord1 and coord2 are tuples representing the coordinates (row, column) of two road squares in the maze. depth_dict_org is a dictionary mapping coordinates to their depths, graph is a dictionary where keys are coordinates of road squares and values are lists of coordinates of directly reachable road squares from the key coordinate.
def func_1(coord1, coord2):
    depth_dict = depth_dict_org.copy()
    cur_coord = coord1
    end_coord = coord2
    cur_depth = 0
    used_coords = [coord1]
    childs = graph[coord1]
    while len(childs) != 0:
        cur_depth += 1
        
        next_childs = []
        
        used_coords += childs
        
        for child in childs:
            res = func_2(child, coord2, used_coords)
            if res == 'found':
                return cur_depth + 1
            next_childs += res
        
        childs = list(set(next_childs))
        
    #State of the program after the loop has been executed: `cur_depth` is the minimum depth found to reach `coord2` from `coord1`, `used_coords` is a list of all unique coordinates visited during the search, including `coord1` and all reachable coordinates, `next_childs` is an empty list, `childs` is an empty list, `graph` is a dictionary where keys are coordinates of road squares and values are lists of coordinates of directly reachable road squares from the key coordinate, `coord1` is a tuple representing the coordinates of a road square in the maze, `coord2` is a tuple representing the coordinates of another road square in the maze, `depth_dict` is a copy of `depth_dict_org`, `end_coord` is equal to `coord2`.
    return 0
    #The program returns 0
#Overall this is what the function does:The function `func_1` accepts two coordinates (`coord1` and `coord2`), a dictionary mapping coordinates to their depths (`depth_dict_org`), and a graph representing the maze structure (`graph`). It performs a breadth-first search (BFS) to find the shortest path from `coord1` to `coord2`. If such a path exists, it returns the minimum depth required to reach `coord2` from `coord1`, incremented by 1. If no path is found, it returns 0.

#State of the program right berfore the function call: jibun is an integer representing a coordinate in the maze, target is a coordinate (also an integer) that represents the goal coordinate, and used_coords is a set of coordinates (integers) that have already been visited. The graph is a dictionary where keys are coordinates (integers) and values are lists of adjacent road coordinates (integers).
def func_2(jibun, target, used_coords):
    childs = []
    for child in graph[jibun]:
        if child == target:
            return 'found'
        
        if child not in used_coords:
            childs.append(child)
        
    #State of the program after the  for loop has been executed: `jibun` is a valid coordinate in the `graph` dictionary, `graph[jibun]` is an empty list, `childs` contains all the coordinates that were explored starting from `jibun` and none of them match `target`, and `used_coords` contains all the coordinates that were visited during the exploration.
    return childs
    #The program returns a list 'childs' containing all the coordinates that were explored starting from 'jibun' and none of them match 'target'
#Overall this is what the function does:The function `func_2` accepts three parameters: `jibun` (an integer representing a coordinate in the maze), `target` (an integer representing the goal coordinate), and `used_coords` (a set of integers representing coordinates that have already been visited). It performs a depth-first search (DFS) to explore the neighboring coordinates of `jibun` that have not been visited yet. If the `target` coordinate is found during the exploration, it returns the string `'found'`. If the `target` is not found, it returns a list of all explored coordinates starting from `jibun` that do not match `target`.

