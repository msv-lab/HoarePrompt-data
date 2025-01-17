from collections import defaultdict, deque

n, k = map(int, input().split())
main_courses = set(map(int, input().split()))
graph = defaultdict(list)
in_degree = [0] * (n + 1)
for i in range(1, n + 1):
    t = int(input())
    in_degree[i] = t
    for j in range(t):
        u = int(input())
        graph[u].append(i)

queue = deque([i for i in range(1, n + 1) if in_degree[i] == 0])
passed_courses = 0
order = []
while queue:
    u = queue.popleft()
    order.append(u)
    passed_courses += 1
    for v in graph[u]:
        in_degree[v] -= 1
        if in_degree[v] == 0:
            queue.append(v)

if len(order) != n:
    print(-1)
else:
    print(passed_courses)
    print(' '.join(map(str, order)))
