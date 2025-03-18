#State of the program right berfore the function call: d is an integer such that 0 <= d <= n - 1, where n is the number of vertices in the graph.
def func_1(d):
    print(f'? {d}')
    #This is printed: ? [d] (where d is an integer such that 0 <= d <= n - 1, and n is the number of vertices in the graph)
    sys.stdout.flush()
    v, u = map(int, input().split())
    return v, u
    #The program returns the integers `v` and `u` provided by the user.
#Overall this is what the function does:The function `func_1` accepts an integer `d` within the range of 0 to `n-1` (inclusive), where `n` is the number of vertices in the graph. It prints a query string in the format `"? d"`. The function then reads a line of input from the user, expecting two integers separated by a space, and returns these integers as a tuple `(v, u)`. After the function concludes, the program state includes the printed query and the returned integers `v` and `u`.

#State of the program right berfore the function call: n is an integer such that 2 <= n <= 10^5, and `remaining_vertices` is a set of integers representing the vertices in the graph, initially containing all integers from 1 to n.
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
        
    #State: `remaining_vertices` is an empty set, and `path` is a list containing all integers from 1 to n in some order.
    print(f"! {' '.join(map(str, path))}")
    #This is printed: ! 1 2 3 ... n (where n is the length of the path list and the elements are all integers from 1 to n in some order)
    sys.stdout.flush()
#Overall this is what the function does:The function `func_2` accepts an integer `n` and operates on a set `remaining_vertices` initially containing integers from 1 to `n`. After the function concludes, `remaining_vertices` is an empty set, and a list `path` containing all integers from 1 to `n` in some order is printed to the console. The function does not return any value.

