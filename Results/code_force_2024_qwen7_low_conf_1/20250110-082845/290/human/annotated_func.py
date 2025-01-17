#State of the program right berfore the function call: N and M are integers such that 3 ≤ N, M ≤ 99 and both are odd. The field is represented as a 2D list of strings, where each string contains M characters, and the first line is a header indicating the dimensions of the field. The field contains up to 10 players for each team, represented by 'R0' to 'R9' for the red team and 'B0' to 'B9' for the blue team. There is exactly one Quaffle represented by '.Q'. Each team has between 1 and 5 goals, represented by 'RG' for a red goal and 'BG' for a blue goal. The number of steps T is an integer such that 0 ≤ T ≤ 10000. Each step is described by a string indicating the action performed by an entity on the field, where the action can be moving ('U', 'D', 'L', 'R'), catching a ball ('C' followed by the ball type), or throwing the Quaffle ('T').
def func_1():
    N, M = map(int, input().split())
    field = [input().split() for _ in range(N)]
    T = int(input())
    actions = [input().split() for _ in range(T)]
    quaffle_position = None
    goals = {'RG': 0, 'BG': 0}
    players = {'R': {}, 'B': {}}
    score = {'R': 0, 'B': 0}
    for i in range(N):
        for j in range(M):
            if field[i][j] == '.Q':
                quaffle_position = i, j
            elif field[i][j] in ['RG', 'BG']:
                goals[field[i][j]] += 1
            elif field[i][j][0] in ['R', 'B']:
                team, number = field[i][j]
                players[team][number] = i, j
        
    #State of the program after the  for loop has been executed: `N` is an integer, 3 ≤ N, M ≤ 99 and both are odd; `M` is an integer, 3 ≤ N, M ≤ 99 and both are odd; `field` is a 2D list of strings representing the field; `T` is an integer, input from the user; `actions` is a list of T lists of strings created by splitting each input line by spaces; `quaffle_position` is a tuple containing the last row and column index where field[i][j] is '.Q'; `goals` is a dictionary where goals['RG'] is the total number of occurrences of 'RG' and goals['BG'] is the total number of occurrences of 'BG'; `players` is a dictionary mapping each team ('R' or 'B') to a dictionary of player numbers to their positions in the field, where each position is a tuple containing the row and column indices.
    for (t, (entity, action, *args)) in enumerate(actions):
        if action == 'U':
            players[entity[0]][entity[1]] = players[entity[0]][entity[1]][0
                ] - 1, players[entity[0]][entity[1]][1]
        elif action == 'D':
            players[entity[0]][entity[1]] = players[entity[0]][entity[1]][0
                ] + 1, players[entity[0]][entity[1]][1]
        elif action == 'L':
            players[entity[0]][entity[1]] = players[entity[0]][entity[1]][0], players[
                entity[0]][entity[1]][1] - 1
        elif action == 'R':
            players[entity[0]][entity[1]] = players[entity[0]][entity[1]][0], players[
                entity[0]][entity[1]][1] + 1
        elif action == 'C':
            pass
        elif action == 'T':
            quaffle_position = players[entity[0]][entity[1]]
        
        if quaffle_position in goals:
            scoring_team = 'R' if quaffle_position in ['BG'] else 'B'
            opposite_team = 'B' if scoring_team == 'R' else 'R'
            score[opposite_team] += 1
            print(f'{t} {opposite_team.upper()} GOAL')
            quaffle_position = (N + 1) // 2 - 1, (M + 1) // 2 - 1
        
    #State of the program after the  for loop has been executed: `t` is `T-1`, `scoring_team` is 'B' or 'R' depending on the final position of the quaffle, `quaffle_position` is the final position of the quaffle after all actions, `goals` is a dictionary where `goals['RG']` is the total number of occurrences of 'RG' and `goals['BG']` is the total number of occurrences of 'BG', `players` is a dictionary mapping each team ('R' or 'B') to a dictionary of player numbers to their positions in the field, where each position is a tuple containing the row and column indices, `score` is a dictionary with the scores for teams 'R' and 'B', and `opposite_team` is 'R' if `scoring_team` is 'B' and vice versa. If the loop does not execute, the initial values of `t`, `scoring_team`, `quaffle_position`, `goals`, `players`, `score`, and `opposite_team` remain unchanged.
    print(f"FINAL SCORE: {score['R']} {score['B']}")
#Overall this is what the function does:The function processes a game simulation based on a 2D field representation. It starts by parsing the initial field configuration, including the dimensions \(N\) and \(M\), the field itself, the number of steps \(T\), and the sequence of actions. It then iterates through each action, updating the positions of players and handling Quaffle transfers. If the Quaffle reaches a goal, it updates the score for the opposing team and resets the Quaffle to the center of the field. After processing all steps, it prints the final score.

