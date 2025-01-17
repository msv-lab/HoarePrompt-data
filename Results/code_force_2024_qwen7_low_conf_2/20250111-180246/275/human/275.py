def main():
    import sys
    input = sys.stdin.read
    data = input().split('\n')
    
    MOD = 10**9 + 7
    
    # Read dimensions of the field
    N, M = map(int, data[0].split())
    
    # Read the field configuration
    field = [data[i + 1].split() for i in range(N)]
    
    # Read number of steps
    T = int(data[N + 1])
    
    # Read each action
    actions = [data[N + 2 + i] for i in range(T)]
    
    # Initialize positions and states
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
    
    # To track scores
    red_score, blue_score = 0, 0
    events = []
    
    # Process each action
    for t in range(T):
        action = actions[t].split()
        entity = action[0]
        command = action[1]
        
        if entity in players:
            x, y = players[entity]['pos']
            if command == 'U':
                x -= 1
            elif command == 'D':
                x += 1
            elif command == 'L':
                y -= 1
            elif command == 'R':
                y += 1
            elif command == 'C':
                # Catching the Quaffle
                if (x, y) == quaffle:
                    players[entity]['has_quaffle'] = True
            elif command == 'T':
                # Throwing the Quaffle
                if players[entity]['has_quaffle']:
                    quaffle = (x, y)
                    players[entity]['has_quaffle'] = False
                    # Check if it's a goal
                    for goal_type in goals:
                        if quaffle in goals[goal_type]:
                            if (goal_type == 'RG' and entity[0] == 'B') or (goal_type == 'BG' and entity[0] == 'R'):
                                if entity[0] == 'R':
                                    red_score += 1
                                    events.append(f"{t} RED GOAL")
                                else:
                                    blue_score += 1
                                    events.append(f"{t} BLUE GOAL")
                            quaffle = (N // 2, M // 2)  # Reset to middle
                            break
            
            # Update position after move
            if command in 'UDLR':
                players[entity]['pos'] = (x, y)
                # Check for Bludger collision
                if (x, y) == bludger:
                    events.append(f"{t} {entity} ELIMINATED")
                    del players[entity]  # Player is eliminated
    
    # Output all events
    for event in sorted(events):
        print(event)
    
    # Output final score
    print(f"FINAL SCORE: {red_score} {blue_score}")

if __name__ == "__main__":
    main()