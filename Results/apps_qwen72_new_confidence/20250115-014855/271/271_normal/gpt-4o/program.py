import sys
from collections import defaultdict, deque
import heapq

def solve():
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    M = int(data[1])
    
    edges = defaultdict(list)
    
    index = 2
    for _ in range(M):
        s = int(data[index])
        t = int(data[index + 1])
        edges[s].append(t)
        index += 2
    
    def calculate_expected_value():
        expected = [float('inf')] * (N + 1)
        expected[N] = 0
        indegree = [0] * (N + 1)
        for u in edges:
            for v in edges[u]:
                indegree[v] += 1
        
        queue = deque()
        for i in range(1, N + 1):
            if indegree[i] == 0:
                queue.append(i)
        
        while queue:
            u = queue.popleft()
            if u == N:
                continue
            if len(edges[u]) == 0:
                continue
            total_expectation = 0
            for v in edges[u]:
                total_expectation += expected[v]
            expected[u] = 1 + total_expectation / len(edges[u])
            for v in edges[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    queue.append(v)
        
        return expected
    
    initial_expected = calculate_expected_value()
    min_expected = initial_expected[1]
    
    for v in edges[1]:
        edges[1].remove(v)
        updated_expected = calculate_expected_value()
        min_expected = min(min_expected, updated_expected[1])
        edges[1].append(v)
    
    print("{:.10f}".format(min_expected))

if __name__ == "__main__":
    solve()
