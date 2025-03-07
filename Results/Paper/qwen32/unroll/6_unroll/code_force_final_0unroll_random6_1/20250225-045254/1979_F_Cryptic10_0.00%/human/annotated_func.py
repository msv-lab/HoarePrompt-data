#State of the program right berfore the function call: d is a non-negative integer such that 0 <= d <= n - 1, where n is the number of vertices in the graph.
def func_1(d):
    print(f'? {d}')
    #This is printed: ? [d] (where d is a non-negative integer such that 0 <= d <= n - 1, and n is the number of vertices in the graph)
    sys.stdout.flush()
    v, u = map(int, input().split())
    return v, u
    #The program returns a tuple containing the integer `v` and the integer `u`.
#Overall this is what the function does:The function accepts a non-negative integer `d` within the range of 0 to `n-1`, where `n` is the number of vertices in a graph. It prints a query with the value of `d` and then reads two integers `v` and `u` from the input. Finally, it returns a tuple containing the integers `v` and `u`.

