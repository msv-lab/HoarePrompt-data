def play_quidditch():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    # Read the dimensions of the field
    N, M = map(int, data[0].split())
    
    # Initialize the field
    field = []
    for i in range(1, N + 1):
        field.append(data[i].split())
    
    # Read the number of steps
    T = int(data[N + 1])
    
    # Initialize positions and states
    positions = {}
    quaffle_position = None
    quaffle_carrier = None
    
    # Parse the field to find initial positions
    for i in range(N):
        for j in range(M):
            cell = field[i][j]
            if cell == '.Q':
                quaffle_position = (i, j)
            elif cell != '..':
                positions[cell] = (i, j)
    
    # Initialize scores
    red_score = 0
    blue_score = 0
    
    # Process each action
    for t in range(T):
        action = data[N + 2 + t].split()
        entity = action[0]
        command = action[1]
        
        if command in 'UDLR':
            # Move the entity
            x, y = positions[entity]
            if command == 'U':
                x -= 1
            elif command == 'D':
                x += 1
            elif command == 'L':
                y -= 1
            elif command == 'R':
                y += 1
            positions[entity] = (x, y)
            
            # If the entity is carrying the Quaffle, move it too
            if quaffle_carrier == entity:
                quaffle_position = (x, y)
        
        elif command == 'C':
            # Catch the Quaffle
            ball = action[2]
            if ball == '.Q':
                quaffle_carrier = entity
        
        elif command == 'T':
            # Throw the Quaffle
            quaffle_carrier = None
        
        # Check for scoring
        if quaffle_carrier is None and quaffle_position is not None:
            x, y = quaffle_position
            cell = field[x][y]
            if cell == 'RG':
                # Blue team scores
                blue_score += 1
                print(f"{t} BLUE GOAL")
                # Reset Quaffle to the center
                quaffle_position = ((N - 1) // 2, (M - 1) // 2)
            elif cell == 'BG':
                # Red team scores
                red_score += 1
                print(f"{t} RED GOAL")
                # Reset Quaffle to the center
                quaffle_position = ((N - 1) // 2, (M - 1) // 2)
    
    # Print the final score
    print(f"FINAL SCORE: {red_score} {blue_score}")

# Call the function to execute the game simulation
play_quidditch()