# FIX 1: Initialize max_pos with the first element of positions
max_pos = positions[0]

# FIX 2: Change the condition for breaking the loop
for i in range(n-2, -1, -1):
    if positions[i] < max_pos + r:
        break
    else:
        shots += 1
        max_pos = positions[i]
        
print(shots)