#State of the program right berfore the function call: d is a non-negative integer such that 0 <= d <= n - 1, where n is the number of vertices in the graph.
def func_1(d):
    print(f'? {d}')
    #This is printed: ? [d] (where d is a non-negative integer such that 0 <= d <= n - 1)
    sys.stdout.flush()
    v, u = map(int, input().split())
    return v, u
    #The program returns the tuple (v, u), where v is the first integer from the input and u is the second integer from the input.
#Overall this is what the function does:The function `func_1` accepts a non-negative integer `d` within the range of 0 to `n - 1`, where `n` is the number of vertices in a graph. It prints a query with the value of `d`, then reads a line of input expecting two integers, and returns these two integers as a tuple `(v, u)`.

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
        
    #State: `n` is a positive integer representing the number of vertices in the graph, where 2 <= n <= 10^5; `path` is a list containing all the vertices from the original set of remaining vertices in the order they were added; `remaining_vertices` is an empty set.
    print(f"! {' '.join(map(str, path))}")
    #This is printed: ! [vertices in path separated by spaces] (where vertices in path are the elements of the path list in order)
    sys.stdout.flush()
#Overall this is what the function does:The function `func_2` accepts a positive integer `n` representing the number of vertices in a graph, where `2 <= n <= 10^5`. It constructs a path by iteratively selecting vertices from the set of remaining vertices until all vertices are included in the path. The function then prints the path in the format `! [vertices in path separated by spaces]`.

