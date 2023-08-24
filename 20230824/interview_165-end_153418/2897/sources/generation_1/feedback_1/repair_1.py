def check_route(r, c, mymap, n, queries):
    results = []
    for query in queries:
        r1, c1, r2, c2 = query
        if mymap[r1-1][c1-1] == mymap[r2-1][c2-1]:
            result = "binary" if mymap[r1-1][c1-1] == '0' else "decimal"
        else:
            result = "neither"
        results.append(result)
    return results

r, c = map(int, input().split())
mymap = []
for _ in range(r):
    mymap.append(input())
n = int(input())
queries = []
for _ in range(n):
    query = list(map(int, input().split()))
    queries.append(query)

results = check_route(r, c, mymap, n, queries)

for result in results:
    print(result)