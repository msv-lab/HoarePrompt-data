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

# Initialize an array to store the maximum cryptocents that can be earned at each venue and each time
max_cryptocents = [[0] * (1000000000 + 1) for _ in range(K+1)]

# Iterate over each gig offer and calculate the maximum cryptocents that can be earned at each time for each venue
for gig in gigs:
    V, S, E, M = gig
    for time in range(S, E):
        max_cryptocents[V][time] = max(max_cryptocents[V][time], max_cryptocents[V][time-1])
        for neighbor, travel_time in adj_list[V]:
            if time >= travel_time:
                max_cryptocents[V][time] = max(max_cryptocents[V][time], max_cryptocents[neighbor][time-travel_time])
        max_cryptocents[V][time] += M

# Find the maximum cryptocents that can be earned across all venues and times
max_earnings = max(max_cryptocents[i][j] for i in range(1, K+1) for j in range(1000000000 + 1))

# Print the result
print(max_earnings)