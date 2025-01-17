def func_1():
    import sys
    input = sys.stdin.read
    data = input().split('\n')
    MOD = 10 ** 9 + 7
    (N, M) = map(int, data[0].split())
    field = [data[i + 1].split() for i in range(N)]
    T = int(data[N + 1])
    actions = [data[N + 2 + i] for i in range(T)]
    players = {}
    goals = {'RG': [], 'BG': []}
    quaffle = None
    bludger = None
    for i in range(N):
        for j in range(M):
            cell = field[i][j]
            if cell in ('RG', 'BG'):
                goals[cell].append((i, j))
            elif cell == '.Q':
                quaffle = (i, j)
            elif cell == '.B':
                bludger = (i, j)
            elif cell != '..':
                players[cell] = {'pos': (i, j), 'has_quaffle': False}
    (red_score, blue_score) = (0, 0)
    events = []
    for t in range(T):
        action = actions[t].split()
        entity = action[0]
        command = action[1]
        if entity in players:
            (x, y) = players[entity]['pos']
            if command == 'U':
                x -= 1
            elif command == 'D':
                x += 1
            elif command == 'L':
                y -= 1
            elif command == 'R':
                y += 1
            elif command == 'C':
                if (x, y) == quaffle:
                    players[entity]['has_quaffle'] = True
            elif command == 'T':
                if players[entity]['has_quaffle']:
                    quaffle = (x, y)
                    players[entity]['has_quaffle'] = False
                    for goal_type in goals:
                        if quaffle in goals[goal_type]:
                            if goal_type == 'RG' and entity[0] == 'B' or (goal_type == 'BG' and entity[0] == 'R'):
                                if entity[0] == 'R':
                                    red_score += 1
                                    events.append(f'{t} RED GOAL')
                                else:
                                    blue_score += 1
                                    events.append(f'{t} BLUE GOAL')
                            quaffle = (N // 2, M // 2)
                            break
            if command in 'UDLR':
                players[entity]['pos'] = (x, y)
                if (x, y) == bludger:
                    events.append(f'{t} {entity} ELIMINATED')
                    del players[entity]
    for event in sorted(events):
        print(event)
    print(f'FINAL SCORE: {red_score} {blue_score}')
if __name__ == '__main__':
    func_1()