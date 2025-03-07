#State of the program right berfore the function call: n and m are integers such that 3 <= n, m <= 99 and both are odd. grid is a 2D list of strings representing the field, where each string is a pair of characters. elements is a dictionary mapping each entity (player, goal, Quaffle) to its position (row, column) on the grid. allPlayers is a dictionary mapping each player to a boolean indicating whether they are carrying the Quaffle. goal is a list of lists, where each sublist contains the positions of the goals for the respective team. points is a list of two integers representing the scores of the red and blue teams.
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
        
    #State: `n` and `m` remain the same specific odd integers, `grid` is a list of `n` lists, each containing `m` elements read from the input, `elements` is a dictionary with keys corresponding to unique elements in the grid (excluding ` '..'`) and values as tuples representing their positions, `allPlayers` is a dictionary with keys corresponding to player elements in the grid (if any) and values set to `False`, `goal` is a list containing two lists, each with tuples representing the positions of the goal elements for each team (if any), `points` remains `[0, 0]`.
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
        
    #State: The values of `n`, `m`, `grid`, `elements`, `allPlayers`, `goal`, and `points` will be modified based on the commands read from the input. Specifically:
    print('FINAL SCORE: %d %d' % (points[0], points[1]))
    #This is printed: FINAL SCORE: [points[0]] [points[1]] (where [points[0]] is the score of the first player and [points[1]] is the score of the second player)
#Overall this is what the function does:The function `func_1` reads a grid configuration and a series of commands from standard input. It initializes and updates the positions of players, the Quaffle, and goals on the grid, and tracks the scores of two teams (red and blue). The function processes each command to move players, transfer the Quaffle, score points, and handle special events like catching the Golden Snitch or eliminating players. After processing all commands, it prints the final scores of the red and blue teams. The function does not accept any parameters and does not return any value.

#State of the program right berfore the function call: pos is a tuple of integers (i, j) representing a position on the field, where 0 <= i < N and 0 <= j < M. goal is a list of two sets, where each set contains tuples of integers representing the positions of the goals for the red team (goal[0]) and the blue team (goal[1]).
def goalIn(pos):
    res = 0 if pos in goal[0] else 1 if pos in goal[1] else -1
    return res
    #The program returns 0 if pos is in the red team's goal positions, 1 if pos is in the blue team's goal positions, and -1 if pos is not in either team's goal positions.
#Overall this is what the function does:The function `goalIn` accepts a position `pos` and checks if it is in the goal positions of the red team or the blue team. It returns 0 if `pos` is in the red team's goal positions, 1 if `pos` is in the blue team's goal positions, and -1 if `pos` is not in either team's goal positions. The function does not modify any input parameters or global state.

#State of the program right berfore the function call: el is a string of length 2, where the first character is either 'B' or 'R' and the second character is a digit from '0' to '9'.
def isPlayer(el):
    res = (el[0] == 'B' or el[0] == 'R') and el[1] != 'G'
    return res
    #The program returns True.
#Overall this is what the function does:The function `isPlayer` accepts a parameter `el`, which is a string of length 2. The first character of `el` is expected to be either 'B' or 'R', and the second character is expected to be a digit from '0' to '9'. The function returns `True` if the first character is 'B' or 'R' and the second character is not 'G'. Otherwise, it returns `False`.

