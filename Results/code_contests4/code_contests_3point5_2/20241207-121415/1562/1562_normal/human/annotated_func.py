#State of the program right berfore the function call: **
def func_1(y, x):
    if (0 <= y <= 11 and 0 <= x <= 11) :
        return True
        #The program returns True
    #State of the program after the if block has been executed: y and x are integers. Either y is outside the range of 0 to 11 or x is outside the range of 0 to 11
    return False
    #The program returns False
#Overall this is what the function does:The function `func_1` accepts two parameters `y` and `x`. It returns True if both `y` and `x` are within the range of 0 to 11 inclusive. Otherwise, it returns False. The function checks if `y` and `x` are within the specified range and returns the corresponding boolean value.

#State of the program right berfore the function call: Each dataset consists of a 12x12 grid of 0s and 1s representing the plan view, where 1 represents a black square and 0 represents a white square.**
def func_2(y, x):
    if (g[y][x] == '0') :
        return 0
        #The program returns 0 when the value at position (x, y) in the 12x12 grid is '0'
    #State of the program after the if block has been executed: *The 12x12 grid consists of 0s and 1s representing the plan view. If (g[y][x] != '0'), then the value at position (y,x) in the grid is not equal to '0'.
    g[y][x] = '0'
    for i in xrange(4):
        nexty = y + dy[i]
        
        nextx = x + dx[i]
        
        if not func_1(nexty, nextx):
            continue
        
        if visited[nexty][nextx] == 0 and g[nexty][nextx] == '1':
            visited[nexty][nextx] = 1
            func_2(nexty, nextx)
        
    #State of the program after the  for loop has been executed: The 12x12 grid consists of 0s and 1s representing the plan view. If the loop executes, all positions in the grid that are reachable from the starting position (y, x) and contain '1' are marked as visited.
    return 1
    #The program returns 1
#Overall this is what the function does:The function `func_2` accepts two parameters `y` and `x`, representing coordinates in a 12x12 grid of 0s and 1s. If the value at position (x, y) in the grid is '0', the function returns 0. Otherwise, it marks all reachable positions containing '1' as visited and returns 1.

