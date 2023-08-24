n, k = map(int, input().split())
buildings = []
for _ in range(n):
    a, b = map(int, input().split())
    buildings.append((a, b))

weather = []
for _ in range(n):
    w = input()
    weather.append(w)

happiness = 0

for i in range(n):
    a, b = buildings[i]
    w = weather[i]
    
    if w[0] == 'R' and w[1] == 'R' and w[2] == 'R':
        happiness += 2
    elif (w[0] == 'R' and w[1] == 'R') or (w[1] == 'R' and w[2] == 'R') or (w[0] == 'R' and w[2] == 'R'):
        happiness += 1

print(happiness)