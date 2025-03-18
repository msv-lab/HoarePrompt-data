#State of the program right berfore the function call: n and m are integers such that 3 ≤ n, m ≤ 99 and both are odd. grid is a 2D list of strings representing the field, where each string is a row of the field and contains pairs of characters representing different entities. allPlayers is a dictionary mapping player entities to boolean values indicating whether they are carrying the Quaffle. goal is a list of two lists, where each sublist contains tuples representing the positions of the goals for the respective team. points is a list of two integers representing the current scores for the red and blue teams. mov is a dictionary mapping movement commands ('U', 'D', 'L', 'R') to their corresponding changes in position coordinates. elements is a dictionary mapping entity identifiers to their positions on the field.
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
        
    #State: Output State: After the loop executes all its iterations, `ind` will be equal to the length of `line` minus one for each iteration of `i` from 0 to `n-1`. The `grid` will be a list containing `n` lines, where each line is a list of strings read from standard input. The `elements` dictionary will contain key-value pairs for each non-'. '..' entry in each line of `grid`, where each key is an entry in `line` and the value is a tuple `(i, ind)`. If `isPlayer(line[ind])` is true, then `allPlayers[line[ind]]` will be set to `False`. For any entry in `line` that is a goal identifier (i.e., starts with 'G'), `goal[tmp]` (where `tmp` is 0 if the first character is 'B', otherwise 1) will contain a list of tuples `(i, ind)` for all such entries across all lines in `grid`.
    #
    #The `points` and `mov` dictionaries will remain as they were initialized, and `goal` will be a list of two empty lists, as it was initialized.
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
        
    #State: All iterations of the loop have completed.
    print('FINAL SCORE: %d %d' % (points[0], points[1]))
    #This is printed: FINAL SCORE: [points[0]] [points[1]]
#Overall this is what the function does:The function processes a game field represented by a 2D grid and updates the state based on player movements and interactions. It reads initial field dimensions and configuration from standard input, then processes a series of commands over multiple time steps. During each command, it updates player positions, checks for golden snitch catches, eliminations, and goal scoring. Finally, it prints the final score for both teams.

#State of the program right berfore the function call: pos is a string representing a position on the field, where the position is either 'RG' or 'BG', indicating a goal for the red or blue team, respectively. The function returns 0 if the position is a red goal, 1 if it is a blue goal, and -1 if it is not a goal.
def goalIn(pos):
    res = 0 if pos in goal[0] else 1 if pos in goal[1] else -1
    return res
    #The program returns res which is 0 if pos is 'RG', 1 if pos is 'BG', and -1 otherwise.
#Overall this is what the function does:The function `goalIn` accepts a string `pos` indicating a position on the field ('RG' for red goal, 'BG' for blue goal), and returns 0 if the position is 'RG', 1 if it is 'BG', and -1 if it is neither a red nor a blue goal.

#State of the program right berfore the function call: el is a string representing an entity on the field, where the first character indicates the team (R for red, B for blue) and the second character (if present) indicates the player number.
def isPlayer(el):
    res = (el[0] == 'B' or el[0] == 'R') and el[1] != 'G'
    return res
    #The program returns a boolean value 'res' which is True if the first character of 'el' is 'B' or 'R' and the second character is not 'G', and False otherwise.
#Overall this is what the function does:The function `isPlayer` accepts a string `el` representing an entity on the field. It checks if the first character of `el` is either 'B' or 'R' and the second character is not 'G'. If both conditions are met, it returns `True`; otherwise, it returns `False`.

