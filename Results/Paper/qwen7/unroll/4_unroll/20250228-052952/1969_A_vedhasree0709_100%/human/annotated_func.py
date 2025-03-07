#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5000. For each test case, n is an integer such that 2 ≤ n ≤ 50, and p is a list of n integers where 1 ≤ p_i ≤ n, p_i ≠ i, and all p_i are distinct.
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
        
    #State: Output State: t is an integer such that 1 ≤ t ≤ 5000. For each test case, n is an integer such that 2 ≤ n ≤ 50, and after executing the loop, if there exists an index `i` where `l[i]` is equal to `i + 1`, the output will be `2`; otherwise, the output will be `3`.
#Overall this is what the function does:The function processes a series of test cases, each containing an integer `n` (2 ≤ n ≤ 50) and a list `p` of `n` distinct integers where each integer `p_i` satisfies 1 ≤ p_i ≤ n and p_i ≠ i. For each test case, the function checks if there exists an index `i` where `p[i]` is equal to `i + 1`. If such an index is found, the function prints `2`; otherwise, it prints `3`. The function does not return any value but outputs the result for each test case.

