#State of the program right berfore the function call: t is an integer such that 1 <= t <= 5000. For each of the t test cases, n is an integer such that 2 <= n <= 50, and p is a list of n distinct integers where each p_i satisfies 1 <= p_i <= n, p_i != i.
def func_1():
    n = int(input())
    v = [0] * (n + 1)
    v = [0] + list(map(int, input().split()))
    if (n == 2) :
        print(2)
        #This is printed: 2
    else :
        for i in range(1, n + 1):
            if v[v[v[i]]] == i:
                print(2)
                return
            
        #State: The program does not print anything and finishes executing the loop.
        print(3)
        #This is printed: 3
    #State: `t` is an integer such that 1 <= t <= 5000; `n` is an integer with the current value of 2, and `p` is a list of 2 distinct integers where each p_i satisfies 1 <= p_i <= 2, p_i != i; `v` is a list where the first element is 0 and the next 2 elements are integers read from the input if `n` is 2. Otherwise, the program does not print anything and finishes executing without modifying `t`, `n`, `p`, or `v`.
#Overall this is what the function does:The function `func_1` processes a series of test cases. For each test case, it reads an integer `n` and a list `p` of `n` distinct integers. It then prints either `2` or `3` based on a specific condition involving the list `p`. The function does not return any value.

