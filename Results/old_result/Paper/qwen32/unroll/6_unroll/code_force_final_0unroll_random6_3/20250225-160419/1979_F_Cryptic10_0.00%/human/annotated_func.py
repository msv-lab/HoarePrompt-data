#State of the program right berfore the function call: d is a non-negative integer such that 0 <= d <= n - 1, where n is the number of vertices in the graph.
def func_1(d):
    print(f'? {d}')
    #This is printed: ? [d] (where [d] is a non-negative integer such that 0 <= d <= n - 1)
    sys.stdout.flush()
    v, u = map(int, input().split())
    return v, u
    #The program returns a tuple containing the integers `v` and `u`.
#Overall this is what the function does:The function `func_1` accepts a non-negative integer `d` and returns a tuple containing two integers `v` and `u`, which are obtained from user input.

