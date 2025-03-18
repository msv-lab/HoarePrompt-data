#State of the program right berfore the function call: (n, m) are positive integers such that 3 ≤ n, m ≤ 99 and both are odd. grid is a 2D list of strings representing the field, where each string contains characters representing different entities (empty cells, players, goals, and the Quaffle). elements is a dictionary mapping entities to their positions on the field. allPlayers is a dictionary indicating whether each player is carrying the Quaffle or not. goal is a list of lists, where each sublist contains the positions of the goals for each team. points is a list of integers representing the current scores of the red and blue teams respectively. mov is a dictionary mapping movement commands (U, D, L, R) to their corresponding changes in position. t is a non-negative integer representing the number of steps in the game.
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
        
    #State: Output State: After the loop executes all the iterations, `i` is equal to `n-1`, `n` is an odd positive integer such that 3 ≤ n ≤ 99, `line` is a list of strings read from standard input for each row of the grid, and `grid` is a list containing `n` elements, each being a `line` read from standard input. For each index `ind` where `line[ind]` is not `'..'` and `isPlayer(line[ind])` returns `True`, `elements[line[ind]]` is set to `(i, ind)`. If `isPlayer(line[ind])` returns `False` and `line[ind][1]` is `'G'`, `tmp` is 0 if `line[ind][0]` is 'B', otherwise `tmp` is 1, and `goal[tmp]` is a list containing tuples `(i, ind)` for every index `ind` where `line[ind]` is not `'..'`.
    #
    #In simpler terms, after the loop completes all its iterations, the `grid` will contain the entire map read from standard input, with each cell's contents stored. The `elements` dictionary will map each player and goal entity to their respective positions on the grid. The `allPlayers` dictionary will mark all players as `False`, indicating they have been processed. The `goal` list will contain the coordinates of the blue ('B') and green ('G') goals based on the entities found in the grid.
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
        
    #State: All iterations of the loop have been executed, with `time` being the final iteration count specified by `t`. The variable `allPlayers` has been updated for each player, marking them as `True` if they caught a golden snitch ('.Q') or moved without conflict. The `points` list has accumulated scores for each team based on catching golden snitches and scoring goals. The `elements` dictionary holds the current positions of all entities on the grid, and the `goal` dictionary retains the coordinates of the blue and green goals.
    print('FINAL SCORE: %d %d' % (points[0], points[1]))
    #This is printed: FINAL SCORE: [points[0]] [points[1]] (where points[0] and points[1] are the accumulated scores of the first and second team respectively)
#Overall this is what the function does:The function processes a game scenario represented by a grid and updates the state of the game over a specified number of steps. It reads the initial setup of the game from standard input, including the dimensions of the grid, the positions of players, goals, and other entities, and the number of steps. During each step, it handles various game events such as players catching the Quaffle, moving, scoring goals, and eliminating other players. Finally, it prints the final scores of both teams.

#State of the program right berfore the function call: pos is a string representing a position on the field, where the field is described by N lines of M pairs of characters. The position can be one of the following: "RG" for a red goal, "BG" for a blue goal, or any other string indicating an empty cell, a player, or the Quaffle. The function returns 0 if the position is a red goal, 1 if the position is a blue goal, and -1 otherwise.
def goalIn(pos):
    res = 0 if pos in goal[0] else 1 if pos in goal[1] else -1
    return res
    #The program returns 0 or 1 or -1 depending on the value of `pos`. If `pos` is "RG", the program returns 0; if `pos` is "BG", the program returns 1; otherwise, it returns -1.
#Overall this is what the function does:The function `goalIn` takes a string `pos` representing a position on the field and returns 0 if `pos` is "RG" (indicating a red goal), 1 if `pos` is "BG" (indicating a blue goal), and -1 otherwise.

#State of the program right berfore the function call: el is a string representing an entity on the field, where the first character indicates the team (R for Red, B for Blue) and the second character (if present) indicates the player number.
def isPlayer(el):
    res = (el[0] == 'B' or el[0] == 'R') and el[1] != 'G'
    return res
    #The program returns a boolean value 'res' which indicates whether the first character of 'el' is 'B' or 'R' and the second character is not 'G'.
#Overall this is what the function does:The function `isPlayer` accepts a string `el` representing an entity on the field, checks if the first character is either 'B' or 'R' and the second character is not 'G', and returns `True` if both conditions are satisfied, otherwise returns `False`.

