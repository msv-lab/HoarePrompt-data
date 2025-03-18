#State of the program right berfore the function call: (n, m) are positive integers such that 3 ≤ n, m ≤ 99 and both are odd. grid is a 2D list of strings representing the field, where each string is a row of the field and contains characters like '..', 'R0', 'B0', '.Q', 'RG', 'BG'. elements is a dictionary mapping entities on the field to their positions (row, column) as tuples. allPlayers is a dictionary mapping player entities to a boolean indicating whether they are carrying the Quaffle. goal is a list of two lists, where each sublist contains the positions of goals for the respective team. points is a list of two integers representing the current scores of the red and blue teams.
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
        
    #State: grid is a list of n lists, each containing m elements read from the standard input. The elements dictionary contains keys for all non-empty cells in the grid, mapping to their coordinates (i, ind). The allPlayers dictionary contains keys for all cells marked with a player, mapped to a value of False. The goal list contains two sublists, each representing the coordinates of all cells marked with 'BG' or 'GB' respectively.
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
        
    #State: After executing the loop for `t` iterations, the output state will consist of the following:
    print('FINAL SCORE: %d %d' % (points[0], points[1]))
    #This is printed: FINAL SCORE: [points[0]] [points[1]]
#Overall this is what the function does:The function processes a game scenario involving two teams on a grid-based field. It reads initial setup data from standard input, including field dimensions, grid layout, player positions, and team goals. The function then simulates a series of commands over multiple time steps, updating player positions and handling events such as catching the Golden Snitch, eliminating players, and scoring goals. Finally, it prints the final scores of both teams.

#State of the program right berfore the function call: pos is a string representing a position on the field, where the position is either 'RG' or 'BG'. goal is a list of two sets, where each set contains the positions of the goals for the respective team ('RG' for red goals and 'BG' for blue goals).
def goalIn(pos):
    res = 0 if pos in goal[0] else 1 if pos in goal[1] else -1
    return res
    #The program returns res which is 0 if pos is in goal[0], 1 if pos is in goal[1], and -1 otherwise.
#Overall this is what the function does:The function `goalIn` takes a position `pos` on a field and a list of goals `goal`. It checks if `pos` is in the set of red goals (`goal[0]`) or blue goals (`goal[1]`). If `pos` is in the red goals, it returns 0; if in the blue goals, it returns 1; otherwise, it returns -1.

#State of the program right berfore the function call: el is a string representing an entity on the field, where the first character indicates the team (R for Red, B for Blue) and the second character (if present) indicates the player number (0-9) or G indicating a goal (RG for Red Goal, BG for Blue Goal).
def isPlayer(el):
    res = (el[0] == 'B' or el[0] == 'R') and el[1] != 'G'
    return res
    #The program returns a boolean value 'res' which is True if 'el' starts with 'B' or 'R' and does not end with 'G', otherwise it is False.
#Overall this is what the function does:The function `isPlayer` accepts a string `el` representing an entity on the field. It checks if `el` starts with either 'B' or 'R' and does not end with 'G'. If both conditions are met, it returns `True`; otherwise, it returns `False`.

