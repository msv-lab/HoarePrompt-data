#State of the program right berfore the function call: d is an integer such that 0 <= d <= n - 1, where n is the number of vertices in the graph.
def func_1(d):
    print(f'? {d}')
    #This is printed: ? [d] (where d is an integer such that 0 <= d <= n - 1, and n is the number of vertices in the graph)
    sys.stdout.flush()
    v, u = map(int, input().split())
    return v, u
    #The program returns the values of `v` and `u`, which are integers provided by the user input.
#Overall this is what the function does:The function `func_1` accepts an integer `d` within the range of 0 to n-1, where n is the number of vertices in the graph. It prints a question mark followed by the value of `d` to the standard output. After flushing the output, it reads a line of input from the user, expecting two integers separated by a space. It then returns these two integers as a tuple `(v, u)`.

