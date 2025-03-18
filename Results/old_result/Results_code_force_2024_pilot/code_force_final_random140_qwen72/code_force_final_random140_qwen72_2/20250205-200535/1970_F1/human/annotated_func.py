#State of the program right berfore the function call: n and m are integers such that 3 <= n, m <= 99 and both are odd. grid is a list of n lists, each containing m pairs of characters representing the field. elements is a dictionary mapping pairs of characters to their positions (i, ind) on the grid. allPlayers is a dictionary mapping player identifiers to a boolean indicating whether they are currently carrying the Quaffle. goal is a list of two lists, each containing tuples of positions (i, ind) of the goals for the respective team. points is a list of two integers representing the scores of the red and blue teams.
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
        
    #State: After the loop executes all iterations, `i` is `n`, `n` and `m` remain integers such that 3 <= n, m <= 99 and both are odd. `grid` is a list containing `n` elements, each element being a list of strings read from the input. `elements` is a dictionary that includes keys for each non-'..' element found in any of the lines, with their corresponding indices as tuples (row, column). `points` remains [0, 0]. `allPlayers` is a dictionary that contains keys for each player character found in any of the lines, each mapped to `False`. `goal` is a list containing two lists, where each sublist contains tuples representing the positions of 'G' characters found in any of the lines, with the first sublist for 'B' characters and the second sublist for 'R' characters. `ind` is the last index processed in the final iteration, which is `m - 1`.
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
        
    #State: After the loop executes all iterations, `time` is `t - 1`, `command` is the last list of strings read from standard input during the final iteration. If `len(command) == 3`, `obj` is the first element of `command`, `com` is the second element of `command`, and `el` is the third element of `command`. If `el == '.Q'`, `allPlayers[obj]` is `True`. If `el == '.S'`, `team` is 1 if `obj[0]` is 'B', otherwise `team` is 0, and `points[team]` is increased by 10. If `len(command) != 3`, `pos` is the value of `elements[obj]`, and `nxt` is (`pos[0] + mov[com][0]`, `pos[1] + mov[com][1]`). If `obj == '.B' and (isPlayer(grid[nxt[0]][nxt[1]]) or (isPlayer(obj) and elements['.B'] == nxt))`, `player` is `obj` if `isPlayer(obj)` returns `True`, otherwise `player` is `grid[nxt[0]][nxt[1]]`. If `obj == '.B' and com == 'T'`, `allPlayers[obj]` is `False`. If `obj == '.B' and goalIn(pos)` is not -1, `team` is the result of `goalIn(pos)`, and `points[team]` is incremented by 1. If `obj == '.B' and com is not 'T' and isPlayer(obj)` is true, `elements[obj]` is updated to `nxt`. The values of `n`, `m`, `grid`, `elements`, `points`, `allPlayers`, `goal`, `ind`, and `t` remain unchanged.
    print('FINAL SCORE: %d %d' % (points[0], points[1]))
    #This is printed: FINAL SCORE: [points[0]] [points[1]] (where points[0] and points[1] are the final scores of the two teams after all iterations and conditions have been applied)
#Overall this is what the function does:The function `func_1` reads and processes a series of inputs to simulate a Quidditch match. It initializes the game state with a grid representing the playing field, a dictionary mapping character pairs to their positions, a dictionary tracking which players are carrying the Quaffle, lists of goal positions for both teams, and the initial scores of both teams set to zero. The function then processes a series of commands over a specified number of turns. Each command can either update the position of a player, transfer the Quaffle, score points, or end the game with a special event like catching the Golden Snitch. After processing all commands, the function prints the final scores of the red and blue teams. The function does not return any value but modifies and uses the game state internally.

#State of the program right berfore the function call: pos is a tuple representing a position on the field, and goal is a list containing two sets where the first set represents the positions of the red team's goals and the second set represents the positions of the blue team's goals.
def goalIn(pos):
    res = 0 if pos in goal[0] else 1 if pos in goal[1] else -1
    return res
    #The program returns 0 if `pos` is in the first set of `goal` (representing the red team's goals), 1 if `pos` is in the second set of `goal` (representing the blue team's goals), and -1 otherwise.
#Overall this is what the function does:The function `goalIn` accepts a tuple `pos` and checks if this position is in one of the two sets within the list `goal`. The first set represents the red team's goals, and the second set represents the blue team's goals. The function returns 0 if `pos` is in the red team's goals, 1 if `pos` is in the blue team's goals, and -1 if `pos` is not in either set.

#State of the program right berfore the function call: el is a string of length 2, where the first character is either 'B' or 'R', and the second character is a digit (0-9) or 'G'.
def isPlayer(el):
    res = (el[0] == 'B' or el[0] == 'R') and el[1] != 'G'
    return res
    #The program returns `True` if the second character of `el` is a digit (0-9), and `False` if the second character of `el` is 'G'.
#Overall this is what the function does:The function `isPlayer` accepts a string `el` of length 2, where the first character is either 'B' or 'R', and the second character is a digit (0-9) or 'G'. It returns `True` if the second character of `el` is a digit (0-9), and `False` if the second character is 'G'.

