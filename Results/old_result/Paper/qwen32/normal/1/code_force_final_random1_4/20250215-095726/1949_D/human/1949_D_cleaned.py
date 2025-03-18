n = int(input())
a = [0] * (n + 1)
b = [0] * (n + 1)
xx = ['']
for i in range(1, n + 1):
    x = input()
    for j in range(1, n + 1):
        if x[j - 1] == 'F':
            a[i] += 1
            a[j] += 1
        elif x[j - 1] == 'S':
            b[i] += 1
            b[j] += 1
    xx.append(x)
sa = []
sb = []
for i in range(1, n + 1):
    if a[i] > 0 and b[i] == 0:
        sa.append(i)
    if b[i] > 0 and a[i] == 0:
        sb.append(i)
if len(sa) >= len(sb):
    for i in range(1, n + 1):
        if a[i] == 0 and b[i] == 0:
            sa.append(i)
    for i in range(1, n + 1):
        nx = ''
        for j in range(1, n + 1):
            if xx[i][j - 1] != '?':
                nx += xx[i][j - 1]
            elif i in sa[:n // 4] or j in sa[:n // 4]:
                nx += 'F'
            else:
                nx += 'S'
        print(nx)
else:
    for i in range(1, n + 1):
        if a[i] == 0 and b[i] == 0:
            sb.append(i)
    for i in range(1, n + 1):
        nx = ''
        for j in range(1, n + 1):
            if xx[i][j - 1] != '?':
                nx += xx[i][j - 1]
            elif i in sb[:n // 4] or j in sb[:n // 4]:
                nx += 'S'
            else:
                nx += 'F'
        print(nx)