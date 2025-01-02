n = int(input())
T = [[0 for loop in range(n)] for i in range(n)]
for loop in range(n):
    T[loop] = list(map(int, raw_input().split(' ')))
lig = [0 for loop in range(n)]
for i in range(n):
    for j in range(n):
        lig[i] += T[i][j]
col = [0 for loop in range(n)]
for i in range(n):
    for j in range(n):
        col[i] += T[j][i]
compt = 0
for i in range(n):
    for j in range(n):
        if col[i] > lig[j]:
            compt += 1
print(compt)