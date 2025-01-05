#State of the program right berfore the function call: **
def func():
    f = lambda : list(map(int, input().split()))
    N, M, R = f()
    r = f()
    a, b, c = zip(*map(f, [0] * M))
    a = csgraph.dijkstra(csr_matrix((c, (a, b)), [N + 1] * 2), 0, r)
    print(int(min(sum(a[e[i]][r[e[i + 1]]] for i in range(R - 1)) for e in
    __import__('itertools').permutations(range(R)))))
#Overall this is what the function does:The function reads input values N, M, R, r, a, b, and c from the user. It then performs various operations on these inputs without accepting any explicit parameters. The function calculates the shortest path using Dijkstra's algorithm, and then computes the minimum cost based on permutations of the given inputs. The final output is printed as an integer. The function does not have a return value.

