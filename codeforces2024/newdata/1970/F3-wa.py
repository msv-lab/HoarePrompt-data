def parse_input():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    N, M = map(int, data[0].split())
    field = [line.split() for line in data[1:N+1]]
    T = int(data[N+1])
    actions = data[N+2:N+2+T]
    
    return N, M, field, T, actions

def find_entities(field):
    entities = {}
    for i, row in enumerate(field):
        for j, cell in enumerate(row):
            if cell != '..':
                entities[cell] = (i, j)
    return entities

def simulate_game(N, M, field, T, actions):
    entities = find_entities(field)
    scores = {'R': 0, 'B': 0}
    carrying_quaffle = {player: False for player in entities if player[0] in 'RB'}
    events = []
    
    for t, action in enumerate(actions):
        parts = action.split()
        entity = parts[0]
        action_type = parts[1]
        
        if action_type in 'UDLR':
            # Move the entity
            i, j = entities[entity]
            if action_type == 'U':
                i -= 1
            elif action_type == 'D':
                i += 1
            elif action_type == 'L':
                j -= 1
            elif action_type == 'R':
                j += 1
            entities[entity] = (i, j)
            
            # Check for Bludger collision
            if entity[0] in 'RB' and '.B' in entities and entities[entity] == entities['.B']:
                events.append(f"{t} {entity} ELIMINATED")
                del entities[entity]
                if carrying_quaffle[entity]:
                    carrying_quaffle[entity] = False
                    entities['.Q'] = (i, j)
        
        elif action_type == 'C':
            # Catch the ball
            ball = parts[2]
            if ball == '.Q':
                carrying_quaffle[entity] = True
                del entities['.Q']
        
        elif action_type == 'T':
            # Throw the Quaffle
            if carrying_quaffle[entity]:
                i, j = entities[entity]
                entities['.Q'] = (i, j)
                carrying_quaffle[entity] = False
        
        # Check for scoring
        if '.Q' in entities:
            i, j = entities['.Q']
            for goal in entities:
                if goal in ['RG', 'BG'] and entities[goal] == (i, j):
                    if goal == 'RG':
                        if entity[0] == 'B':
                            events.append(f"{t} BLUE GOAL")
                            scores['B'] += 1
                        else:
                            events.append(f"{t} RED GOAL")
                            scores['R'] += 1
                    elif goal == 'BG':
                        if entity[0] == 'R':
                            events.append(f"{t} RED GOAL")
                            scores['R'] += 1
                        else:
                            events.append(f"{t} BLUE GOAL")
                            scores['B'] += 1
                    # Reset Quaffle to center
                    entities['.Q'] = ((N+1)//2 - 1, (M+1)//2 - 1)
        
        # Check for Golden Snitch
        if '.S' in entities and entity[0] in 'RB' and entities[entity] == entities['.S']:
            if entity[0] == 'R':
                events.append(f"{t} RED CATCH GOLDEN SNITCH")
                scores['R'] += 10
            else:
                events.append(f"{t} BLUE CATCH GOLDEN SNITCH")
                scores['B'] += 10
            break  # Game ends immediately
    
    return events, scores

def main():
    N, M, field, T, actions = parse_input()
    events, scores = simulate_game(N, M, field, T, actions)
    
    for event in events:
        print(event)
    print(f"FINAL SCORE: {scores['R']} {scores['B']}")

if __name__ == "__main__":
    main()