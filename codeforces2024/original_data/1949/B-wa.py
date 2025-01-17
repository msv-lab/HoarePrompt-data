import sys
import threading
import bisect

def main():
    sys.setrecursionlimit(1 << 25)
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        a = list(map(int, sys.stdin.readline().split()))
        b = list(map(int, sys.stdin.readline().split()))
        a.sort()
        b.sort()
        
        # Generate candidate charm values
        candidates = set()
        for i in range(n):
            candidates.add(abs(a[i] - b[i]))
            if i > 0:
                candidates.add(abs(a[i] - b[i-1]))
            if i + 1 < n:
                candidates.add(abs(a[i] - b[i+1]))
        candidates = sorted(candidates)
        
        # Binary search over candidate charm values
        left = 0
        right = len(candidates) - 1
        answer = -1
        while left <= right:
            mid = (left + right) // 2
            c = candidates[mid]
            adj = [[] for _ in range(n)]  # Adjacency list for the bipartite graph
            for i in range(n):
                # Find all b_j such that |a_i - b_j| >= c
                l = bisect.bisect_right(b, a[i] - c)
                for j in range(l):
                    adj[i].append(j)
                r = bisect.bisect_left(b, a[i] + c)
                for j in range(r, n):
                    adj[i].append(j)
            # Hopcroft-Karp algorithm
            match_left = [-1] * n
            match_right = [-1] * n
            dist = [0] * n
            from collections import deque
            def bfs():
                queue = deque()
                for u in range(n):
                    if match_left[u] == -1:
                        dist[u] = 0
                        queue.append(u)
                    else:
                        dist[u] = -1
                found = False
                while queue:
                    u = queue.popleft()
                    for v in adj[u]:
                        if match_right[v] == -1:
                            found = True
                        elif dist[match_right[v]] == -1:
                            dist[match_right[v]] = dist[u] + 1
                            queue.append(match_right[v])
                return found
            def dfs(u):
                for v in adj[u]:
                    if match_right[v] == -1 or (dist[match_right[v]] == dist[u] +1 and dfs(match_right[v])):
                        match_left[u] = v
                        match_right[v] = u
                        return True
                dist[u] = -1
                return False
            matching = 0
            while bfs():
                for u in range(n):
                    if match_left[u] == -1 and dfs(u):
                        matching +=1
            if matching == n:
                answer = c
                left = mid + 1
            else:
                right = mid - 1
        print(answer)

threading.Thread(target=main).start()