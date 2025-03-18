#State of the program right berfore the function call: d is a non-negative integer such that 0 <= d <= n - 1, where n is the number of vertices in the graph.
def func_1(d):
    print(f'? {d}')
    #This is printed: ? [d] (where d is a non-negative integer such that 0 <= d <= n - 1)
    sys.stdout.flush()
    v, u = map(int, input().split())
    return v, u
    #The program returns the tuple (v, u), where v and u are the two integers obtained from the input.
#Overall this is what the function does:The function `func_1` accepts a non-negative integer `d` as a parameter, which is within the range of 0 to `n - 1`, where `n` is the number of vertices in a graph. It prints a query with this integer, flushes the output, and then reads two integers from the input. The function returns these two integers as a tuple (v, u).

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
        
    #State: `remaining_vertices` is an empty set, and `path` is a list containing all integers from 1 to `n` in the order they were added.
    print(f"! {' '.join(map(str, path))}")
    #This is printed: ! 1 2 3 ... n (where n is the total number of integers in the path list, and path contains integers from 1 to n in the order they were added)
    sys.stdout.flush()
#Overall this is what the function does:The function `func_2` takes an integer `n` as input, representing the number of vertices in a graph, and prints a sequence of integers from 1 to `n` in a specific order determined by the internal logic of the function. The final state of the program is that all integers from 1 to `n` are printed in a single line, prefixed with an exclamation mark, and separated by spaces.

