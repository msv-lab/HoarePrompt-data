#State of the program right berfore the function call: d is an integer such that 0 <= d <= n - 1, where n is the number of vertices in the graph.
def func_1(d):
    print(f'? {d}')
    #This is printed: ? d (where d is an integer such that 0 <= d <= n - 1)
    sys.stdout.flush()
    v, u = map(int, input().split())
    return v, u
    #The program returns v and u, where v is an input integer and u is another input integer.
#Overall this is what the function does:The function accepts an integer `d` within the range 0 to n-1 and reads two integers `v` and `u` from user input. It then returns these two integers `v` and `u`.

