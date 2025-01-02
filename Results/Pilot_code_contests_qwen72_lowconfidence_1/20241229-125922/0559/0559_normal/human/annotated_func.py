#State of the program right berfore the function call: coord1 and coord2 are tuples representing coordinates (i, j) where 0 <= i < H and 0 <= j < W, and both are road squares (i.e., S_{ij} is `.`).
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
        
    #State of the program after the loop has been executed: To determine the final output state of the loop, let's analyze the behavior of the loop step by step and consider the changes to the variables over multiple iterations.
    #
    #### Initial State:
    #- `cur_coord` is `coord1`
    #- `coord1` and `coord2` are tuples representing coordinates (i, j) where 0 <= i < H and 0 <= j < W, and both are road squares (i.e., S_{ij} is `.`)
    #- `depth_dict` is a shallow copy of `depth_dict_org`
    #- `end_coord` is `coord2`
    #- `cur_depth` is 0
    #- `used_coords` is `[coord1]`
    #- `childs` is `graph[coord1]`
    #
    #### Loop Execution:
    #1. **First Iteration:**
    #   - `cur_depth` is incremented to 1.
    #   - `used_coords` is updated to `[coord1] + graph[coord1]`.
    #   - For each `child` in `childs`, `func_2(child, coord2, used_coords)` is called.
    #   - If `func_2` returns 'found', the loop exits and returns `cur_depth + 1`.
    #   - Otherwise, `next_childs` is populated with the results of `func_2` that are not 'found'.
    #   - `childs` is updated to a list of unique elements from `next_childs`.
    #
    #2. **Subsequent Iterations:**
    #   - `cur_depth` is incremented by 1 for each iteration.
    #   - `used_coords` is extended with the current `childs`.
    #   - For each `child` in `childs`, `func_2(child, coord2, used_coords)` is called.
    #   - If `func_2` returns 'found', the loop exits and returns `cur_depth + 1`.
    #   - Otherwise, `next_childs` is populated with the results of `func_2` that are not 'found'.
    #   - `childs` is updated to a list of unique elements from `next_childs`.
    #
    #### Final Output State:
    #The loop continues until `len(childs) == 0`, meaning there are no more unexplored children to process. At this point, the following conditions will hold:
    #
    #- `cur_depth` will be the number of iterations the loop has executed.
    #- `used_coords` will contain all the coordinates that have been explored, starting from `coord1` and including all children explored in each iteration.
    #- `childs` will be an empty list, indicating no more unexplored children.
    #- If `func_2` ever returned 'found', the loop would have exited early, returning `cur_depth + 1`.
    #
    #Therefore, the final output state is:
    #**`cur_coord` is `coord1`, `coord1` and `coord2` are tuples representing coordinates (i, j) where 0 <= i < H and 0 <= j < W, and both are road squares (i.e., S_{ij} is `.`), `depth_dict` is a shallow copy of `depth_dict_org`, `end_coord` is `coord2`, `cur_depth` is the number of iterations the loop has executed, `used_coords` contains all coordinates explored during the search, `childs` is an empty list.**
    return 0
    #The program returns 0. The variables `cur_coord`, `coord1`, and `coord2` remain unchanged as tuples representing coordinates (i, j) where 0 <= i < H and 0 <= j < W, and both are road squares (i.e., S_{ij} is `.`). `depth_dict` remains a shallow copy of `depth_dict_org`. `end_coord` remains `coord2`. `cur_depth` is the number of iterations the loop has executed. `used_coords` contains all coordinates explored during the search. `childs` is an empty list.
#Overall this is what the function does:The function `func_1` performs a breadth-first search (BFS) to find a path between two coordinates `coord1` and `coord2` on a grid. It accepts two parameters: `coord1` and `coord2`, both tuples representing coordinates (i, j) where 0 <= i < H and 0 <= j < W, and both are road squares (i.e., S_{ij} is `.`). The function returns an integer value representing the depth (number of steps) taken to find a path, or 0 if no path is found. 

-

#State of the program right berfore the function call: jibun and target are tuples representing coordinates (row, column) of road squares in the maze, used_coords is a set of tuples representing coordinates of road squares that have already been visited.
def func_2(jibun, target, used_coords):
    childs = []
    for child in graph[jibun]:
        if child == target:
            return 'found'
        
        if child not in used_coords:
            childs.append(child)
        
    #State of the program after the  for loop has been executed: `jibun` is a valid key in `graph`, `graph[jibun]` contains the neighbors of `jibun`, `target` is a tuple, `used_coords` is a set of tuples, and `childs` is a list of all unique children of `jibun` that are not in `used_coords` and are not equal to `target`. If any `child` equals `target`, the program returns 'found' and does not complete the loop. If `graph[jibun]` is empty or all children are in `used_coords` or equal to `target`, `childs` remains an empty list.
    return childs
    #The program returns a list of all unique children of `jibun` that are not in `used_coords` and are not equal to `target`. If any child equals `target`, the program returns 'found'. If `graph[jibun]` is empty or all children are in `used_coords` or equal to `target`, the program returns an empty list.
#Overall this is what the function does:The function `func_2` accepts three parameters: `jibun`, `target`, and `used_coords`. `jibun` and `target` are tuples representing coordinates, and `used_coords` is a set of tuples representing coordinates that have already been visited. The function returns 'found' if any neighbor of `jibun` matches the `target`. Otherwise, it returns a list of all unique neighbors of `jibun` that are not in `used_coords` and are not equal to `target`. If `jibun` has no neighbors, or all neighbors are either in `used_coords` or equal to `target`, the function returns an empty list. Edge cases include scenarios where `jibun` is not a valid key in `graph` (which would raise a KeyError), or if `graph[jibun]` is empty, leading to an immediate return of an empty list.

