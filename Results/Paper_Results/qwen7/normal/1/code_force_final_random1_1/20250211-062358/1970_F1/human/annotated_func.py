#State of the program right berfore the function call: (n, m) are positive integers such that 3 ≤ n, m ≤ 99 and both are odd. grid is a 2D list of strings representing the field, where each string is a row of the field and contains characters like '..', 'R0', 'B0', 'RG', 'BG', and '.Q'. elements is a dictionary mapping entities on the field to their coordinates, allPlayers is a dictionary mapping players to whether they are carrying the Quaffle or not, goal is a list of lists where each sublist contains the coordinates of the goals for the red and blue teams respectively, and points is a list of two integers representing the current scores of the red and blue teams.
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
        
    #State: Output State: After the loop executes all its iterations, the final state of the variables is as follows: `i` will be incremented by the sum of the values of `elements[line[ind]]` for each iteration, `ind` will be set to the last index processed in the loop, `n` will remain an odd integer between 3 and 99 inclusive, `line` will be a list of strings read from `stdin` until the end of input, `grid` will be a list containing `n` elements, each of which is a list `line` representing a row of the input grid, `elements` will be a dictionary where for every non-`.` character in any of the lines, the key is the character and the value is a tuple `(i, ind)` where `ind` is the index of the character in its respective line. If `isPlayer(line[ind])` is `True`, then `allPlayers[line[ind]]` will be `False`. If `isPlayer(line[ind])` returns `False`, then either `line[ind][1]` is 'G' and `tmp` is 0 if `line[ind][0]` equals 'B', otherwise `tmp` is 1, and `goal[tmp]` will contain tuples `(i, ind)` for each non-`.` character in the respective line.
    #
    #In summary, the grid will be fully populated with all lines read from standard input, and the dictionaries and lists (`elements`, `allPlayers`, `goal`, `grid`) will be updated according to the rules described within the loop.
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
        
    #State: All players' `allPlayers` status is determined, and their respective points are finalized. The positions of all players and the golden snitch are settled.
    print('FINAL SCORE: %d %d' % (points[0], points[1]))
    #This is printed: FINAL SCORE: [points[0]] [points[1]]
#Overall this is what the function does:The function processes a game board represented by a 2D grid and updates the game state based on commands. It reads the initial setup of the game, including the grid, players, and goals, and then processes a series of commands. For each command, it updates the positions of the players, checks for eliminations, catches of the golden snitch, and goals scored. Finally, it prints the final scores of the two teams.

#State of the program right berfore the function call: pos is a string representing a position on the field, where the position is either 'RG' or 'BG'. The function assumes that the variable `goal` is a list containing two sets: the first set contains all the positions of the red goals ('RG'), and the second set contains all the positions of the blue goals ('BG').
def goalIn(pos):
    res = 0 if pos in goal[0] else 1 if pos in goal[1] else -1
    return res
    #The program returns res which is 0 if pos is 'RG', 1 if pos is 'BG', and -1 otherwise.
#Overall this is what the function does:The function accepts a string `pos` representing a position on the field. It checks whether `pos` is 'RG' or 'BG' and returns 0 if `pos` is 'RG', 1 if `pos` is 'BG', and -1 if `pos` is neither 'RG' nor 'BG'.

#State of the program right berfore the function call: el is a string representing an entity on the field, where the first character is the team ('R' for red, 'B' for blue) and the second character is either a player number or 'G' for a goal.
def isPlayer(el):
    res = (el[0] == 'B' or el[0] == 'R') and el[1] != 'G'
    return res
    #The program returns a boolean value 'res' which is True if 'el' starts with 'B' or 'R' and does not end with 'G', otherwise False.
#Overall this is what the function does:The function `isPlayer` accepts a string `el` representing an entity on the field. It checks if `el` starts with 'B' or 'R' and does not end with 'G'. If both conditions are met, it returns `True`; otherwise, it returns `False`.

