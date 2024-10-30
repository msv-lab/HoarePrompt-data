n = int(input())
segments = []
for _ in range(n):
    l, r = map(int, input().split())
    segments.append((l, r))

for i in range(n):
    for j in range(n):
        if i != j and segments[i][0] >= segments[j][0] and segments[i][1] <= segments[j][1]:
            print(i+1, j+1)
            exit()
print(-1, -1)
