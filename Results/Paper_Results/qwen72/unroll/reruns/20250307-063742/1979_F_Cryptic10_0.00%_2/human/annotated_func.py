#State of the program right berfore the function call: d is an integer such that 0 <= d <= n - 1, where n is the number of vertices in the graph.
def func_1(d):
    print(f'? {d}')
    #This is printed: ? [d] (where d is an integer such that 0 <= d <= n - 1)
    sys.stdout.flush()
    v, u = map(int, input().split())
    return v, u
    #The program returns the integers `v` and `u` provided by the user input.
#Overall this is what the function does:The function `func_1` accepts an integer `d` within the range 0 to n-1 (inclusive), where n is the number of vertices in the graph. It prints a query string in the format `? [d]` to the standard output and then reads a line of input from the user, expecting two integers separated by a space. The function returns these two integers as a tuple `(v, u)`. After the function concludes, the program state includes the printed query and the returned tuple of integers `(v, u)` provided by the user input.

#State of the program right berfore the function call: n is an integer such that 2 <= n <= 10^5, representing the number of vertices in the graph.
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
        
    #State: `path` contains a sequence of vertices, and `remaining_vertices` is an empty set.
    print(f"! {' '.join(map(str, path))}")
    #This is printed: ! [space-separated vertices in path] (where [space-separated vertices in path] is the sequence of vertices in the `path` list, each separated by a space)
    sys.stdout.flush()
#Overall this is what the function does:The function `func_2` accepts an integer `n` (where 2 <= n <= 10^5) representing the number of vertices in a graph. It constructs a path by iteratively selecting vertices and adding them to the path until all vertices are included. The function then prints the path as a sequence of space-separated vertex numbers and flushes the output buffer. After the function concludes, the `path` contains a sequence of all vertices, and the `remaining_vertices` set is empty.

