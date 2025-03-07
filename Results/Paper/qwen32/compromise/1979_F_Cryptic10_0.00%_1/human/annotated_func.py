#State of the program right berfore the function call: d is a non-negative integer such that 0 <= d <= n - 1, where n is the number of vertices in the graph.
def func_1(d):
    print(f'? {d}')
    #This is printed: ? [d] (where d is a non-negative integer such that 0 <= d <= n - 1, and n is the number of vertices in the graph)
    sys.stdout.flush()
    v, u = map(int, input().split())
    return v, u
    #The program returns the first integer from the input, `v`, and the second integer from the input, `u`.
#Overall this is what the function does:The function accepts a non-negative integer `d` within the range of 0 to `n-1`, where `n` is the number of vertices in a graph. It prints a query with `d` and then reads two integers from the input, returning them as a tuple `(v, u)`.

#State of the program right berfore the function call: n is a positive integer representing the number of vertices in the graph, and it is guaranteed that 2 <= n <= 10^5.
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
        
    #State: `path` is a list containing all vertices from 1 to n in some order, and `remaining_vertices` is an empty set.
    print(f"! {' '.join(map(str, path))}")
    #This is printed: ! 1 2 3 ... n (where 1 2 3 ... n are the vertices in the order they appear in the path list)
    sys.stdout.flush()
#Overall this is what the function does:The function `func_2` accepts a positive integer `n` representing the number of vertices in a graph, with the constraint that 2 <= n <= 100,000. It constructs a path that includes all vertices from 1 to n in some order and prints this path prefixed with an exclamation mark. After execution, the function outputs the vertices in the order they appear in the path list, ensuring all vertices are included exactly once.

