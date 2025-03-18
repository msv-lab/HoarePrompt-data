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
        
    #State: `grid` is a list of `n` lists, each containing `m` elements read from the input. `elements` is a dictionary that maps each unique element in the grid (except '..') to its coordinates (row, column). `allPlayers` is a dictionary that maps each player element in the grid to `False`. `goal` is a list containing two lists, each with the coordinates of the 'BG' and 'WG' elements, respectively. `points` remains [0, 0].
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
        
    #State: The `grid` remains a list of `n` lists, each containing `m` elements read from the input. The `elements` dictionary is updated to reflect the final positions of all players and the Quaffle ('.B') after the loop executes. The `allPlayers` dictionary is updated to reflect the final state (True or False) of each player after the loop executes. The `goal` list remains unchanged, containing the coordinates of the 'BG' and 'WG' elements. The `points` list is updated to reflect the final score of each team after the loop executes.
    print('FINAL SCORE: %d %d' % (points[0], points[1]))
    #This is printed: FINAL SCORE: [points[0]] [points[1]] (where points[0] is the final score of the Blue team and points[1] is the final score of the White team)
#Overall this is what the function does:The function reads a grid of size `n` x `m` from the input, where `n` and `m` are odd integers between 3 and 99. It processes a series of commands over `t` time steps, updating the positions of players and the Quaffle ('.B') on the grid, and tracking the elimination of players, goals scored, and the capture of the Golden Snitch. The function maintains a score for two teams (Blue and White) and prints the final score at the end. The `grid` remains unchanged, `elements` reflects the final positions of all players and the Quaffle, `allPlayers` reflects the final state of each player, `goal` retains the coordinates of the 'BG' and 'WG' elements, and `points` contains the final scores of both teams.

#State of the program right berfore the function call: pos is a tuple of integers (i, j) representing a position on the field, and goal is a list of two sets where goal[0] contains the positions of the red goals and goal[1] contains the positions of the blue goals.
def goalIn(pos):
    res = 0 if pos in goal[0] else 1 if pos in goal[1] else -1
    return res
    #The program returns 0 if `pos` is in the set of red goals (`goal[0]`), 1 if `pos` is in the set of blue goals (`goal[1]`), and -1 otherwise.
#Overall this is what the function does:The function `goalIn` accepts a position `pos` (a tuple of integers) and a list `goal` containing two sets: `goal[0]` for red goals and `goal[1]` for blue goals. It returns 0 if `pos` is in the set of red goals, 1 if `pos` is in the set of blue goals, and -1 if `pos` is not in either set.

#State of the program right berfore the function call: el is a string of length 2, where the first character is either 'B' or 'R' and the second character is a digit from '0' to '9' or 'G'.
def isPlayer(el):
    res = (el[0] == 'B' or el[0] == 'R') and el[1] != 'G'
    return res
    #The program returns `True` if the first character of `el` is 'B' or 'R' and the second character is not 'G', otherwise it returns `False`.
#Overall this is what the function does:The function `isPlayer` accepts a string `el` of length 2, where the first character is either 'B' or 'R' and the second character is a digit from '0' to '9' or 'G'. It returns `True` if the first character is 'B' or 'R' and the second character is not 'G'. Otherwise, it returns `False`.

