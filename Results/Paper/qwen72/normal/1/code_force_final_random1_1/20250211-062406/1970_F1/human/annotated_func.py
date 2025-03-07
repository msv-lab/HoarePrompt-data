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
        
    #State: After the loop executes all iterations, `n` and `m` remain integers read from input and satisfy the conditions 3 <= n, m <= 99 and both `n` and `m` are odd. `grid` is a list containing `n` elements, where each element is a list of strings read from the input, representing the rows of the grid. `elements` is a dictionary that contains entries for each unique non-'..' string in the entire grid, with the key being the string and the value being a tuple (i, ind) where `i` is the row index and `ind` is the column index of the string in the grid. `allPlayers` is a dictionary that contains entries for each player string (as determined by the `isPlayer` function) found in the grid, with the key being the player string and the value being `False`. `goal` is a list containing two lists: the first list contains tuples (i, ind) for each string in the grid that ends with 'G' and starts with 'B', and the second list contains tuples (i, ind) for each string in the grid that ends with 'G' and starts with 'R'. `points` remains a list `[0, 0]`. `i` is `n-1`. `line` is the last list of strings read from the input and has `m` elements. `ind` is `m-1`. If `line[ind]` is not '..': `elements` includes an entry for `line[ind]` which is `(n-1, m-1)`. If `isPlayer(line[ind])` is true, `allPlayers[line[ind]]` is set to `False`. Otherwise, if `line[ind][1]` is 'G', `tmp` is 0 if `line[ind][0]` is 'B', otherwise `tmp` is 1, and `goal[tmp]` now includes the tuple `(n-1, m-1)`. If `line[ind]` is '..': no changes are made to any variables.
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
        
    #State: After the loop executes all iterations, `t` is 0, `time` is `t-1`, `command` is the last list of strings read from standard input during the final iteration. The values of `allPlayers`, `team`, `points`, `mov`, `grid`, and `player` may have changed based on the commands processed during the loop. Specifically, `allPlayers` may have some keys set to `True` if the command was `.Q`, `points` may have been incremented by 10 for the respective team if the command was `.S`, and positions of players and the ball (`.B`) may have been updated based on movement commands. Any eliminations or goals scored will have been printed to the console.
    print('FINAL SCORE: %d %d' % (points[0], points[1]))
    #This is printed: FINAL SCORE: [points[0]] [points[1]] (where [points[0]] and [points[1]] are the final scores for the two teams after all commands have been processed)
#Overall this is what the function does:This function reads a grid and a series of commands from standard input to simulate a game. It initializes a grid of size `n x m` (where `n` and `m` are odd integers between 3 and 99) and populates it with elements, tracking their positions. It also tracks players, goals, and points for two teams. The function processes `t` commands, updating the game state accordingly, including moving players, scoring goals, catching the golden snitch, and eliminating players. The final scores for both teams are printed at the end.

#State of the program right berfore the function call: pos is a tuple representing a position on the field, and goal is a list containing two sets of tuples, where the first set represents the positions of the red team's goals and the second set represents the positions of the blue team's goals.
def goalIn(pos):
    res = 0 if pos in goal[0] else 1 if pos in goal[1] else -1
    return res
    #The program returns 0 if `pos` is in `goal[0]`, 1 if `pos` is in `goal[1]`, and -1 otherwise.
#Overall this is what the function does:The function `goalIn` takes a position `pos` and determines whether this position is within the goal areas of either the red team or the blue team. It returns 0 if `pos` is in the red team's goal area, 1 if `pos` is in the blue team's goal area, and -1 if `pos` is not in any goal area. The function does not modify any input parameters.

#State of the program right berfore the function call: el is a string of length 2, where the first character is either 'B' or 'R' and the second character is a digit from '0' to '9'.
def isPlayer(el):
    res = (el[0] == 'B' or el[0] == 'R') and el[1] != 'G'
    return res
    #The program returns True.
#Overall this is what the function does:The function `isPlayer` accepts a parameter `el`, which is expected to be a string of length 2. The first character of `el` should be either 'B' or 'R', and the second character should be a digit from '0' to '9'. The function returns `True` if the first character is 'B' or 'R' and the second character is not 'G'. Otherwise, it returns `False`.

