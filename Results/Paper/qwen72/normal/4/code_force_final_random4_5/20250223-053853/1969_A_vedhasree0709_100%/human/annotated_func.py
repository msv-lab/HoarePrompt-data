#State of the program right berfore the function call: t is an integer such that 1 <= t <= 5000, n is an integer such that 2 <= n <= 50, and p is a list of n integers where each p_i satisfies 1 <= p_i <= n and p_i ≠ i, and all p_i are distinct.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        l = list(map(int, input().split()))
        
        i = 0
        
        j = 0
        
        while i <= n - 1:
            p = l[i]
            q = l[p - 1]
            if q == i + 1:
                print(2)
                j = 1
                break
            i += 1
        
        if j == 0:
            print(3)
        
    #State: t is an integer such that 1 <= t <= 5000, n is an integer such that 2 <= n <= 50, and p is a list of n integers where each p_i satisfies 1 <= p_i <= n and p_i ≠ i, and all p_i are distinct. The loop has executed and printed either 2 or 3 for each iteration of the outer loop, depending on whether a specific condition was met.
#Overall this is what the function does:The function `func` processes a series of test cases defined by an integer `t` (1 <= t <= 5000). For each test case, it reads an integer `n` (2 <= n <= 50) and a list `l` of `n` distinct integers where each integer `l_i` satisfies 1 <= l_i <= n and l_i ≠ i. The function then checks if there exists an index `i` such that `l[l[i] - 1] == i + 1`. If such an index is found, it prints `2` and breaks out of the loop. If no such index is found, it prints `3`. After processing all test cases, the function has printed either `2` or `3` for each test case, depending on the condition being met or not.

