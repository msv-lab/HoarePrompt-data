import sys
sys.setrecursionlimit(10**6) # Increase recursion stack size

def dfs(node):
    visited[node] = True
    color[node] = curr_color
    for neigh in adj_list[node]:
        if visited[neigh] == False:
            dfs(neigh)

T = int(input())
for _ in range(T):
    n = int(input())
    adj_list = [[] for __ in range(n)]
    visited = [False]*n
    color = [-1]*n
    curr_color = 0
    for i in range(n-1):
        print('? {} {}'.format(min(i+1, n), max(i+1, n)), flush=True)
        ans = input().strip()
        if ans == 'YES':
            adj_list[i].append(n-1)
            adj_list[n-1].append(i)
    for node in range(n):
        if visited[node]==False:
            dfs(node)
            curr_color ^= 1 # Flip current color between 0 and 1
    print('! {}'.format(' '.join(map(str, color))), flush=True)