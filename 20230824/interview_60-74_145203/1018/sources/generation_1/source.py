n = int(input())
ink_volumes = list(map(int, input().split()))

remaining_ink = ink_volumes.copy()
day = 0
while len(set(remaining_ink)) > 1:
    day += 1
    current_pen = day % n
    if current_pen == 0:
        current_pen = n
    remaining_ink[current_pen-1] -= 1
    if day % 7 == 0:
        remaining_ink[current_pen-1] += 1

empty_pen = remaining_ink.index(min(remaining_ink))
print(empty_pen + 1)