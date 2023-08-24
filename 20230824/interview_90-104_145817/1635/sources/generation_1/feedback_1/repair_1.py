n = int(input())
cafes = list(map(int, input().split()))

last_index = {}
max_index = -1
result = None

for i in range(n-1, -1, -1):
    cafe = cafes[i]
    if cafe not in last_index:
        last_index[cafe] = i
        if i > max_index:
            max_index = i
            result = cafe

print(result)