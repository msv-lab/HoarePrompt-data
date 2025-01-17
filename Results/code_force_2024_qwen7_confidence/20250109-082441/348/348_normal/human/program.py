from collections import *
from heapq import *
import sys

input = sys.stdin.readline
INF = 1 << 60  # A large number representing infinity

def dijkstra(start, edges):
    N = len(edges)
    dist = [INF] * N  # Distance array initialized to infinity
    dist[start] = 0  # Starting node distance is 0
    heap = []
    heappush(heap, start)  # Push the starting node into the heap

    while heap:
        current_weight, current_node = divmod(heappop(heap), N)
        if dist[current_node] != current_weight:
            continue
        for neighbor, cost in edges[current_node]:
            new_cost = cost + current_weight
            if new_cost < dist[neighbor]:
                dist[neighbor] = new_cost
                heappush(heap, new_cost * N + neighbor)
    return dist

def answer():
    N, M = map(int, input().split())
    edges = [[] for _ in range(N * (M + 1))]
    costs = list(map(int, input().split()))
    attributes = [list(map(int, input().split())) for _ in range(N)]

    for i in range(M):
        # Sort Pokémon based on the i-th attribute
        sorted_pokemon = [(attributes[j][i], j) for j in range(N)]
        sorted_pokemon.sort(reverse=True)

        for j in range(N):
            # Create edges for hiring Pokémon
            _j = j + (i + 1) * N
            edges[j].append((_j, costs[j]))
            edges[_j].append((j, 0))

        for j in range(N - 1):
            # Create edges for attribute increase
            vi, idx = sorted_pokemon[j]
            vj, jdx = sorted_pokemon[j + 1]
            _idx = idx + (i + 1) * N
            _jdx = jdx + (i + 1) * N
            edges[_idx].append((_jdx, 0))
            edges[_jdx].append((_idx, vi - vj))

    # Find the minimum cost to reach the nth Pokémon
    distances = dijkstra(N - 1, edges)
    print(distances[0])

# Process each test case
for _ in range(int(input())):
    answer()