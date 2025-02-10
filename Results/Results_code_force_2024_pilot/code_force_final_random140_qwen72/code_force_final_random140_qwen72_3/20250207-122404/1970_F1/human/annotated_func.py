#State of the program right berfore the function call: n and m are integers such that 3 <= n, m <= 99 and both n and m are odd.
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
        
    #State: After the loop executes all the iterations, `n` is an integer such that 3 <= n <= 99 and n is odd, `i` is `n-1`, `line` is a list of strings read from the standard input and split by spaces, `ind` is the length of `line` minus 1, `grid` contains `n` lines, each a list of strings read from the standard input. The `elements` dictionary contains keys for each non-'..' element in the entire grid, with values being tuples representing their positions (row, column). The `allPlayers` dictionary contains keys for each player element in the grid, with values set to `False`. The `goal` list contains tuples for each non-player element in the grid whose second character is 'G', with the tuples representing their positions (row, column), and `tmp` is 0 if the first character of these elements is 'B' or 1 if it is not.
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
        
    #State: After the loop executes all the iterations, the following changes occur:
    print('FINAL SCORE: %d %d' % (points[0], points[1]))
    #This is printed: FINAL SCORE: [points[0]] [points[1]] (where points[0] and points[1] are the final scores after the loop has completed all iterations)
#Overall this is what the function does:This function reads a grid of characters from the standard input, where the grid dimensions `n` and `m` are odd integers between 3 and 99. It processes the grid to identify specific elements and their positions, including players and goals. The function then simulates a series of commands over a specified number of turns, updating the state of the game based on these commands. Players can be eliminated, score points, or catch a golden snitch, which affects the game's state and scoring. After all commands are processed, the function prints the final scores for two teams. The function does not accept any parameters and does not return any values.

#State of the program right berfore the function call: pos is a tuple representing a position on the field, and goal is a list containing two sets, where the first set contains positions of the red team's goals and the second set contains positions of the blue team's goals.
def goalIn(pos):
    res = 0 if pos in goal[0] else 1 if pos in goal[1] else -1
    return res
    #The program returns 0 if `pos` is in the first set of `goal` (red team's goals), 1 if `pos` is in the second set of `goal` (blue team's goals), and -1 otherwise.
#Overall this is what the function does:The function `goalIn` takes a position `pos` and checks if it is in the red team's goals (first set in the `goal` list) or the blue team's goals (second set in the `goal` list). It returns 0 if `pos` is in the red team's goals, 1 if `pos` is in the blue team's goals, and -1 if `pos` is not in either set. The function does not modify any input parameters.

#State of the program right berfore the function call: el is a string of length 2, where the first character is either 'B' or 'R' and the second character is a digit (0-9) or 'G'.
def isPlayer(el):
    res = (el[0] == 'B' or el[0] == 'R') and el[1] != 'G'
    return res
    #The program returns `True` if the second character of `el` is a digit (0-9), and `False` if the second character of `el` is 'G'.
#Overall this is what the function does:The function `isPlayer` accepts a string `el` of length 2, where the first character is either 'B' or 'R', and the second character is either a digit (0-9) or 'G'. It returns `True` if the second character is a digit (0-9), and `False` if the second character is 'G'.

