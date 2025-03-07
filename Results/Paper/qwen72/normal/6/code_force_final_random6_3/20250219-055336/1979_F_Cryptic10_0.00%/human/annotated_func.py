#State of the program right berfore the function call: d is a non-negative integer such that 0 <= d <= n - 1, where n is the number of vertices in the graph.
def func_1(d):
    print(f'? {d}')
    #This is printed: ? [d] (where d is a non-negative integer such that 0 <= d <= n - 1, and n is the number of vertices in the graph)
    sys.stdout.flush()
    v, u = map(int, input().split())
    return v, u
    #The program returns the integers `v` and `u` provided by the user.
#Overall this is what the function does:The function `func_1` accepts a non-negative integer `d` within the range of 0 to n-1, where n is the number of vertices in a graph. It prints a query string in the format `? d` to the standard output and then reads two integers `v` and `u` from the user input. The function returns these two integers `v` and `u`. After the function concludes, the program has printed the query and received and returned the two integers provided by the user.

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
        
    #State: `n` is an integer such that 2 <= n <= 10^5, `path` is a list that includes all vertices from the initial `remaining_vertices` set, and `remaining_vertices` is an empty set.
    print(f"! {' '.join(map(str, path))}")
    #This is printed: !
    sys.stdout.flush()
#Overall this is what the function does:The function `func_2` accepts an integer `n` (where 2 <= n <= 10^5) representing the number of vertices in a graph. It constructs a path that includes all vertices from 1 to `n` and prints this path in the format "! 1 2 3 ... n". After the function concludes, `path` contains all vertices from 1 to `n` in some order, and `remaining_vertices` is an empty set. The function does not return any value.

