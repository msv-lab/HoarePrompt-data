def func_1(n, m, flats_memory):
    possible_floors = set()
    for (k, f) in flats_memory:
        possible_floors.add((k - 1) // f)
    if len(possible_floors) == 1:
        flats_per_floor = list(possible_floors)[0] + 1
        return (n - 1) // flats_per_floor + 1
    else:
        return -1
(n, m) = map(int, input().split())
flats_memory = [tuple(map(int, input().split())) for _ in range(m)]
print(func_1(n, m, flats_memory))