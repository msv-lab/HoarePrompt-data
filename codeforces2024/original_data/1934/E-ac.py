import sys

# Predefined solutions for specific cases
ans1 = [8]
ans2 = [[[2, 6, 8], [3, 5, 7]]]

for _ in range(int(input())):
    n = int(input())
    
    # Check if n is in the predefined solutions
    if n in ans1:
        ans = ans2[ans1.index(n)]
        print(len(ans))
        for x in ans:
            print(' '.join(map(str, x)))
        continue
    
    ans = []  # List to store the operations
    pos = 0   # Position tracker
    ost = []  # List to store remaining indices
    
    # Loop to create operations in segments
    for i in range(3, n - 1, 4):
        if i > n // 2 - 2:
            ans.append([i, i + 1, i + 2])
            pos = i + 2
    
    # Collect remaining indices for further operations
    for i in range(pos + 1, n + 1):
        if (i % 2 != 0 or i % 4 == 0) and i > n // 2:
            ost.append(i)
    
    # Determine the last index to consider for operations
    per = n
    if (n - 1) % 4 == 2:
        per = n - 1
    elif (n - 2) % 4 == 2:
        per = n - 2
    elif (n - 3) % 4 == 2:
        per = n - 3
    
    # Create operations for the remaining indices
    for i in range(per, n // 2, -12):
        if i > n // 2:
            if i > 8:
                ans.append([i, i - 4, i - 8])
            else:
                ost.append(i)
    
    # Handle the remaining indices based on their count
    if len(ost) == 1:
        ans.append([1, 2, ost[0]])
    elif len(ost) == 2:
        ans.append([1, ost[1], ost[0]])
    elif len(ost) == 3:
        ans.append([ost[0], ost[1], ost[2]])
    elif len(ost) == 4:
        ans.append([1, ost[0], ost[1]])
        ans.append([2, ost[2], ost[3]])
    
    # Output the number of operations and the operations themselves
    print(len(ans))
    for x in ans:
        print(' '.join(map(str, x)))