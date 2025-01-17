import heapq
import sys
input = sys.stdin.read

def solve():
    data = input().split()
    index = 0
    t = int(data[index])
    index += 1
    results = []
    
    for _ in range(t):
        n = int(data[index])
        m = int(data[index + 1])
        k = int(data[index + 2])
        index += 3
        
        edges = []
        for i in range(m):
            u = int(data[index])
            v = int(data[index + 1])
            a = int(data[index + 2])
            b = int(data[index + 3])
            index += 4
            edges.append((u, v, a, b))
        
        # We need to find x such that sum(x) = k * (n - 1)
        required_edges = k * (n - 1)
        
        # Priority queue to choose the best edge to increment
        pq = []
        
        # Initialize x and cost
        x = [0] * m
        cost = 0
        
        # Fill the priority queue with initial cost increments
        for i in range(m):
            a, b = edges[i][2], edges[i][3]
            # Cost increment for the first edge
            increment = a * (2 * x[i] + 1) + b
            heapq.heappush(pq, (increment, i))
        
        # Add edges until we reach the required number of edges
        for _ in range(required_edges):
            increment, i = heapq.heappop(pq)
            cost += increment
            x[i] += 1
            a, b = edges[i][2], edges[i][3]
            # Calculate new increment for this edge
            new_increment = a * (2 * x[i] + 1) + b
            heapq.heappush(pq, (new_increment, i))
        
        results.append(cost)
    
    for result in results:
        print(result)