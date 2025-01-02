#State of the program right berfore the function call: The input consists of two integers n and m, followed by m lines, each containing three integers ui, vi, and wi, indicating a directed edge from vertex ui to vertex vi with weight wi. The graph does not contain self-loops or multiple edges, and the weights are positive integers not exceeding 10^5.
def func():
    rints = lambda : [int(x) for x in stdin.readline().split()]
    rints_2d = lambda n: [rints() for _ in range(n)]
    n, m = rints()
    mem, edges, weight = [0] * (n + 1), rints_2d(m), [[] for _ in range(10 ** 5 +
    1)]
    for (u, v, w) in edges:
        weight[w].append((u, v))
        
    #State of the program after the  for loop has been executed: `n` is an integer, `m` is a non-negative integer, `edges` is a 2D list with `m` rows where each row is a tuple of three integers, `mem` is a list of `n + 1` zeros, `weight` is a list of 100001 empty lists, where for each `w` in the `edges` list, the list `weight[w]` contains tuples `(u, v)` for each edge specified in the `edges` list.
    for i in range(1, 10 ** 5 + 1):
        all = [(v, mem[u]) for u, v in weight[i]]
        
        for v, du in all:
            mem[v] = max(mem[v], du + 1)
        
    #State of the program after the  for loop has been executed: `i` is 100001, `all` is an empty list, `mem[v]` is the maximum value of `du + 1` for each tuple `(v, du)` in `all` for all `v` in `mem`.
    print(max(mem))
#Overall this is what the function does:The function reads a directed graph with `n` vertices and `m` edges, where each edge is defined by a pair of vertices `(u, v)` and a positive integer weight `w`. It then computes the maximum distance from vertex 1 to every other vertex in the graph using a modified breadth-first search approach. The function stores these distances in the `mem` array and finally returns the maximum distance found. If the graph is disconnected or contains isolated vertices, the function still processes them according to the given rules. However, note that the function does not handle negative weights or self-loops explicitly, as per the problem statement.

