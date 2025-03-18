#State of the program right berfore the function call: d is an integer such that 0 <= d <= n - 1, where n is the number of vertices in the graph.
def func_1(d):
    print(f'? {d}')
    #This is printed: ? [d]
    sys.stdout.flush()
    v, u = map(int, input().split())
    return v, u
    #The program returns two values, `v` and `u`, where `v` is an input integer and `u` is another input integer.
#Overall this is what the function does:The function accepts an integer `d` within a specific range (0 to n-1, where n is the number of vertices in the graph), prints `d`, reads two integers `v` and `u` from the standard input, and returns these two integers.

