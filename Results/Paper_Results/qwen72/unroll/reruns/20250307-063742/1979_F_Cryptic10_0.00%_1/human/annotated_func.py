#State of the program right berfore the function call: d is an integer such that 0 <= d <= n - 1, where n is the number of vertices in the graph.
def func_1(d):
    print(f'? {d}')
    #This is printed: ? [d] (where d is an integer such that 0 <= d <= n - 1)
    sys.stdout.flush()
    v, u = map(int, input().split())
    return v, u
    #The program returns the integers `v` and `u` provided by the user.
#Overall this is what the function does:The function `func_1` accepts an integer `d` within the range 0 to n-1, where n is the number of vertices in the graph. It prints a query string in the format "? d" to the standard output and then reads two integers `v` and `u` from the user input. The function returns these two integers `v` and `u`.

#State of the program right berfore the function call: n is an integer such that 2 <= n <= 10^5, and remaining_vertices is a set of integers representing the vertices of the graph that have not been removed yet.
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
        
    #State: `remaining_vertices` is an empty set, `path` is a list containing integers from 1 to n in some order.
    print(f"! {' '.join(map(str, path))}")
    #This is printed: - Since `path` is a list containing integers from 1 to n in some order, the output will be a string that starts with `!` followed by these integers separated by spaces.
    #   - For example, if `path` is `[1, 3, 2, 4]`, the output will be `! 1 3 2 4`.
    #
    #Output:
    sys.stdout.flush()
#Overall this is what the function does:The function `func_2` accepts an integer `n` (where 2 <= n <= 10^5) and initializes a set `remaining_vertices` containing integers from 1 to `n`. It constructs a list `path` by iteratively selecting and removing vertices from `remaining_vertices` based on the output of `func_1`. After all vertices are removed, the function prints a string that starts with `!` followed by the integers in `path` separated by spaces. The final state of the program is that `remaining_vertices` is an empty set, and `path` contains integers from 1 to `n` in some order. The function does not return any value.

