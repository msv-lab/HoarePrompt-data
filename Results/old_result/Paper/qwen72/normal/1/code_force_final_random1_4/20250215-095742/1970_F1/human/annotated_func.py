#State of the program right berfore the function call: n and m are integers such that 3 <= n, m <= 99 and both n and m are odd.
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
        
    #State: After the loop executes all iterations, the following state is reached:
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
        
    #State: After the loop has executed all iterations, `t` is 0, as the loop has completed its execution based on the initial value of `t`. The variable `time` will have reached the value of `t - 1` (the last iteration index). The dictionary `allPlayers` will contain the final state of players, where each key is a player identifier and the value is a boolean indicating whether the player is active (`True`) or inactive (`False`). The list `points` will contain the final scores for each team, with `points[0]` representing the score for Team 0 and `points[1]` representing the score for Team 1. The dictionary `elements` will contain the final positions of all objects, including players and the ball, with each key being an object identifier and the value being a tuple representing the coordinates of the object. The grid `grid` will reflect the final state of the game board, with the positions of players and the ball updated according to the commands executed during the loop.
    print('FINAL SCORE: %d %d' % (points[0], points[1]))
    #This is printed: FINAL SCORE: [points[0]] [points[1]] (where [points[0]] is the final score for Team 0 and [points[1]] is the final score for Team 1)
#Overall this is what the function does:The function `func_1` reads input from standard input to simulate a game. It initializes a grid based on the dimensions `n` and `m`, which are odd integers between 3 and 99. The function processes a series of commands over `t` turns, updating the positions of players and a ball, and managing game events such as scoring goals, catching the golden snitch, and eliminating players. After processing all commands, it prints the final scores for two teams. The function does not return any value but modifies and prints the final state of the game, including the scores and any relevant game events.

#State of the program right berfore the function call: pos is a tuple representing a position on the field, and goal is a list containing two sets, where the first set contains positions of the red team's goals and the second set contains positions of the blue team's goals.
def goalIn(pos):
    res = 0 if pos in goal[0] else 1 if pos in goal[1] else -1
    return res
    #The program returns 0 if `pos` is in the first set of `goal` (red team's goals), 1 if `pos` is in the second set of `goal` (blue team's goals), and -1 otherwise.
#Overall this is what the function does:The function `goalIn` takes a tuple `pos` representing a position on the field and a list `goal` containing two sets of positions (the first set for the red team's goals and the second set for the blue team's goals). It returns 0 if `pos` is in the red team's goals, 1 if `pos` is in the blue team's goals, and -1 if `pos` is not in either set. The function does not modify any input parameters and only returns one of these three values based on the position provided.

#State of the program right berfore the function call: el is a string of length 2, where the first character is either 'B' or 'R' and the second character is a digit (0-9) or 'G'.
def isPlayer(el):
    res = (el[0] == 'B' or el[0] == 'R') and el[1] != 'G'
    return res
    #The program returns True if the first character of `el` is 'B' or 'R' and the second character is not 'G'. Otherwise, it returns False.
#Overall this is what the function does:The function `isPlayer` accepts a string `el` of length 2, where the first character is either 'B' or 'R' and the second character is a digit (0-9) or 'G'. It returns `True` if the first character is 'B' or 'R' and the second character is not 'G'. Otherwise, it returns `False`.

