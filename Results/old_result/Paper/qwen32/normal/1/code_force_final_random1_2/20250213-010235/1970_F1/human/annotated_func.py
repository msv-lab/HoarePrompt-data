#State of the program right berfore the function call: n and m are integers representing the dimensions of the grid (N lines and M columns), where 3 <= n <= 99 and 3 <= m <= 99. grid is a 2D list of strings representing the field, where each string is either '..' for an empty cell, 'R0', ..., 'R9', 'B0', ..., 'B9' for players, 'RG' or 'BG' for goals, or '.Q' for the Quaffle. elements is a dictionary mapping entity identifiers to their positions on the grid. allPlayers is a dictionary mapping player identifiers to a boolean indicating whether they are carrying the Quaffle. goal is a list of lists, where goal[0] contains tuples representing the positions of blue goals and goal[1] contains tuples representing the positions of red goals. points is a list of two integers representing the scores of the blue and red teams, respectively.
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
        
    #State: `n` is an integer representing the number of lines in the grid, `m` is an integer representing the number of columns in the grid, `grid` is a list of `n` elements where each element is a list of strings representing the grid's rows, `elements` is a dictionary mapping each non-'..' element to its position, `allPlayers` is a dictionary mapping each player identifier to `False`, `goal` is a list of two lists where the first list contains positions of blue goals and the second list contains positions of red goals, and `points` is `[0, 0]`.
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
        
    #State: `n` is unchanged, `m` is unchanged, `grid` is unchanged unless modified by commands, `elements` reflects final positions, `allPlayers` reflects active players, `goal` is unchanged, `points` reflects accumulated points, `t` is unchanged.
    print('FINAL SCORE: %d %d' % (points[0], points[1]))
    #This is printed: FINAL SCORE: points[0] points[1] (where points[0] is the accumulated points for the first player and points[1] is the accumulated points for the second player)
#Overall this is what the function does:The function processes a series of commands to update the state of a Quidditch-like game on a grid, modifying player positions, handling Quaffle possession, scoring goals, and eliminating players. It outputs the final scores of the blue and red teams after processing all commands.

#State of the program right berfore the function call: pos is a tuple representing a position on the field, goal is a list of two lists where each sublist contains tuples representing the positions of the goals for the red and blue teams respectively.
def goalIn(pos):
    res = 0 if pos in goal[0] else 1 if pos in goal[1] else -1
    return res
    #The program returns `res`, which is 0 if `pos` is in `goal[0]`, 1 if `pos` is in `goal[1]`, otherwise -1.
#Overall this is what the function does:The function determines whether a given position `pos` is within the goal areas of either the red or blue team. It returns 0 if `pos` is in the red team's goal area, 1 if `pos` is in the blue team's goal area, and -1 if `pos` is not in either goal area.

#State of the program right berfore the function call: el is a string representing an entity on the field, where el[0] is either 'B' or 'R' indicating the team (Blue or Red), and el[1] is a character that is not 'G', indicating it is a player (and not a goal).
def isPlayer(el):
    res = (el[0] == 'B' or el[0] == 'R') and el[1] != 'G'
    return res
    #The program returns True
#Overall this is what the function does:The function checks if the given string `el` represents a player on the field by verifying that the first character is either 'B' or 'R' and the second character is not 'G'. It returns `True` if these conditions are met, otherwise it returns `False`.

