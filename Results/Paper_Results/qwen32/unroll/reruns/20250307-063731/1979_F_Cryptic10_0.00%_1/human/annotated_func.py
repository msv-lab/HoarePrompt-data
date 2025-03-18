#State of the program right berfore the function call: d is a non-negative integer such that 0 <= d <= n - 1, where n is the number of vertices in the graph.
def func_1(d):
    print(f'? {d}')
    #This is printed: ? [d] (where d is a non-negative integer such that 0 <= d <= n - 1, and n is the number of vertices in the graph)
    sys.stdout.flush()
    v, u = map(int, input().split())
    return v, u
    #The program returns the tuple (v, u) where v and u are the two integers provided as input.
#Overall this is what the function does:The function accepts a non-negative integer `d` within the range of 0 to `n-1` (where `n` is the number of vertices in a graph) and returns a tuple `(v, u)` consisting of two integers provided as input.

#State of the program right berfore the function call: n is a positive integer representing the number of vertices in the graph, where 2 <= n <= 10^5.
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
        
    #State: - `n`: Remains unchanged as it is not modified within the loop.
    #- `path`: Contains all the vertices from `1` to `n` in the order they were removed from `remaining_vertices`.
    #- `remaining_vertices`: Is an empty set because all vertices have been removed.
    #
    #Output State:
    print(f"! {' '.join(map(str, path))}")
    #This is printed: ! [space-separated vertices from 1 to n in the order they were removed from remaining_vertices]
    sys.stdout.flush()
#Overall this is what the function does:The function `func_2` accepts a positive integer `n` representing the number of vertices in a graph, where `2 <= n <= 10^5`. It constructs a path that includes all vertices from `1` to `n` in a specific order by iteratively selecting vertices and removing them from a set of remaining vertices. The function prints a line starting with an exclamation mark followed by the space-separated vertices in the order they were removed.

