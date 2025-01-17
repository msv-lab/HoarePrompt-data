import heapq
import sys

input = sys.stdin.read
data = input().split()

index = 0

t = int(data[index])
index += 1

results = []

for _ in range(t):
    n = int(data[index])
    m = int(data[index + 1])
    index += 2

    costs = list(map(int, data[index:index + n]))
    index += n

    attributes = []
    for i in range(n):
        attributes.append(list(map(int, data[index:index + m])))
        index += m

    pq = []
    heapq.heappush(pq, (costs[0], 0))  # (cost, pokemon_index)
    visited = [False] * n

    while pq:
        current_cost, current_index = heapq.heappop(pq)
        
        if visited[current_index]:
            continue
        
        visited[current_index] = True
        
        if current_index == n - 1:
            results.append(current_cost)
            break

        for i in range(n):
            if visited[i]:
                continue

            for j in range(m):
                if attributes[i][j] >= attributes[current_index][j]:
                    heapq.heappush(pq, (current_cost + costs[i], i))
                    break

for result in results:
    print(result)
