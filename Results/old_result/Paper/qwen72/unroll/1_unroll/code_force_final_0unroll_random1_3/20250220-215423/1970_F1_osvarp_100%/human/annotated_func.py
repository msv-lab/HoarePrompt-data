#State of the program right berfore the function call: n and m are integers such that 3 <= n, m <= 99 and both n and m are odd.
def func_1():
    n, m = map(int, stdin.readline().strip().split())
    grid = []
    elements = {'.B': (-1, -1)}
    allPlayers = {}
    goal = [[], []]
    points = [0, 0]
    for i in range(n):
        line = stdin.readline().strip().split()
        
        grid.append(line)
        
        for ind in range(len(line)):
            if line[ind] != '..':
                elements[line[ind]] = i, ind
                if isPlayer(line[ind]):
                    allPlayers[line[ind]] = False
                elif line[ind][1] == 'G':
                    tmp = 0 if line[ind][0] == 'B' else 1
                    goal[tmp].append((i, ind))
        
    #State: `n` and `m` remain the same as their initial values; `grid` is a list of `n` lists, each containing `m` elements read from the input; `elements` is a dictionary that now contains the positions of all non-`'..'` elements in the grid, with the key being the element and the value being a tuple (row, column); `allPlayers` is a dictionary that contains all player elements (as determined by the `isPlayer` function) with the value `False`; `goal` is a list containing two lists, each with the positions of the goals for the respective players (0 for 'B' and 1 for 'R'). `points` remains [0, 0].
    t = int(stdin.readline().strip())
    for time in range(t):
        comand = stdin.readline().strip().split()
        
        if len(comand) == 3:
            obj, com, el = comand
            if el == '.Q':
                allPlayers[obj] = True
            elif el == '.S':
                team = 1 if obj[0] == 'B' else 0
                points[team] += 10
                print('%d %s CATCH GOLDEN SNITCH' % (time, GoalName[team]))
        else:
            obj, com = comand
            pos = elements[obj]
            nxt = pos[0] + mov[com][0], pos[1] + mov[com][1]
            if obj == '.B' and isPlayer(grid[nxt[0]][nxt[1]]) or isPlayer(obj
                ) and elements['.B'] == nxt:
                player = obj if isPlayer(obj) else grid[nxt[0]][nxt[1]]
                print('%d %s ELIMINATED' % (time, player))
            elif com == 'T':
                allPlayers[obj] = False
                if goalIn(pos) != -1:
                    team = goalIn(pos)
                    print('%d %s GOAL' % (time, GoalName[team]))
                    points[team] += 1
            elif isPlayer(obj):
                elements[obj] = nxt
            if obj == '.B':
                elements[obj] = nxt
        
    #State: The values of `n`, `m`, `grid`, `elements`, `allPlayers`, `goal`, and `t` remain unchanged. The `points` list will be updated based on the goals scored and the golden snitches caught during the loop execution. The `allPlayers` dictionary will be updated to reflect the active status of players after each command. The `elements` dictionary will be updated to reflect the new positions of the players and the bludger (`.B`) after each move command.
    print('FINAL SCORE: %d %d' % (points[0], points[1]))
    #This is printed: FINAL SCORE: [points[0]] [points[1]] (where points[0] and points[1] are the final scores of the two teams, updated based on goals scored and golden snitches caught during the loop execution)
#Overall this is what the function does:The function reads a grid of size `n` x `m` from the standard input, where `n` and `m` are predefined odd integers within the range of 3 to 99. It initializes a dictionary `elements` to store the positions of all non-`'..'` elements in the grid, a dictionary `allPlayers` to track the active status of players, and a list `goal` to store the positions of goals for two teams. The function then reads a number `t` indicating the number of commands to process. For each command, it updates the state of the game, including moving players and the bludger (`.B`), scoring points, and handling special commands like catching the golden snitch (`.S`) and eliminating players. After processing all commands, the function prints the final scores of the two teams. The function does not return any value but modifies the `points` list and the `allPlayers` and `elements` dictionaries as a result of the commands.

#State of the program right berfore the function call: pos is a tuple of integers (x, y) representing a position on the field, and goal is a list of two sets where each set contains tuples of integers representing the positions of the goals for the red and blue teams, respectively.
def goalIn(pos):
    res = 0 if pos in goal[0] else 1 if pos in goal[1] else -1
    return res
    #The program returns 0 if `pos` is in the set of red team goals, 1 if `pos` is in the set of blue team goals, and -1 otherwise.
#Overall this is what the function does:The function `goalIn` accepts a parameter `pos` (a tuple of integers) and a parameter `goal` (a list containing two sets of tuples). It returns 0 if `pos` is in the set of red team goals (the first set in the list), 1 if `pos` is in the set of blue team goals (the second set in the list), and -1 if `pos` is not in either set.

#State of the program right berfore the function call: el is a string of length 2, where the first character is either 'B' or 'R' and the second character is a digit from '0' to '9' or 'G'.
def isPlayer(el):
    res = (el[0] == 'B' or el[0] == 'R') and el[1] != 'G'
    return res
    #The program returns True if the first character of the string 'el' is 'B' or 'R' and the second character is not 'G', otherwise it returns False.
#Overall this is what the function does:The function `isPlayer` accepts a string `el` of length 2, where the first character is either 'B' or 'R' and the second character is a digit from '0' to '9' or 'G'. It returns `True` if the first character is 'B' or 'R' and the second character is not 'G'. Otherwise, it returns `False`.

