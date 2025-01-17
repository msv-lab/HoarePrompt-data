n = int(input())  # Number of scenarios
a = [0] * (n + 1)  # Array to count 'F' transitions for each scenario
b = [0] * (n + 1)  # Array to count 'S' transitions for each scenario
xx = [""]  # To store the input matrix

# Read the input matrix and count 'F' and 'S' transitions
for i in range(1, n + 1):
    x = input()
    for j in range(1, n + 1):
        if x[j - 1] == "F":
            a[i] += 1
            a[j] += 1
        elif x[j - 1] == "S":
            b[i] += 1
            b[j] += 1
    xx.append(x)

sa = []  # Scenarios with only 'F' transitions
sb = []  # Scenarios with only 'S' transitions

# Identify scenarios with only one type of transition
for i in range(1, n + 1):
    if a[i] > 0 and b[i] == 0:
        sa.append(i)
    if b[i] > 0 and a[i] == 0:
        sb.append(i)

# Determine which type to prioritize
if len(sa) >= len(sb):
    t = len(sa)
    # Add scenarios with no transitions to 'sa'
    for i in range(1, n + 1):
        if a[i] == 0 and b[i] == 0:
            sa.append(i)
    # Fill undecided transitions
    for i in range(1, n + 1):
        nx = ""
        for j in range(1, n + 1):
            if xx[i][j - 1] != "?":
                nx += xx[i][j - 1]
            elif i in sa[:n // 4 - 1] or j in sa[:n // 4 - 1]:
                nx += "F"
            else:
                nx += "S"
        print(nx)
else:
    # Add scenarios with no transitions to 'sb'
    for i in range(1, n + 1):
        if a[i] == 0 and b[i] == 0:
            sb.append(i)
    # Fill undecided transitions
    for i in range(1, n + 1):
        nx = ""
        for j in range(1, n + 1):
            if xx[i][j - 1] != "?":
                nx += xx[i][j - 1]
            elif i in sb[:n // 4 - 1] or j in sb[:n // 4 - 1]:
                nx += "S"
            else:
                nx += "F"
        print(nx)