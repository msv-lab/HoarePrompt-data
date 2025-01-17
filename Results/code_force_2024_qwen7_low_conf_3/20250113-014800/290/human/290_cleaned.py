def func_1():
    (N, M) = map(int, input().split())
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
                quaffle_position = (i, j)
            elif field[i][j] in ['RG', 'BG']:
                goals[field[i][j]] += 1
            elif field[i][j][0] in ['R', 'B']:
                (team, number) = field[i][j]
                players[team][number] = (i, j)
    for (t, (entity, action, *args)) in enumerate(actions):
        if action == 'U':
            players[entity[0]][entity[1]] = (players[entity[0]][entity[1]][0] - 1, players[entity[0]][entity[1]][1])
        elif action == 'D':
            players[entity[0]][entity[1]] = (players[entity[0]][entity[1]][0] + 1, players[entity[0]][entity[1]][1])
        elif action == 'L':
            players[entity[0]][entity[1]] = (players[entity[0]][entity[1]][0], players[entity[0]][entity[1]][1] - 1)
        elif action == 'R':
            players[entity[0]][entity[1]] = (players[entity[0]][entity[1]][0], players[entity[0]][entity[1]][1] + 1)
        elif action == 'C':
            pass
        elif action == 'T':
            quaffle_position = players[entity[0]][entity[1]]
        if quaffle_position in goals:
            scoring_team = 'R' if quaffle_position in ['BG'] else 'B'
            opposite_team = 'B' if scoring_team == 'R' else 'R'
            score[opposite_team] += 1
            print(f'{t} {opposite_team.upper()} GOAL')
            quaffle_position = ((N + 1) // 2 - 1, (M + 1) // 2 - 1)
    print(f"FINAL SCORE: {score['R']} {score['B']}")
if __name__ == '__main__':
    func_1()