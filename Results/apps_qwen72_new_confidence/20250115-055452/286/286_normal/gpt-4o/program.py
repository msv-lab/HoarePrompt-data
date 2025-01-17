n = int(input())
x1, x2 = map(int, input().split())

lines = []
for _ in range(n):
    k, b = map(int, input().split())
    lines.append((k, b))

# Calculate the y-values at x1 and x2 for each line
y_values_x1 = []
y_values_x2 = []
for k, b in lines:
    y_values_x1.append(k * x1 + b)
    y_values_x2.append(k * x2 + b)

# Pair the y-values with their corresponding slopes
paired_y_values_x1 = list(zip(y_values_x1, lines))
paired_y_values_x2 = list(zip(y_values_x2, lines))

# Sort the pairs by y-values at x1 and x2
paired_y_values_x1.sort()
paired_y_values_x2.sort()

# Check if the order changes between the left and right endpoints
for i in range(n - 1):
    if paired_y_values_x1[i][1] != paired_y_values_x2[i][1]:
        print("YES")
        break
else:
    print("NO")
