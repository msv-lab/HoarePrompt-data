from heapq import heappush, heappop

def Dijkstra(adj_list, start):
    n = len(adj_list)
    dist = [float('inf')] * n
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        d, node = heappop(pq)
        if d > dist[node]:
            continue

        for neighbor, w in adj_list[node]:
            new_dist = dist[node] + w
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heappush(pq, (new_dist, neighbor))

    return dist


# Read input values
G, K, R = map(int, input().split())

# Create an adjacency list to represent the graph
adj_list = [[] for _ in range(K+1)]
for _ in range(R):
    A, B, T = map(int, input().split())
    adj_list[A].append((B, T))
    adj_list[B].append((A, T))

# Read gig offers
gigs = []
for _ in range(G):
    V, S, E, M = map(int, input().split())
    gigs.append((V, S, E, M))

# Sort the gig offers by end time in ascending order
gigs.sort(key=lambda x: x[2])

# Create a time list to store the maximum cryptocents that can be earned at each time for each venue
max_cryptocents = [0] * (max(gig[2] for gig in gigs) + 1)

# Iterate over each gig offer and calculate the maximum cryptocents that can be earned at each time for each venue
for gig in gigs:
    V, S, E, M = gig
    dist = Dijkstra(adj_list, V)
    for time in range(S, E):
        max_cryptocents[time] = max(max_cryptocents[time], max_cryptocents[time - 1])
        max_cryptocents[time] = max(max_cryptocents[time], max_cryptocents[time - dist[V]] + M)

# Find the maximum cryptocents that can be earned across all times
max_earnings = max(max_cryptocents)

# Print the result
print(max_earnings)