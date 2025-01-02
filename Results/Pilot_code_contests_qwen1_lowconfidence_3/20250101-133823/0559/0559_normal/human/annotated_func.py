#State of the program right berfore the function call: coord1 and coord2 are tuples representing coordinates (i, j) of road squares in the maze, where 0 <= i < H and 0 <= j < W. depth_dict_org is a dictionary mapping each coordinate to its initial depth (distance from the start), graph is a dictionary where keys are coordinates and values are lists of adjacent road square coordinates, and end_coord is the coordinate of the goal square.
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
        
    #State of the program after the loop has been executed: `next_childs` is an empty list, `childs` is a list with no duplicate elements, `cur_depth` is the total number of iterations plus 1, `used_coords` includes all the `childs` encountered during the loop executions, the function returns `cur_depth + 1` if `func_2(child, coord2, used_coords)` returns 'found' for any `child` in the final iteration.
    return 0
    #The program returns 0
#Overall this is what the function does:The function `func_1` accepts two parameters `coord1` and `coord2`, which represent coordinates in a maze grid. It initializes a depth dictionary from an original one, sets the current coordinate to `coord1`, and marks `coord1` as used. The function then explores neighboring coordinates using a breadth-first search strategy via recursive calls to `func_2`. If a path to `coord2` is found, it returns the depth (number of steps taken) plus one. If no path is found, it returns zero. The function returns different values based on the depth of the search and whether a path was found:

#State of the program right berfore the function call: jibun is an integer representing a road square in the maze, target is a road square in the maze, and used_coords is a set of tuples representing the coordinates of squares that have already been visited. The function assumes the existence of a graph where each key is a road square and the value is a list of its adjacent road squares.
def func_2(jibun, target, used_coords):
    childs = []
    for child in graph[jibun]:
        if child == target:
            return 'found'
        
        if child not in used_coords:
            childs.append(child)
        
    #State of the program after the  for loop has been executed: `jibun` is an integer representing a road square in the maze, `target` is a road square in the maze, `used_coords` is a set of tuples representing the coordinates of squares that have already been visited, and `childs` is a list of all the child nodes that were explored without being in `used_coords`. The loop will continue to execute until either the `target` is found or there are no more unvisited children for the current `jibun`. If the target is found, the function returns 'found'. If the loop finishes without finding the target, `jibun` remains unchanged, `used_coords` includes all previously visited coordinates, and `childs` is a list of all child nodes that were explored without being in `used_coords`.
    return childs
    #`The program returns a list of all child nodes that were explored without being in used_coords`
#Overall this is what the function does:The function `func_2` accepts three parameters: `jibun`, `target`, and `used_coords`. `jibun` represents a road square in the maze, `target` is another road square in the maze, and `used_coords` is a set of tuples representing the coordinates of squares that have already been visited. The function explores the children (adjacent squares) of the given `jibun` to check if any of them match the `target`. If the `target` is found, the function returns `'found'`. If the `target` is not found among the children, the function returns a list of all child nodes that were explored and confirmed not to be in `used_coords`.

