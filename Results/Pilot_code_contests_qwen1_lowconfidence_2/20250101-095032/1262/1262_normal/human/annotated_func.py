#State of the program right berfore the function call: N is an integer such that 2 <= N <= 100, and W is a list of N integers such that 1 <= W_i <= 100 for all i in range(N).
def func():
    N = input()
    V = list(map(int, input().split()))
    M = 1000000000.0
    for i in range(1, len(V)):
        diff = abs(sum(V[:i]) - sum(V[i:]))
        
        if M > diff:
            M = diff
        
    #State of the program after the  for loop has been executed: `N` is the length of the input list `V`, `W` is equal to `V`, `M` is the minimum absolute difference between the sums of any two parts of the list `V` that split the list into two non-empty parts.
    print(M)
#Overall this is what the function does:The function `func()` accepts no explicit parameters; instead, it reads an integer `N` and a list `V` of `N` integers from standard input. It then calculates and prints the minimum absolute difference between the sums of any two parts of the list `V` that split the list into two non-empty parts. If the inputs do not meet the constraints (i.e., `N` is not between 2 and 100 inclusive, or the elements of `V` are not between 1 and 100 inclusive), the function will not properly execute the intended logic and may produce incorrect results or errors. However, the function does not explicitly handle such invalid inputs, so the behavior in these cases is undefined.

