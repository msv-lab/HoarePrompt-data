#State of the program right berfore the function call: d is an integer such that 0 <= d <= n - 1, where n is the number of vertices in the graph.
def func_1(d):
    print(f'? {d}')
    #This is printed: ? d (where d is an integer such that 0 <= d <= n - 1)
    sys.stdout.flush()
    v, u = map(int, input().split())
    return v, u
    #The program returns two values, `v` and `u`, where `v` is an input integer and `u` is another input integer.
#Overall this is what the function does:The function accepts an integer `d` within the range of 0 to n-1, where n is the number of vertices in the graph. It then reads two integers `v` and `u` from user input and returns these two integers.

#State of the program right berfore the function call: n is an integer such that 2 <= n <= 10^5.
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
        
    #State: Output State: `d` is -1, `v` is the return value of `func_1(-1)` after all iterations, `u` is the second return value of `func_1(-1)` after all iterations, `path` contains all vertices that satisfy the given conditions, and `remaining_vertices` is an empty set since all vertices from 1 to `n` have been processed and added to `path`.
    #
    #In this final state, the loop has completed all its iterations, meaning it has iterated through all possible values of `d` from `n-1` down to `-1`. The variable `d` will have reached `-1`, indicating the end of the loop. The variable `v` will hold the last value returned by `func_1(-1)`, and `u` will hold the corresponding second return value. The `path` list will contain all the vertices that met the condition of being in `remaining_vertices` and were successfully appended to `path` before being removed from `remaining_vertices`. Finally, `remaining_vertices` will be an empty set because all vertices from 1 to `n` have been processed.
    print(f"! {' '.join(map(str, path))}")
    #This is printed: ! path (where path contains all vertices that satisfied the given conditions)
    sys.stdout.flush()
#Overall this is what the function does:The function `func_2` accepts an integer `n` and constructs a path containing all vertices from 1 to `n` that satisfy certain conditions. It uses a loop to iterate through possible values of `d` from `n-1` down to `-1`, calling another function `func_1(d)` to get pairs of vertices `(v, u)`. If `v` is found in the set of remaining vertices, it is added to the path and removed from the set. After processing all vertices, it prints the path and ensures the set of remaining vertices is empty.

