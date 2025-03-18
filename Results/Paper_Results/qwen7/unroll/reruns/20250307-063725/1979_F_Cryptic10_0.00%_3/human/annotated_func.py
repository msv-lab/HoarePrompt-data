#State of the program right berfore the function call: d is an integer such that 0 <= d <= n - 1, where n is the number of vertices in the graph.
def func_1(d):
    print(f'? {d}')
    #This is printed: ? [d] (where d is an integer such that 0 ≤ d ≤ n - 1)
    sys.stdout.flush()
    v, u = map(int, input().split())
    return v, u
    #The program returns v and u, where v and u are input integers.
#Overall this is what the function does:The function accepts an integer `d` within the range of 0 to n-1, prints `d`, reads two integers `v` and `u` from the standard input, and returns these two integers `v` and `u`.

#State of the program right berfore the function call: n is an integer such that 2 <= n <= 10^5. The variable `remaining_vertices` is a set containing integers from 1 to n, representing the vertices that have not been removed yet. The function `func_1(d)` is expected to return a tuple `(v, u)` where `v` is the vertex with the minimum degree at least `d` (or 0 if no such vertex exists), and `u` is the vertex that `v` is not connected to (or 0 if no such vertex exists).
def func_2(n):
    path = []
    remaining_vertices = set(range(1, n + 1))
    while remaining_vertices:
        for d in range(n - 1, -1, -1):
            v, u = func_1(d)
            if v == 0:
                continue
            if v in remaining_vertices:
                path.append(v)
                remaining_vertices.remove(v)
                break
        
    #State: The `path` list contains a sequence of vertices from the set {1, 2, ..., n}, and the `remaining_vertices` set is empty.
    print(f"! {' '.join(map(str, path))}")
    #This is printed: ! [sequence of vertices from the set {1, 2, ..., n}]
    sys.stdout.flush()
#Overall this is what the function does:The function `func_2` accepts an integer `n` (where 2 ≤ n ≤ 10^5) and returns a sequence of vertices represented as a list of integers. It constructs a path by iteratively selecting vertices based on their degrees, ensuring each selected vertex has the minimum degree that meets the criteria specified by `d`. The function removes selected vertices from a set of remaining vertices until all vertices are processed. Finally, it prints the constructed path and flushes the output buffer.

