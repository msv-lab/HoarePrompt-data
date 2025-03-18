#State of the program right berfore the function call: n and m are integers such that 3 ≤ n, m ≤ 99 and both are odd. grid is a 2D list of strings representing the field, where each string contains M characters and there are N such strings. elements is a dictionary mapping entities on the field to their coordinates, allPlayers is a dictionary mapping players to whether they are carrying the Quaffle, goal is a list of two lists, each containing tuples representing the coordinates of the goals for the red and blue teams respectively, and points is a list of two integers representing the current scores of the red and blue teams.
def func_1():
    n, m = map(int, stdin.readline().strip().split())
    grid = []
    elements = {'.B': (0, 0)}
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
        
    #State: After the loop executes all iterations, the grid will be fully populated with lines read from standard input, and the following conditions will be met:
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
        
    #State: After the loop executes all iterations, `t` will be the total number of iterations, `time` will be equal to `t-1`, and `command` will be the last command read from stdin and stripped/split. If any command included `.Q`, `allPlayers[obj]` will be set to `True` for the corresponding object. If any command included `.S`, `team` will be 1 if `obj[0]` is 'B' else 0, and `points[team]` will be incremented by 10. For commands without `.Q` or `.S`, if `obj` is a player and `com` is 'T', `allPlayers[obj]` will be set to `False` and `points[team]` will be incremented by 1 if `goalIn(pos)` is not -1. The positions of all objects will be updated according to the movement commands.
    print('FINAL SCORE: %d %d' % (points[0], points[1]))
    #This is printed: FINAL SCORE: points[0] points[1]
#Overall this is what the function does:The function reads a game field configuration and a series of commands from standard input. It updates the game state based on these commands, including moving players and objects, updating scores when a golden snitch is caught or a goal is scored, and handling player eliminations. Finally, it prints the final scores of the red and blue teams.

#State of the program right berfore the function call: pos is a string representing a position on the field, where the position is one of the characters 'R0' to 'R9', 'B0' to 'B9', 'RG', 'BG', or '.Q'. The function determines whether the given position is a goal for the red team (returning 0), the blue team (returning 1), or neither (returning -1).
def goalIn(pos):
    res = 0 if pos in goal[0] else 1 if pos in goal[1] else -1
    return res
    #The program returns res which is 0 if pos is in goal[0], 1 if pos is in goal[1], and -1 otherwise.
#Overall this is what the function does:The function `goalIn` accepts a string `pos` representing a position on the field and returns 0 if `pos` is a goal for the red team, 1 if `pos` is a goal for the blue team, and -1 if `pos` is neither a goal for the red nor the blue team.

#State of the program right berfore the function call: el is a string representing an entity on the field, where the first character is the team (either 'R' for Red or 'B' for Blue) and the second character is additional information (e.g., player number or 'G' for goal).
def isPlayer(el):
    res = (el[0] == 'B' or el[0] == 'R') and el[1] != 'G'
    return res
    #The program returns a boolean value 'res' which is True if the first character of 'el' is 'B' and the second character is not 'G', and False otherwise.
#Overall this is what the function does:The function `isPlayer` accepts a string `el` and returns `True` if the first character is 'B' (indicating Blue) and the second character is not 'G' (indicating a goal), otherwise it returns `False`.

