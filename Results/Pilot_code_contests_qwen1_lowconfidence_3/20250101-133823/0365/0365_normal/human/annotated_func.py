#State of the program right berfore the function call: The input consists of two integers n and m, where 2 ≤ n ≤ 3⋅10^5 and 1 ≤ m ≤ min(n⋅(n - 1), 3⋅10^5). Following these, m lines each contain three space-separated integers ui, vi, and wi, representing a directed edge from vertex ui to vertex vi with weight wi, where 1 ≤ ui, vi ≤ n and 1 ≤ wi ≤ 10^5. The graph does not contain self-loops or multiple edges.
def func():
    rints = lambda : [int(x) for x in stdin.readline().split()]
    rints_2d = lambda n: [rints() for _ in range(n)]
    n, m = rints()
    mem, edges, weight = [0] * (n + 1), rints_2d(m), [[] for _ in range(10 ** 5 +
    1)]
    for (u, v, w) in edges:
        weight[w].append((u, v))
        
    #State of the program after the  for loop has been executed: `edges` is a 2D list of size `m` (or potentially smaller if the loop did not fully iterate over all elements due to list modifications during iteration); `weight[w]` is a list of tuples representing all unique edge pairs `(u, v)` where `w` is the weight associated with those edges, `mem` remains a list of length `n + 1` filled with zeros, `edges` is a 2D list of size `m` that must have been fully processed if the loop completed successfully, `weight` is a list of lists where each index corresponds to a weight and contains tuples of edge pairs.
    for i in range(1, 10 ** 5 + 1):
        all = [(v, mem[u]) for u, v in weight[i]]
        
        for v, du in all:
            mem[v] = max(mem[v], du + 1)
        
    #State of the program after the  for loop has been executed: `total` is 0, `i` is `10
    print(max(mem))
#Overall this is what the function does:The function processes a directed graph represented by `n` vertices and `m` edges, where each edge has a weight between 1 and 10^5. It initializes an array `mem` to store the maximum distance (or path length) from a starting vertex to each vertex. For each possible edge weight, it constructs a list of tuples containing the destination vertex and the distance from the source vertex. It then iterates over these tuples to update the `mem` array, ensuring that `mem[v]` is the maximum value between its current value and the sum of `du + 1`, where `du` is the distance from the source vertex to the current vertex. After processing all possible edge weights, it prints the maximum value in the `mem` array, which represents the longest path from the starting vertex to any other vertex in the graph.

