n = int(input())
cafes = list(map(int, input().split()))

last_index = {}
result = None

for cafe in cafes:
    last_index[cafe] = cafes.index(cafe)

max_index = -1
for cafe in last_index:
    if last_index[cafe] > max_index:
        max_index = last_index[cafe]
        result = cafe

print(result)