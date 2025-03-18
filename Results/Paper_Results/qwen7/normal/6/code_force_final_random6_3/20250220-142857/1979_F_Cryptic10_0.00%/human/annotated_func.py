#State of the program right berfore the function call: d is an integer such that 0 <= d <= n - 1, where n is the number of vertices in the graph.
def func_1(d):
    print(f'? {d}')
    #This is printed: ? [d]
    sys.stdout.flush()
    v, u = map(int, input().split())
    return v, u
    #The program returns v and u, where v is an input integer and u is also an input integer.
#Overall this is what the function does:The function `func_1` accepts an integer `d` within the range [0, n-1] and reads two integers `v` and `u` from the standard input. It then returns these two integers `v` and `u`.

#State of the program right berfore the function call: n is an integer such that 2 <= n <= 10^5. The variable `remaining_vertices` is a set containing integers from 1 to n, representing the vertices that have not been removed yet. The function `func_1(d)` is expected to return a tuple `(v, u)` where `v` is the vertex with the minimum degree at least `d` (or 0 if no such vertex exists), and `u` is the vertex that is not connected to `v` (or 0 if no such vertex exists).
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
        
    #State: Output State: The final state of the loop will be such that `path` contains all vertices from 1 to n, added in descending order from the highest index `d` down to 0. The `remaining_vertices` set will be empty since every vertex that was present initially has been removed from it and added to `path`. The value of `d` will be -1 after the loop completes, as the loop iterates over `range(n - 1, -1, -1)` and decrements `d` in each iteration until it reaches -1.
    print(f"! {' '.join(map(str, path))}")
    #This is printed: ! n n-1 ... 2 1
    sys.stdout.flush()
#Overall this is what the function does:The function `func_2` accepts an integer `n` representing the number of vertices in a graph. It constructs a path by iteratively selecting vertices based on their degrees and removing them from the set of remaining vertices. The path is constructed in such a way that it includes all vertices from 1 to n, added in descending order from the highest index `d` down to 0. After processing, the function prints the path as a sequence of vertices, starting from n and ending at 1. The function does not return any value; instead, it prints the path directly.

