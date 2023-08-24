P, R, L = map(int, input().split())

adj_list = [[] for _ in range(R+2)]
for _ in range(L):
    E1, E2 = map(int, input().split())
    adj_list[E1].append(E2)
    adj_list[E2].append(E1)

visited = [False] * (R+2)

def dfs(v):
    visited[v] = True
    count = 1
    for u in adj_list[v]:
        if not visited[u]:
            count += dfs(u)
    return count

total_count = dfs(-2)
left_behind = P - total_count

if left_behind < 0:
    print(0)
elif left_behind == 0:
    print(total_count - 1)  # subtract 1 since Sally is already on the right bank
else:
    print(left_behind)