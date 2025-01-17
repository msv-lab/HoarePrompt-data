def solve():
    n = int(input())  # Number of wizards
    a = list(map(int, input().split()))  # Distance requirements for each wizard
    
    # We will assign each wizard to a unique column, and try to assign rows
    # Let's start by assigning rows and columns in a simple way
    positions = []
    for i in range(n):
        positions.append((i + 1, i + 1))  # Assign wizard i to (i+1, i+1)
    
    # Now we need to check if we can satisfy the distance requirements
    visit = [-1] * n  # This will store which wizard each wizard will visit
    
    for i in range(n):
        found = False
        for j in range(n):
            if i != j:
                # Calculate the Manhattan distance between wizard i and wizard j
                dist = abs(positions[i][0] - positions[j][0]) + abs(positions[i][1] - positions[j][1])
                if dist == a[i]:
                    visit[i] = j + 1  # Wizard i will visit wizard j
                    found = True
                    break
        if not found:
            print("NO")
            return
    
    # If we reach here, it means we found a valid solution
    print("YES")
    for pos in positions:
        print(pos[0], pos[1])
    print(" ".join(map(str, visit)))

# Read input and solve the problem
solve()