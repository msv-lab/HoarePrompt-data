# Reading input
traffic_lights = []
for _ in range(4):
    traffic_lights.append(list(map(int, input().split())))

# Check for possible accidents
accident_possible = False
for i in range(4):
    l, s, r, p = traffic_lights[i]
    if p == 1:
        # Check if any vehicle light in the same part is green
        if l == 1 or s == 1 or r == 1:
            accident_possible = True
            break
        # Check if any vehicle light in the corresponding parts is green
        for j in range(3):
            if traffic_lights[(i + j) % 4][j] == 1:
                accident_possible = True
                break
        if accident_possible:
            break

# Output the result
if accident_possible:
    print("YES")
else:
    print("NO")
