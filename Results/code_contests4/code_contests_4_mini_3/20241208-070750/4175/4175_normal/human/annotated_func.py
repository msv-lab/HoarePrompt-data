#State of the program right berfore the function call: N is an integer such that 2 ≤ N ≤ 200, M is an integer such that 1 ≤ M ≤ N×(N-1)/2, R is an integer such that 2 ≤ R ≤ min(8, N), r_i are integers representing towns such that 1 ≤ r_i ≤ N and r_i are all distinct, A_i and B_i are integers representing roads such that 1 ≤ A_i, B_i ≤ N and A_i ≠ B_i, and C_i is an integer representing the length of the road such that 1 ≤ C_i ≤ 100000.
def func():
    f = lambda : list(map(int, input().split()))
    N, M, R = f()
    r = f()
    a, b, c = zip(*map(f, [0] * M))
    a = csgraph.dijkstra(csr_matrix((c, (a, b)), [N + 1] * 2), 0, r)
    print(int(min(sum(a[e[i]][r[e[i + 1]]] for i in range(R - 1)) for e in
    __import__('itertools').permutations(range(R)))))
#Overall this is what the function does:The function reads input values for the number of towns (N), the number of roads (M), and the number of distinct towns to visit (R), along with the specific towns and the roads connecting them. It then calculates the shortest paths between the specified towns using Dijkstra's algorithm and computes the minimum total distance required to visit all specified towns in every possible order. The function does not return any value; it directly prints the result.

