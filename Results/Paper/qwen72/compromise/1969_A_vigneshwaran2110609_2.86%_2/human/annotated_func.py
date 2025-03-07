#State of the program right berfore the function call: t is an integer such that 1 <= t <= 5000; for each test case, n is an integer such that 2 <= n <= 50, and p is a list of n integers where 1 <= p_i <= n, p_i ≠ i, and all p_i are distinct.
def func():
    n = int(input())
    for i in range(n):
        x = int(input())
        
        l = list(map(int, input().strip().split()))
        
        for i in range(0, x):
            if l[l[i] - 1] == l[i] - 1:
                flag = True
                print(2)
                break
        else:
            print(3)
        
    #State: `t` is an integer such that 1 <= t <= 5000, `n` is an integer such that 2 <= n <= 50, `p` is a list of `n` integers where 1 <= p_i <= n, p_i ≠ i, and all p_i are distinct, `i` is `n-1`, `x` is an input integer, `l` is a list of integers provided by the user, and `flag` is True if the condition `l[l[i] - 1] == l[i] - 1` was met at any iteration. If the condition was met, the loop prints 2 and breaks. If the condition was never met, the loop prints 3 after completing all iterations.
#Overall this is what the function does:The function `func` processes a series of test cases. For each test case, it reads an integer `n` and a list `l` of `n` integers. It then checks if there is any index `i` in the list `l` such that `l[l[i] - 1] == l[i] - 1`. If this condition is met for any index, the function prints `2` and moves on to the next test case. If the condition is never met for any index in the list, the function prints `3`. The function does not return any value; it only prints the results for each test case.

