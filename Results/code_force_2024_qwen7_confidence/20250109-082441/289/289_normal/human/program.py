import sys

def find_complexes(n, m, c, corridors):
    count = 0
    for u, v in corridors:
        if v - u == 1 or u - v == 1:
            count += 1
    if count == 2:
        return n
    else:
        return -1

def min_funding(t, test_cases):
    for i in range(t):
        n, m, c = test_cases[i][0]
        corridors = test_cases[i][1]
        result = find_complexes(n, m, c, corridors)
        print(result)

t = int(sys.stdin.readline().strip())
test_cases = []
for _ in range(t):
    case = []
    n, m, c = map(int, sys.stdin.readline().strip().split())
    case.append((n, m, c))
    corridors = [tuple(map(int, sys.stdin.readline().strip().split())) for _ in range(m)]
    case.append(corridors)
    test_cases.append(case)

min_funding(t, test_cases)