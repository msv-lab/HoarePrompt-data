#State of the program right berfore the function call: n and m are integers such that 3 <= n, m <= 99 and both are odd. grid is a list of n lists, each containing m pairs of characters representing the initial state of the Quidditch field. elements is a dictionary mapping each entity (player, goal, Quaffle) to its initial position (row, column) on the grid. allPlayers is a dictionary mapping each player to a boolean indicating whether they are currently carrying the Quaffle. goal is a list of two lists, where each sublist contains the positions of the goals for the respective team (blue or red). points is a list of two integers representing the current scores of the red and blue teams.
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
        
    #State: After the loop executes all iterations, `n` is a specific integer read from the input, `i` is `n-1`, `m` is a specific integer read from the input, `grid` is a list containing `n` elements, each of which is a list of strings obtained from reading and splitting a line from standard input. `elements` is a dictionary with the entry `'.B': (-1, -1)` and an entry for each string `s` in any `line` that is not '..' with the value `(i, index_of_s)`, where `i` is the iteration index and `index_of_s` is the index of the string `s` in the corresponding `line`. `points` is a list of two integers `[0, 0]` representing the current scores of the red and blue teams. `allPlayers` is a dictionary with entries for each string `s` in any `line` that represents a player, with the value `False`. `goal` is a list containing two lists. For each string `s` in any `line` that is not '..' and has a second character 'G', the tuple `(i, index_of_s)` is appended to `goal[tmp]`, where `tmp` is 0 if the first character of `s` is 'B', otherwise `tmp` is 1.
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
        
    #State: After all iterations of the loop, the variables `time` will be equal to `t`, and the values of `points`, `allPlayers`, and `elements` will reflect the changes made during the loop based on the commands read from the input. The `grid` and `goal` will remain unchanged, and `n`, `i`, and `m` will retain their initial values.
    print('FINAL SCORE: %d %d' % (points[0], points[1]))
    #This is printed: FINAL SCORE: [points[0]] [points[1]] (where [points[0]] and [points[1]] are the final scores of the two players after all iterations of the loop)
#Overall this is what the function does:This function reads and processes a series of inputs to simulate a Quidditch game. It initializes the game state with the dimensions of the playing field, the initial positions of players, the Quaffle, and goals, and the initial scores of both teams. The function then processes a series of commands over a specified number of turns, updating the game state accordingly. Specifically, it handles player movements, the capture of the Golden Snitch, scoring goals, and player eliminations. After processing all commands, it prints the final scores of the red and blue teams. The function does not return any value; it only modifies and prints the game state.

#State of the program right berfore the function call: pos is a tuple of integers representing a position on the field, and goal is a list containing two sets of tuples, where the first set represents the positions of the red team's goals and the second set represents the positions of the blue team's goals.
def goalIn(pos):
    res = 0 if pos in goal[0] else 1 if pos in goal[1] else -1
    return res
    #The program returns 0 if `pos` is in the first set of `goal`, 1 if `pos` is in the second set of `goal`, and -1 otherwise.
#Overall this is what the function does:The function `goalIn` takes a single parameter `pos`, which is a tuple of integers representing a position on the field. It checks whether `pos` is in the first set of `goal` (representing the red team's goals), the second set of `goal` (representing the blue team's goals), or neither. The function returns 0 if `pos` is in the first set, 1 if `pos` is in the second set, and -1 if `pos` is not in either set.

#State of the program right berfore the function call: el is a string of length 2, where the first character is either 'B' or 'R' and the second character is a digit from 0 to 9 or 'G'.
def isPlayer(el):
    res = (el[0] == 'B' or el[0] == 'R') and el[1] != 'G'
    return res
    #The program returns True if the first character of `el` is 'B' or 'R' and the second character is not 'G', otherwise it returns False.
#Overall this is what the function does:The function `isPlayer` takes a string `el` of length 2, where the first character is either 'B' or 'R' and the second character is a digit from 0 to 9 or 'G'. It returns `True` if the first character is 'B' or 'R' and the second character is not 'G'; otherwise, it returns `False`.

