#State of the program right berfore the function call: n and m are integers representing the dimensions of the field such that 3 <= n, m <= 99 and both are odd. grid is a 2D list of strings representing the field where each string is either '..' for an empty cell, 'R0' to 'R9' or 'B0' to 'B9' for players, 'RG' or 'BG' for goals, or '.Q' for the Quaffle. elements is a dictionary mapping entity identifiers to their positions on the grid. allPlayers is a dictionary mapping player identifiers to a boolean indicating whether they are carrying the Quaffle. goal is a list of lists where goal[0] contains the positions of blue team goals and goal[1] contains the positions of red team goals. points is a list of two integers representing the scores of the blue and red teams respectively. t is an integer representing the number of steps in the game. comand is a list of strings representing a command where the first element is the entity performing the action, the second element is the action, and if the action is 'C', the third element is the ball being caught.
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
        
    #State: `n` and `m` are the integers read from the input, representing the dimensions of the field; `grid` is a list of lists representing the parsed input lines; `elements` is a dictionary mapping entity identifiers to their positions on the grid, including any players and goals; `allPlayers` is a dictionary mapping player identifiers to a boolean indicating whether they are carrying the Quaffle, initialized to `False` for each player; `goal` is a list of lists where `goal[0]` contains the positions of blue team goals and `goal[1]` contains the positions of red team goals, categorized based on the input; `points` is `[0, 0]`; `t` is an integer representing the number of steps in the game; `command` is a list of strings representing a command where the first element is the entity performing the action, the second element is the action, and if the action is 'C', the third element is the ball being caught.`
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
        
    #State: `n`, `m`, `grid` (with updated entity positions), `elements` (with updated positions), `allPlayers` (with updated Quaffle carrying status), `goal`, `points` (with updated scores), `t`
    print('FINAL SCORE: %d %d' % (points[0], points[1]))
    #This is printed: FINAL SCORE: [points[0]] [points[1]] (where points[0] is the score of the first team and points[1] is the score of the second team)
#Overall this is what the function does:The function processes a series of commands to simulate a game on a field, updating the positions of entities, handling Quaffle catches, scoring goals, and eliminating players. It outputs the final scores of the blue and red teams after all commands have been executed.

#State of the program right berfore the function call: pos is a tuple representing a position on the field, and goal is a list of two lists where each sublist contains positions of goals for one team.
def goalIn(pos):
    res = 0 if pos in goal[0] else 1 if pos in goal[1] else -1
    return res
    #The program returns `res`, which is 0 if `pos` is in `goal[0]`, 1 if `pos` is in `goal[1]`, and -1 if `pos` is in neither `goal[0]` nor `goal[1]`.
#Overall this is what the function does:The function checks if a given position `pos` is within the goal areas of two teams represented by `goal[0]` and `goal[1]`. It returns `0` if `pos` is in `goal[0]`, `1` if `pos` is in `goal[1]`, and `-1` if `pos` is not in either goal area.

#State of the program right berfore the function call: el is a string of length 2, where the first character is either 'B' or 'R' and the second character is not 'G'.
def isPlayer(el):
    res = (el[0] == 'B' or el[0] == 'R') and el[1] != 'G'
    return res
    #The program returns True
#Overall this is what the function does:The function checks if the input string `el` of length 2 starts with either 'B' or 'R' and does not end with 'G'. It returns `True` if both conditions are met; otherwise, it returns `False`.

