#State of the program right berfore the function call: None of the variables are passed as parameters to the function `func_1`. This function reads a line from standard input, strips any leading or trailing whitespace, splits the line into parts, and maps each part to an integer.
def func_1():
    return map(int, sys.stdin.readline().strip().split())
    #The program returns a map object that converts each part of the input line (after stripping leading/trailing whitespace and splitting by spaces) into an integer. The actual content depends on the input provided to the standard input.
#Overall this is what the function does:The function `func_1` reads a single line from standard input, removes any leading and trailing whitespace, splits the line into parts based on spaces, and converts each part into an integer. It returns a map object containing these integers. The actual content of the map object depends on the input provided. If the input line contains non-integer values, the function will raise a `ValueError`. If the input line is empty or contains only whitespace, the function will return an empty map object.

#State of the program right berfore the function call: None of the variables in the function signature are used, as the function reads input from standard input and returns a list of integers.
def func_2():
    return list(map(int, sys.stdin.readline().strip().split()))
    #The program returns a list of integers read from standard input, where each integer is converted from its string representation.
#Overall this is what the function does:The function `func_2` reads a single line of input from standard input (stdin), splits the line into individual string tokens based on whitespace, converts each token to an integer, and returns a list of these integers. The function assumes that the input line contains valid integer representations separated by whitespace. If the input line is empty or contains non-integer values, the function will raise a `ValueError`. After the function executes, the program will have a list of integers derived from the input, or it will terminate with an error if the input is invalid.

#State of the program right berfore the function call: None. This function does not take any parameters. It reads a line from standard input, strips leading and trailing whitespace, and returns the resulting string.
def func_3():
    return sys.stdin.readline().strip()
    #The program returns a string read from standard input with leading and trailing whitespace removed.
#Overall this is what the function does:The function `func_3` does not accept any parameters. It reads a line from standard input, removes any leading and trailing whitespace from the line, and returns the cleaned string. If the input is empty or consists only of whitespace, the function will return an empty string. The function does not handle any other edge cases, such as handling multi-line input or non-string inputs, and it assumes that the input is a single line of text. After the function concludes, the program state is unchanged except for the returned string, which is the result of the input processing.

#State of the program right berfore the function call: No variables are passed as arguments to `func_4()`. Inside the function, `n` is an integer representing the number of snow drifts, with 1 ≤ n ≤ 100. `lst` is a list that will store tuples `(x, y)` representing the coordinates of each snow drift, where 1 ≤ x, y ≤ 1000. `mydict_x` and `mydict_y` are dictionaries mapping x-coordinates and y-coordinates to lists of corresponding y-coordinates and x-coordinates, respectively. `visited` is a set that will keep track of the snow drifts that have been visited during the depth-first search (DFS).
def func_4():
    n = int(func_3())
    lst = []
    count_of_components = 0
    mydict_x = {i: [] for i in range(1, 1001)}
    mydict_y = {i: [] for i in range(1, 1001)}
    for i in range(n):
        x, y = func_1()
        
        lst.append((x, y))
        
        mydict_x[x].append(y)
        
        mydict_y[y].append(x)
        
    #State of the program after the  for loop has been executed: `n` is an integer between 1 and 100 (inclusive), `lst` is a list containing `n` elements, each element being a tuple `(x, y)`, `mydict_x` is a dictionary with keys from 1 to 1000 where each key `x` maps to a list containing `y` values corresponding to the tuples `(x, y)` in `lst`, `mydict_y` is a dictionary with keys from 1 to 1000 where each key `y` maps to a list containing `x` values corresponding to the tuples `(x, y)` in `lst`, `visited` is a set, `count_of_components` is 0, `i` is `n-1`, `x` and `y` are the last values returned by `func_1()` during the final iteration of the loop, if `n` is 0 then `lst`, `mydict_x`, and `mydict_y` remain unchanged and `i` is -1.
    visited = set()
    for i in lst:
        if i not in visited:
            dfs(i)
            count_of_components += 1
        
    #State of the program after the  for loop has been executed: `n` is an integer between 1 and 100 (inclusive), `lst` is a list containing `n` elements, each element being a tuple `(x, y)`, `mydict_x` is a dictionary with keys from 1 to 1000 where each key `x` maps to a list containing `y` values corresponding to the tuples `(x, y)` in `lst`, `mydict_y` is a dictionary with keys from 1 to 1000 where each key `y` maps to a list containing `x` values corresponding to the tuples `(x, y)` in `lst`, `visited` includes all elements in `lst` and all elements reachable from any element in `lst` through the tuples in `lst`, `count_of_components` is the number of distinct connected components in the graph represented by `lst`, `i` is the last element of `lst`, `x` and `y` are the last values returned by `func_1()` during the final iteration of the loop. If `n` is 0, then `lst`, `mydict_x`, and `mydict_y` remain unchanged, `visited` remains an empty set, `count_of_components` remains 0, and `i` is -1.
    print(count_of_components - 1)
