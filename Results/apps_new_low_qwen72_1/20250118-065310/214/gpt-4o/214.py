def find_floor(n, m, flats_memory):
    possible_floors = set()
    for k, f in flats_memory:
        possible_floors.add((k - 1) // f)
    
    if len(possible_floors) == 1:
        flats_per_floor = list(possible_floors)[0] + 1
        return (n - 1) // flats_per_floor + 1
    else:
        return -1

# Read input
n, m = map(int, input().split())
flats_memory = [tuple(map(int, input().split())) for _ in range(m)]

# Find and print the floor number of the n-th flat
print(find_floor(n, m, flats_memory))
