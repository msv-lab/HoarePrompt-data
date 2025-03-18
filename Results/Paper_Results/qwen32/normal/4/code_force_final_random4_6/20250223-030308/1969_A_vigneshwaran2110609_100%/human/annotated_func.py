#State of the program right berfore the function call: t is an integer such that 1 <= t <= 5000. For each test case, n is an integer such that 2 <= n <= 50, and p is a list of n integers where each p_i is an integer such that 1 <= p_i <= n, p_i != i, and all p_i are distinct.
def func():
    n = int(input())
    for i in range(n):
        x = int(input())
        
        l = list(map(int, input().strip().split()))
        
        for i in range(0, x):
            if l[l[i] - 1] == i + 1:
                flag = True
                print(2)
                break
        else:
            print(3)
        
    #State: The loop completes all `n` iterations, and for each iteration, the inner loop completes all `x` iterations without breaking, resulting in the program printing `3` `n` times.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it reads an integer `n` and a list `p` of `n` integers. It checks if there exists an index `i` such that `p[p[i] - 1]` equals `i + 1`. If such an index exists, it prints `2`; otherwise, it prints `3`. The function performs this check for each of the `t` test cases.

