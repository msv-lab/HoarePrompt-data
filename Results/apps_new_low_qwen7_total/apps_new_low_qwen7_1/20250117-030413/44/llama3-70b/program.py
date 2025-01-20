import math

n = int(input())

v = []
for _ in range(n):
    x, y = map(int, input().split())
    v.append((x, y))

ans = (0, 1)
ans_angle = math.pi

v.sort(key=lambda v: math.atan2(v[1], v[0]))

for i in range(n):
    for j in range(i+1, min(n, i+100)):
        angle = math.acos((v[i][0]*v[j][0] + v[i][1]*v[j][1]) / 
                          math.sqrt(v[i][0]**2 + v[i][1]**2) / 
                          math.sqrt(v[j][0]**2 + v[j][1]**2))
        if angle < ans_angle:
            ans_angle = angle
            ans = (i, j)

print(ans[0]+1, ans[1]+1)
