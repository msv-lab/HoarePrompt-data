n, k = map(int, input().split())

buildings = []
for _ in range(n):
    a = int(input())
    b = int(input())
    buildings.append((a, b))

weather = []
for _ in range(n):
    w = input()
    weather.append(w)

happiness = 0

for i in range(n):
    a, b = buildings[i]
    w = weather[i]
    
    if 'R' in w and a != b:
        happiness += 1
        if w == 'RRR':
            happiness += 1

print(happiness)