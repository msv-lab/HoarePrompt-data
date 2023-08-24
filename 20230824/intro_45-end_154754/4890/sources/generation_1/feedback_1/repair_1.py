import math

n, m, s, d = map(int, input().split())
c = list(map(int, input().split()))

# check if it's impossible for all students to get a cold soda
if d == 0:
    print("impossible")
    exit()

# calculate the minimum number of soda bottles needed to give to the next m students
min_bottles = math.ceil(m / d)

# check if it's possible to give enough bottles to the next m students
if min_bottles > n * d:
    print("impossible")
    exit()

# refill the fridge with the new soda bottles
refill = [0] * s
remaining_bottles = n

# fill the slots that already have some bottles
for i in range(s):
    refill[i] = min(remaining_bottles, d - c[i])
    remaining_bottles -= refill[i]

# fill the remaining slots with the new soda bottles
for i in range(s):
    if remaining_bottles == 0:
        break
    refill[i] += min(remaining_bottles, d)
    remaining_bottles -= min(remaining_bottles, d)

print(*refill)