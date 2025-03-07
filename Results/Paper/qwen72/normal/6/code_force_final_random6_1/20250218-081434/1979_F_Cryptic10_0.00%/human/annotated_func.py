#State of the program right berfore the function call: d is a non-negative integer such that 0 <= d <= n - 1, where n is the number of vertices in the graph.
def func_1(d):
    print(f'? {d}')
    #This is printed: ? [d] (where d is a non-negative integer such that 0 <= d <= n - 1, and n is the number of vertices in the graph)
    sys.stdout.flush()
    v, u = map(int, input().split())
    return v, u
    #The program returns the integers `v` and `u` provided by the user input.
#Overall this is what the function does:The function `func_1` accepts a parameter `d`, which is a non-negative integer. It prints a query string in the format "? d" to the console and flushes the output buffer to ensure immediate printing. The function then reads a line of input from the user, expects it to contain two integers separated by a space, and returns these two integers as a tuple `(v, u)`. The function does not modify the input parameter `d` or any other external state.

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
        
    #State: `n` is an integer such that 2 <= n <= 10^5, `path` contains all vertices from 1 to n (inclusive) in some order, and `remaining_vertices` is an empty set.
    print(f"! {' '.join(map(str, path))}")
    #This is printed: ! 1 2 3 ... n (where 1 2 3 ... n is the space-separated list of all integers from 1 to n in the order they appear in the `path` list)
    sys.stdout.flush()
#Overall this is what the function does:The function `func_2` accepts an integer `n` (2 <= n <= 10^5) representing the number of vertices in a graph. It constructs a path that includes all vertices from 1 to `n` in some order and prints this path as a space-separated list of integers. After the function concludes, `n` remains unchanged, `path` contains all vertices from 1 to `n` in the order they were added, and `remaining_vertices` is an empty set.