#Overall this is what the function does:The function `func_4` does not accept any parameters. It reads an integer `n` (1 ≤ n ≤ 100) representing the number of snow drifts. It then reads `n` pairs of coordinates `(x, y)` (1 ≤ x, y ≤ 1000) and stores them in a list `lst`. It also populates two dictionaries, `mydict_x` and `mydict_y`, which map x-coordinates to lists of y-coordinates and y-coordinates to lists of x-coordinates, respectively. The function performs a depth-first search (DFS) to find the number of distinct connected components in the graph represented by these coordinates. Finally, it prints the number of connected components minus one. If `n` is 0, the function prints `-1` since there are no snow drifts to form any components.

#State of the program right berfore the function call: i is a tuple of two integers representing the coordinates of a snow drift, and `visited` is a set containing tuples of coordinates of snow drifts that have been visited. `mydict_x` is a dictionary where keys are x-coordinates and values are sets of y-coordinates of snow drifts sharing the same x-coordinate. `mydict_y` is a dictionary where keys are y-coordinates and values are sets of x-coordinates of snow drifts sharing the same y-coordinate.
def dfs(i):
    if (i not in visited) :
        visited.add(i)
        for child in mydict_x[i[0]]:
            if (i[0], child) not in visited:
                dfs((i[0], child))
            
        #State of the program after the  for loop has been executed: `i` is a tuple of two integers representing the coordinates of a snow drift, `visited` is a set containing tuples of coordinates of snow drifts that have been visited, including all tuples `(i[0], child)` where `child` is in `mydict_x[i[0]]` and `(i[0], child)` was not originally in `visited`. `mydict_x` is a dictionary where keys are x-coordinates and values are sets of y-coordinates of snow drifts sharing the same x-coordinate, and `mydict_x[i[0]]` contains all y-coordinates that were checked. `mydict_y` is a dictionary where keys are y-coordinates and values are sets of x-coordinates of snow drifts sharing the same y-coordinate. If no unvisited `child` exists in `mydict_x[i[0]]`, the loop does not execute, and `visited` remains unchanged from its initial state.
        for child in mydict_y[i[1]]:
            if (child, i[1]) not in visited:
                dfs((child, i[1]))
            
        #State of the program after the  for loop has been executed: `i` is a tuple of two integers representing the coordinates of a snow drift, `visited` is a set containing tuples of coordinates of snow drifts that have been visited. After all iterations of the loop, `visited` includes all tuples `(child, i[1])` where `child` is in `mydict_y[i[1]]` and `(child, i[1])` was not originally in `visited`. `mydict_x` is a dictionary where keys are x-coordinates and values are sets of y-coordinates of snow drifts sharing the same x-coordinate, and `mydict_y` is a dictionary where keys are y-coordinates and values are sets of x-coordinates of snow drifts sharing the same y-coordinate. If no unvisited `child` exists in `mydict_y[i[1]]`, the loop does not execute, and `visited` remains unchanged from its initial state.
    #State of the program after the if block has been executed: *`i` is a tuple of two integers representing the coordinates of a snow drift, and `visited` is a set containing tuples of coordinates of snow drifts that have been visited. If `i` is not in `visited`, then after all iterations of the loop, `visited` includes all tuples `(child, i[1])` where `child` is in `mydict_y[i[1]]` and `(child, i[1])` was not originally in `visited`. If no unvisited `child` exists in `mydict_y[i[1]]`, the loop does not execute, and `visited` remains unchanged from its initial state. If `i` is already in `visited`, `visited` remains unchanged.
#Overall this is what the function does:The `dfs` function performs a depth-first search (DFS) starting from the given snow drift coordinates `i`. It marks the current snow drift as visited by adding `i` to the `visited` set. Then, it recursively explores all connected snow drifts that share the same x-coordinate and y-coordinate, marking them as visited if they haven't been visited yet. The function modifies the `visited` set to include all reachable snow drifts from the starting point `i`. If `i` is already in `visited`, the function does nothing. The dictionaries `mydict_x` and `mydict_y` are used to efficiently find connected snow drifts. The final state of the program after the function concludes is that `visited` contains all the snow drifts that are reachable from the starting point `i`, and `i` itself is marked as visited.

