#State of the program right berfore the function call: **Precondition**: **y is an integer representing the number of rows in the plan view, and x is an integer representing the number of columns in the plan view.**
def func_1(y, x):
    if (0 <= y <= 11 and 0 <= x <= 11) :
        return True
        #The program returns True
    #State of the program after the if block has been executed: y is an integer representing the number of rows in the plan view, and x is an integer representing the number of columns in the plan view. y is not in the range from 0 to 11 or x is not in the range from 0 to 11
    return False
    #The program returns False
#Overall this is what the function does:The function `func_1` accepts two integer parameters `y` and `x`, representing the number of rows and columns in the plan view, respectively. It returns True if both `y` and `x` are within the range of 0 to 11, otherwise it returns False. The function covers the cases where `y` and `x` are outside the specified range as well, where it should potentially handle those cases.

#State of the program right berfore the function call: y and x are integers such that 0 <= y < 12 and 0 <= x < 12.**
def func_2(y, x):
    if (g[y][x] == '0') :
        return 0
        #The program returns 0
    #State of the program after the if block has been executed: *y and x are integers such that 0 <= y < 12 and 0 <= x < 12. The value of g[y][x] is not '0'
    g[y][x] = '0'
    for i in xrange(4):
        nexty = y + dy[i]
        
        nextx = x + dx[i]
        
        if not func_1(nexty, nextx):
            continue
        
        if visited[nexty][nextx] == 0 and g[nexty][nextx] == '1':
            visited[nexty][nextx] = 1
            func_2(nexty, nextx)
        
    #State of the program after the  for loop has been executed: `g[y][x]` is '0', all cells in `visited` that were set to 1 by the loop are still 1, `i` is 3, `nexty` and `nextx` are the final values after the last iteration, `g[nexty][nextx]` is the value of `g` at the final `(nexty, nextx)` coordinates.
    return 1
    #The program returns 1
#Overall this is what the function does:The function `func_2` accepts two parameters `y` and `x`, both integers such that 0 <= y < 12 and 0 <= x < 12. If `g[y][x]` is '0', the function returns 0. Otherwise, it sets `g[y][x]` to '0' and iterates through neighboring cells based on predefined directions. It recursively calls itself for cells meeting specific conditions. The function returns 1 at the end. The functionality of the function is to manipulate a grid `g` based on certain conditions and return either 0 or 1.

