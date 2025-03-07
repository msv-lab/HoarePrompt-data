#State of the program right berfore the function call: d is a non-negative integer such that 0 <= d <= n - 1, where n is the number of vertices in the graph.
def func_1(d):
    print(f'? {d}')
    #This is printed: ? [d] (where d is a non-negative integer such that 0 <= d <= n - 1, and n is the number of vertices in the graph)
    sys.stdout.flush()
    v, u = map(int, input().split())
    return v, u
    #The program returns the values of `v` and `u`, where `v` and `u` are input integers.
#Overall this is what the function does:The function `func_1` accepts a non-negative integer `d` within the range of 0 to n-1, where n is the number of vertices in a graph. It prints a query string in the format `? d` and then reads two integers `v` and `u` from the standard input. The function returns these two integers `v` and `u`.

#State of the program right berfore the function call: n is a non-negative integer such that 2 <= n <= 10^5, and represents the number of vertices in the graph.
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
        
    #State: The loop will continue to execute until `remaining_vertices` is empty. After all iterations, `path` will contain all the integers from 1 to `n` (inclusive) in some order, and `remaining_vertices` will be an empty set. The value of `d` will be 0.
    print(f"! {' '.join(map(str, path))}")
    #This is printed: ! 1 2 3 ... n (where n is the last integer in the path list, and the integers are in some order from 1 to n)
    sys.stdout.flush()
#Overall this is what the function does:The function `func_2` accepts a non-negative integer `n` (where 2 <= n <= 10^5) representing the number of vertices in a graph. It constructs a path that includes all integers from 1 to `n` in some order. After the function completes, it prints the path in the format "! 1 2 3 ... n" (with the integers in some order from 1 to `n`), and flushes the output buffer. The function does not return any value.

