n, r = map(int, input().split())
house = list(map(int, input().split()))

heaters = []
count = 0

for i in range(n):
    if house[i] == 1:
        heaters.append(i)
        
for i in range(n):
    if house[i] == 1:
        continue
    
    found = False
    for j in range(len(heaters)-1, -1, -1):
        if i-r+1 <= heaters[j] <= i+r-1:
            count += 1
            found = True
            break
    if not found:
        print(-1)
        break

if found:
    print(count)
    