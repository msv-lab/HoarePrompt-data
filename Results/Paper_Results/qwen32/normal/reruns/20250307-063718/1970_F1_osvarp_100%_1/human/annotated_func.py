#State of the program right berfore the function call: n and m are integers representing the dimensions of the grid (n lines and m columns), where 3 <= n, m <= 99 and both n and m are odd. grid is a 2D list of strings representing the field, with each string being either '..' for an empty cell, 'R0', ..., 'R9', 'B0', ..., 'B9' for players, 'RG' or 'BG' for goals, or '.Q' for the Quaffle. elements is a dictionary mapping each entity on the grid to its position as a tuple of integers (row, column). allPlayers is a dictionary mapping each player to a boolean indicating whether they are carrying the Quaffle. goal is a list of lists, where goal[0] contains tuples representing the positions of blue goals and goal[1] contains tuples representing the positions of red goals. points is a list of two integers representing the scores of the blue and red teams, respectively.
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
        
    #State: n is an integer such that 3 <= n <= 99 and n is odd, m is an integer such that 3 <= m <= 99 and m is odd, grid is a list containing n elements, all of which are line, points is [0, 0], i is n-1, line is a list of strings obtained from the input line, ind is len(line), elements is a dictionary containing all non-'..' elements from all lines with their coordinates (i, ind), allPlayers is a dictionary containing all player elements from all lines with a value of False, goal is a list of two lists, where the first list contains all goal elements with 'B' as the first character, and the second list contains all goal elements with a character other than 'B' as the first character.
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
        
    #State: `points` is the final scores of the two teams, `elements` is the final positions of all elements, `allPlayers` indicates which players have been caught.
    print('FINAL SCORE: %d %d' % (points[0], points[1]))
    #This is printed: FINAL SCORE: [points[0]] [points[1]] (where points[0] is the score of the first team and points[1] is the score of the second team)
#Overall this is what the function does:The function reads the dimensions and initial state of a Quidditch game grid, processes a series of game commands, and updates the positions of players and the Quaffle, as well as the scores of the blue and red teams based on the game's rules. It outputs the final scores of the game.

#State of the program right berfore the function call: pos is a tuple representing a position on the field, goal is a list of two lists where goal[0] contains positions of red goals and goal[1] contains positions of blue goals.
def goalIn(pos):
    res = 0 if pos in goal[0] else 1 if pos in goal[1] else -1
    return res
    #The program returns res, which is 0 if pos is in goal[0], 1 if pos is in goal[1], and -1 if pos is in neither.
#Overall this is what the function does:The function `goalIn` determines whether a given position `pos` is in the list of red goals (`goal[0]`), blue goals (`goal[1]`), or neither, and returns `0`, `1`, or `-1` respectively.

#State of the program right berfore the function call: el is a string representing an entity on the field, where the first character is either 'B' or 'R' and the second character is not 'G'.
def isPlayer(el):
    res = (el[0] == 'B' or el[0] == 'R') and el[1] != 'G'
    return res
    #The program returns `True`
#Overall this is what the function does:The function `isPlayer` accepts a string `el` representing an entity on the field. It returns `True` if the first character of `el` is either 'B' or 'R' and the second character is not 'G'.

