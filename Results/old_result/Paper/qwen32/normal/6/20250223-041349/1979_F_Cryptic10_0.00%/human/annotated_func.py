#State of the program right berfore the function call: d is a non-negative integer such that 0 <= d <= n - 1, where n is the number of vertices in the graph.
def func_1(d):
    print(f'? {d}')
    #This is printed: ? [d] (where d is a non-negative integer such that 0 <= d <= n - 1)
    sys.stdout.flush()
    v, u = map(int, input().split())
    return v, u
    #The program returns the integers `v` and `u` that were read from the input.
#Overall this is what the function does:The function `func_1` accepts a non-negative integer `d` as input and returns two integers `v` and `u` that are read from the input.

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
        
    #State: `n` is a positive integer representing the number of vertices in the graph, where 2 <= n <= 10^5; `path` is a list containing all vertices from 1 to n in the order they were found and added to `path`; `remaining_vertices` is an empty set.
    print(f"! {' '.join(map(str, path))}")
    #This is printed: ! 1 2 3 ... n (where n is the number of vertices in the graph and the numbers are the vertices in the path list in order)
    sys.stdout.flush()
#Overall this is what the function does:The function `func_2` takes a positive integer `n` representing the number of vertices in a graph (where 2 <= n <= 10^5) and prints a path of vertices from 1 to n in a specific order. The function does not return any value explicitly but outputs a string starting with '!' followed by the vertices in the order they were added to the path.

