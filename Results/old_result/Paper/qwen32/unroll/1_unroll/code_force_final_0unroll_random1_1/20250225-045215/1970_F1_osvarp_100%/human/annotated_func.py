#State of the program right berfore the function call: n and m are integers representing the dimensions of the grid such that 3 <= n, m <= 99 and both are odd. grid is a 2D list of strings of size n x m representing the field. elements is a dictionary mapping strings to tuples of integers representing positions on the grid. allPlayers is a dictionary mapping player identifiers to boolean values indicating if they are carrying the Quaffle. goal is a list of lists of tuples of integers representing the positions of the goals for each team. points is a list of two integers representing the scores of the red and blue teams.
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
        
    #State: `n` and `m` are integers read from the input representing the dimensions of the grid such that 3 <= n, m <= 99 and both are odd; `grid` is a list of `n` lines, where each line is a list of `m` strings read from the input; `elements` is a dictionary mapping strings to tuples of integers representing positions on the grid, where each key is a non-'..' string from the grid and its value is the corresponding position (i, ind); `allPlayers` is a dictionary containing keys that are player identifiers (strings from the grid for which `isPlayer(line[ind])` is True) with values set to False; `goal` is a list of two lists, where the first list contains positions (i, ind) of all 'BG' strings from the grid and the second list contains positions of all 'RG' strings from the grid; `points` is a list of two integers representing the scores of the red and blue teams, where `points` is now `[0, 0]`.
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
        
    #State: `points` is a list of two integers representing the final scores of the red and blue teams; `allPlayers` is a dictionary indicating the active status of each player; `elements` is a dictionary with the final positions of all players and the bludger `.B`.
    print('FINAL SCORE: %d %d' % (points[0], points[1]))
    #This is printed: FINAL SCORE: [points[0]] [points[1]] (where points[0] is the score of the red team and points[1] is the score of the blue team)
#Overall this is what the function does:The function processes a series of commands to simulate a game on a grid. It updates the positions of players and the bludger, manages the Quaffle carrier status, scores goals, and eliminates players. The final output is the final scores of the red and blue teams after all commands have been processed.

#State of the program right berfore the function call: pos is a tuple representing a position on the field, and goal is a list of two lists where each inner list contains positions of goals for the red and blue teams respectively.
def goalIn(pos):
    res = 0 if pos in goal[0] else 1 if pos in goal[1] else -1
    return res
    #The program returns res, which is 0 if pos is in goal[0], 1 if pos is in goal[1], otherwise -1.
#Overall this is what the function does:The function determines whether a given position is a goal for the red team, the blue team, or neither, and returns 0, 1, or -1 respectively.

#State of the program right berfore the function call: el is a string of length 2, where the first character is either 'B' or 'R' and the second character is not 'G'.
def isPlayer(el):
    res = (el[0] == 'B' or el[0] == 'R') and el[1] != 'G'
    return res
    #The program returns True
#Overall this is what the function does:The function checks if the input string `el` meets the condition where the first character is either 'B' or 'R' and the second character is not 'G'. It returns `True` if the condition is met, otherwise it returns `False`.

