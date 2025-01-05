n = int(input())
i = 1
sq = False
while i <= n:
    if i == n:
        sq = True
    i = i * 3
if sq:
    print('YES')
else:
    print('NO')