#State of the program right berfore the function call: n and m are integers representing the dimensions of the field such that 3 <= n, m <= 99 and both are odd.
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
        
    #State: `grid` is a list of `n` lists, each of length `m`, representing the field; `elements` is a dictionary with non-'..' elements as keys and their positions as values; `allPlayers` is a dictionary with player identifiers as keys and `False` as values; `goal` is a list of two lists containing positions of 'BG' and 'RG' respectively; `points` is [0, 0].
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
        
    #State: grid is updated with new positions of elements, elements dictionary reflects final positions, allPlayers reflects active/inactive status, goal remains unchanged, points reflect scores, t remains unchanged.
    print('FINAL SCORE: %d %d' % (points[0], points[1]))
    #This is printed: FINAL SCORE: [points[0]] [points[1]] (where points[0] and points[1] are the scores of the first and second players/teams respectively)
#Overall this is what the function does:The function reads the dimensions of a field and its initial state, processes a series of commands to update the field, and prints the final scores of two teams. It also prints messages indicating when players are eliminated or goals are scored.

#State of the program right berfore the function call: pos is a tuple of two integers representing a position on the field, goal is a list of two lists where each inner list contains tuples representing the positions of the goals for the red and blue teams respectively.
def goalIn(pos):
    res = 0 if pos in goal[0] else 1 if pos in goal[1] else -1
    return res
    #The program returns res, which is 0 if pos is in goal[0], 1 if pos is in goal[1], and -1 if pos is in neither goal[0] nor goal[1]
#Overall this is what the function does:The function determines whether a given position is within the goal area of the red team, blue team, or neither, and returns 0, 1, or -1 respectively.

#State of the program right berfore the function call: el is a string representing an entity on the field, where the first character is either 'B' or 'R' (indicating the team) and the second character is not 'G'.
def isPlayer(el):
    res = (el[0] == 'B' or el[0] == 'R') and el[1] != 'G'
    return res
    #The program returns `True`
#Overall this is what the function does:The function `isPlayer` determines if a given string `el` represents a player on the field. It returns `True` if the first character of `el` is either 'B' or 'R' and the second character is not 'G'.

