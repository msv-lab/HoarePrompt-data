#State of the program right berfore the function call: n and m are integers representing the dimensions of the field such that 3 <= n, m <= 99 and both are odd. grid is a 2D list of strings representing the field where each string is either '..' for an empty cell, 'R0', ..., 'R9', 'B0', ..., 'B9' for players, 'RG' or 'BG' for goals, or '.Q' for the Quaffle. elements is a dictionary mapping entity identifiers to their positions on the grid. allPlayers is a dictionary mapping player identifiers to a boolean indicating whether they are carrying the Quaffle. goal is a list of lists where each sublist contains tuples representing the positions of the goals for each team. points is a list of two integers representing the scores of the blue and red teams respectively.
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
        
    #State: `n` and `m` are integers representing the dimensions of the field such that 3 <= n, m <= 99 and both are odd; `grid` is a list containing `n` elements, each of which is a `line` list read from the input; `elements` is a dictionary mapping entity identifiers to their positions on the grid, including all non-'..' elements in the input; `allPlayers` is a dictionary with `allPlayers[line[ind]] = False` for all player entities in the input; `goal` is a list of two lists, where each list contains tuples of positions of goals for the blue and red teams respectively, and if `line[ind]` is not a player and its second character is 'G', then `goal[tmp]` includes the tuple `(i, ind)` where `tmp` is 0 if `line[ind]` is 'BG', otherwise `tmp` is 1; `points` is a list of two integers representing the scores of the blue and red teams respectively, with `points = [0, 0]`.
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
        
    #State: `n` and `m` are integers representing the dimensions of the field such that 3 <= n, m <= 99 and both are odd; `grid` is a list containing `n` elements, each of which is a `line` list read from the input; `elements` is a dictionary mapping entity identifiers to their final positions on the grid; `allPlayers` is a dictionary indicating the final active status of all players; `goal` is a list of two lists, where each list contains tuples of positions of goals for the blue and red teams respectively; `points` is a list of two integers representing the final scores of the blue and red teams respectively; `t` is an integer read from the input.
    print('FINAL SCORE: %d %d' % (points[0], points[1]))
    #This is printed: FINAL SCORE: [points[0]] [points[1]] (where points[0] is the final score of the blue team and points[1] is the final score of the red team)
#Overall this is what the function does:The function reads the dimensions and initial state of a Quidditch field, processes a series of commands affecting players and the Quaffle, and updates the scores based on goals and the capture of the Golden Snitch. It outputs the final scores of the blue and red teams.

#State of the program right berfore the function call: pos is a tuple representing a position on the field, goal is a list of two sets where goal[0] contains positions of red goals and goal[1] contains positions of blue goals.
def goalIn(pos):
    res = 0 if pos in goal[0] else 1 if pos in goal[1] else -1
    return res
    #The program returns res, which is 0 if pos is in goal[0], 1 if pos is in goal[1], otherwise -1.
#Overall this is what the function does:The function `goalIn` determines whether a given position `pos` is in the set of red goals (`goal[0]`) or blue goals (`goal[1]`). It returns 0 if `pos` is a red goal, 1 if `pos` is a blue goal, and -1 if `pos` is neither.

#State of the program right berfore the function call: el is a string of length 2, where the first character is either 'B' or 'R' and the second character is not 'G'.
def isPlayer(el):
    res = (el[0] == 'B' or el[0] == 'R') and el[1] != 'G'
    return res
    #The program returns True
#Overall this is what the function does:The function checks if the input string `el` has its first character as either 'B' or 'R' and its second character not as 'G', returning `True` if both conditions are met.

