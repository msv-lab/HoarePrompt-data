#State of the program right berfore the function call: d is a non-negative integer such that 0 <= d <= n - 1, where n is the number of vertices in the graph.
def func_1(d):
    print(f'? {d}')
    #This is printed: ? [d] (where d is a non-negative integer such that 0 <= d <= n - 1)
    sys.stdout.flush()
    v, u = map(int, input().split())
    return v, u
    #The program returns the tuple (v, u), where v and u are the two integers provided by the input.
#Overall this is what the function does:The function `func_1` accepts a non-negative integer `d` as a parameter, which is within the range from 0 to `n-1` (where `n` is the number of vertices in a graph). It prints a query with the value of `d`, flushes the output, and then reads two integers `v` and `u` from the input. The function returns a tuple containing these two integers.

#State of the program right berfore the function call: n is an integer representing the number of vertices in the graph, where 2 <= n <= 10^5.
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
        
    #State: `path` is a permutation of `[1, 2, ..., n]` and `remaining_vertices` is an empty set.
    print(f"! {' '.join(map(str, path))}")
    #This is printed: ! 1 2 ... n (where [1, 2, ..., n] is a permutation of the list [1, 2, ..., n])
    sys.stdout.flush()
#Overall this is what the function does:The function `func_2` takes an integer `n` representing the number of vertices in a graph and outputs a permutation of the integers from 1 to `n`. The output is printed in the format `! 1 2 ... n`, where `[1, 2, ..., n]` is a permutation of the list `[1, 2, ..., n]`.

