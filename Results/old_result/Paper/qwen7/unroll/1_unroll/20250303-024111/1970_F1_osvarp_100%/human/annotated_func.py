#State of the program right berfore the function call: (n, m) are positive integers such that 3 ≤ n, m ≤ 99 and both are odd. grid is a 2D list of strings representing the field, where each string contains characters representing different entities (empty cells, players, goals, and the Quaffle). elements is a dictionary mapping entities to their coordinates on the grid. allPlayers is a dictionary indicating whether a player is carrying the Quaffle. goal is a list of two lists, each containing the coordinates of the goals for the respective teams. points is a list of two integers representing the current scores of the red and blue teams. mov is a dictionary mapping movement commands (U, D, L, R) to their corresponding coordinate changes. t is a non-negative integer representing the number of steps in the game.
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
        
    #State: `n` is a positive odd integer between 3 and 99, `m` is a positive odd integer between 3 and 99; `grid` is a list of `n` rows, each row being a list of length `m`, `elements` is a dictionary containing {'.B': (-1, -1)}, `allPlayers` is an empty dictionary, `goal` is a list containing two empty lists, `points` is a list containing [0, 0]; the `grid` is populated with the input lines, where each non-empty cell is stored in the `elements` dictionary with its coordinates, and players or goals are recorded in the `allPlayers` and `goal` dictionaries accordingly.
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
        
    #State: Output State: `t` is an integer representing the number of iterations the loop has executed, `n` is a positive odd integer between 3 and 99, `m` is a positive odd integer between 3 and 99; `grid` is a list of `n` rows, each row being a list of length `m`, `elements` is a dictionary containing {'.B': (-1, -1)} and potentially updated positions for other players, `allPlayers` is a dictionary containing boolean values indicating whether a player is active, `goal` is a list containing two empty lists, `points` is a list containing the total points scored by each team after all iterations, with the first element being the score for team 0 and the second element being the score for team 1.
    #
    #The `t` value will reflect the total number of iterations the loop has run. The `elements` dictionary will contain the final positions of all players and the golden snitch after all iterations. The `allPlayers` dictionary will indicate which players are still active. The `points` list will show the cumulative scores for both teams based on the actions performed within the loop.
    print('FINAL SCORE: %d %d' % (points[0], points[1]))
    #This is printed: FINAL SCORE: [points[0]] [points[1]] (where [points[0]] is the total score for team 0 and [points[1]] is the total score for team 1 after all iterations)
#Overall this is what the function does:The function processes a game scenario involving a field represented by a 2D grid, players, goals, and scoring. It reads initial setup data from standard input, including grid dimensions, grid content, and game parameters. The function then iterates through a series of game steps, updating player positions, checking for eliminations, goal completions, and golden snitch catches. After processing all steps, it prints the final scores for both teams.

#State of the program right berfore the function call: pos is a string representing a position on the field, where the position is either 'RG' or 'BG'. The variable `goal` is a list of two sets, where each set contains the positions of the goals for the red and blue teams respectively.
def goalIn(pos):
    res = 0 if pos in goal[0] else 1 if pos in goal[1] else -1
    return res
    #The program returns res which is 0 if pos is in goal[0], 1 if pos is in goal[1], and -1 otherwise.
#Overall this is what the function does:Functionality: The function `goalIn` accepts a parameter `pos`, which is a string representing a position on the field ('RG' or 'BG'), and a parameter `goal`, which is a list of two sets containing the positions of the goals for the red and blue teams respectively. It checks whether `pos` is in the set of red team goals (`goal[0]`) or the set of blue team goals (`goal[1]`). If `pos` is in the set of red team goals, it returns 0; if `pos` is in the set of blue team goals, it returns 1; otherwise, it returns -1.

#State of the program right berfore the function call: el is a string representing an entity on the field, where the first character is the team (either 'R' for Red or 'B' for Blue) and the second character is additional information (e.g., player number or 'G' for goal).
def isPlayer(el):
    res = (el[0] == 'B' or el[0] == 'R') and el[1] != 'G'
    return res
    #The program returns a boolean value 'res' which is True if 'el' starts with 'B' or 'R' and does not end with 'G', otherwise False.
#Overall this is what the function does:The function `isPlayer` accepts a string `el` representing an entity on the field. It checks if `el` starts with either 'B' or 'R' and does not end with 'G'. If both conditions are met, it returns `True`; otherwise, it returns `False`.

