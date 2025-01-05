#State of the program right berfore the function call: **
def func():
    f = lambda : list(map(int, input().split()))
    N, M, R = f()
    r = f()
    a, b, c = zip(*map(f, [0] * M))
    a = csgraph.dijkstra(csr_matrix((c, (a, b)), [N + 1] * 2), 0, r)
    print(int(min(sum(a[e[i]][r[e[i + 1]]] for i in range(R - 1)) for e in
    __import__('itertools').permutations(range(R)))))
#Overall this is what the function does:The function does not accept any parameters and performs a series of operations involving input reading, matrix manipulation, and permutation calculations. It calculates the shortest path using Dijkstra's algorithm and prints the minimum sum of distances between points based on permutations. The actual return value is not explicitly defined in the code, so it does not return "Hello, World!" as mentioned in the annotations.

