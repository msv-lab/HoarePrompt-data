def check_route(r, c, map, n, queries):
    for query in queries:
        r1, c1, r2, c2 = query
        if map[r1-1][c1-1] == map[r2-1][c2-1]:
            return "binary" if map[r1-1][c1-1] == '0' else "decimal"
    return "neither"

r, c = map(int, input().split())
map = []
for _ in range(r):
    map.append(input())
n = int(input())
queries = []
for _ in range(n):
    query = list(map(int, input().split()))
    queries.append(query)

result = check_route(r, c, map, n, queries)

print(result)