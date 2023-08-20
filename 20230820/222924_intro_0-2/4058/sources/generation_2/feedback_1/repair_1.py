n, r = map(int, input().split())
house = list(map(int, input().split()))

heaters = []
count = 0

# Find positions of heaters
for i in range(n):
    if house[i] == 1:
        heaters.append(i)

for i in range(n):
    if house[i] == 1:
        continue
    
    found = False
    min_dist = float('inf') # initialize minimum distance to a high value
    
    # Check heaters within range r
    for j in range(len(heaters)):
        if abs(i - heaters[j]) <= r-1: # check if the heater is within range
            dist = abs(i - heaters[j]) # calculate distance from element to heater
            if dist < min_dist: # update minimum distance if a closer heater is found
                min_dist = dist
                found = True
    if not found: # if no heater can warm up the element within range
        count += 1

if count == 0: # if all elements are already heated
    print(0)
else:
    print(count)