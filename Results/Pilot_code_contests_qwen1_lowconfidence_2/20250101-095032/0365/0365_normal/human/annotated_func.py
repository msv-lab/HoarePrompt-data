#State of the program right berfore the function call: The input consists of two integers n and m, where 2 ≤ n ≤ 3·10^5 and 1 ≤ m ≤ min(n·(n - 1), 3·10^5). Following these, m lines each contain three space-separated integers ui, vi, and wi, where 1 ≤ ui, vi ≤ n and 1 ≤ wi ≤ 10^5, representing a directed edge from vertex ui to vertex vi with weight wi. It is guaranteed that the graph does not contain self-loops or multiple edges.
def func():
    rints = lambda : [int(x) for x in stdin.readline().split()]
    rints_2d = lambda n: [rints() for _ in range(n)]
    n, m = rints()
    mem, edges, weight = [0] * (n + 1), rints_2d(m), [[] for _ in range(10 ** 5 +
    1)]
    for (u, v, w) in edges:
        weight[w].append((u, v))
        
    #State of the program after the  for loop has been executed: `n` is an integer between 2 and \(3 \times 10^5\), `m` is equal to the number of edges, `mem` is a list of length `n + 1` with all elements initialized to 0, `edges` is a 2D list of size `m` with random integers, `weight` is a list of 10 sublists where each sublist `weight[i]` contains all tuples `(u, v)` such that the edge `(u, v)` has weight `i+1`.
    for i in range(1, 10 ** 5 + 1):
        all = [(v, mem[u]) for u, v in weight[i]]
        
        for v, du in all:
            mem[v] = max(mem[v], du + 1)
        
    #State of the program after the  for loop has been executed: `all` is a list containing pairs `(v, mem[u])` for each `(u, v)` in `weight[99999]`, `mem[v]` for each vertex `v` is the maximum value between its original value (0) and `du + 1` for each pair `(v, du)` encountered during all iterations of the loop, `i` is 100000.
    print(max(mem))
#Overall this is what the function does:The function reads a directed graph with `n` vertices and `m` edges from standard input, where each edge is defined by a source vertex `u`, a destination vertex `v`, and a weight `w`. It then computes the longest path (in terms of the number of edges) from the first vertex (vertex 1) to all other vertices in the graph, using a dynamic programming approach. The function initializes a `mem` array to store the longest path lengths for each vertex, starting with 0 for all vertices. For each possible edge weight from 1 to 100000, it updates the `mem` array by considering all edges with that weight. Finally, it prints the maximum value in the `mem` array, which represents the longest path length from the first vertex to any other vertex in the graph. If there is no path from the first vertex to any other vertex, the output will be 0. This function handles the case where the graph does not contain self-loops or multiple edges, as stated in the problem description.

