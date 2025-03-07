#State of the program right berfore the function call: d is a non-negative integer such that 0 <= d <= n - 1, where n is the number of vertices in the graph.
def func_1(d):
    print(f'? {d}')
    #This is printed: ? [d] (where d is a non-negative integer such that 0 <= d <= n - 1, and n is the number of vertices in the graph)
    sys.stdout.flush()
    v, u = map(int, input().split())
    return v, u
    #The program returns the integers `v` and `u` provided by the user input.
#Overall this is what the function does:The function `func_1` accepts a parameter `d`, which is a non-negative integer within the range of 0 to n-1, where n is the number of vertices in the graph. It prints a query string in the format `? d` and then reads a line of input from the user, expecting two integers separated by a space. The function returns these two integers as a tuple `(v, u)`.

