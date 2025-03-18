#State of the program right berfore the function call: t is an integer such that 1 <= t <= 100, and for each test case, n and m are integers such that 1 <= n, m <= 100.
def func_1():
    n, m = map(int, input().split())
    if ((n - m) % 2 == 0 and n - m >= 0) :
        print('Yes')
        #This is printed: Yes
    else :
        print('No')
        #This is printed: No
    #State: t is an integer such that 1 <= t <= 100; n and m are integers such that 1 <= n, m <= 100. If (n - m) is even and non-negative, then n is greater than or equal to m with the difference (n - m) being an even number. Otherwise, either (n - m) is not even or (n - m) is negative.
#Overall this is what the function does:The function reads two integers `n` and `m` for each of `t` test cases. For each test case, it checks if the difference `n - m` is even and non-negative. If so, it prints 'Yes'; otherwise, it prints 'No'.

