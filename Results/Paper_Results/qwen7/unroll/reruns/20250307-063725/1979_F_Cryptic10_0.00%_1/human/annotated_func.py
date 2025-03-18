#State of the program right berfore the function call: d is an integer such that 0 <= d <= n - 1, where n is the number of vertices in the graph.
def func_1(d):
    print(f'? {d}')
    #This is printed: ? d
    sys.stdout.flush()
    v, u = map(int, input().split())
    return v, u
    #The program returns v and u, where v is an input integer and u is another input integer.
#Overall this is what the function does:The function `func_1` accepts an integer `d` within the range [0, n-1] and reads two integers `v` and `u` from standard input. It then returns these two integers `v` and `u`.

#State of the program right berfore the function call: n is an integer such that 2 <= n <= 10^5. The variable `remaining_vertices` is a set containing integers from 1 to n, representing the vertices that have not been removed yet. The function `func_1(d)` is a helper function that returns a tuple (v, u), where v is the vertex with the minimum degree at least d (or 0 if no such vertex exists), and u is the vertex not connected to v (or 0 if no such vertex exists).
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
        
    #State: The `path` list contains some or all of the integers from 1 to n, and the `remaining_vertices` set is empty.
    print(f"! {' '.join(map(str, path))}")
    #This is printed: ! [element1] [element2] ... [elementN]
    sys.stdout.flush()
#Overall this is what the function does:The function `func_2(n)` accepts an integer `n` such that 2 ≤ n ≤ 10^5. It processes a set of vertices from 1 to n, removing them one by one based on their degrees using a helper function `func_1(d)`. After processing, it prints a list of the removed vertices in the order they were processed. The function does not return any value.

