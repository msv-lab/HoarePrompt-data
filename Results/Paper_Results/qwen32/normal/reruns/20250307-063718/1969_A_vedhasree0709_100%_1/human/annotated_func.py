#State of the program right berfore the function call: t is an integer such that 1 <= t <= 5000. For each test case, n is an integer such that 2 <= n <= 50, and p is a list of n distinct integers where each p_i is an integer such that 1 <= p_i <= n, p_i != i.
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
        
    #State: t is 0; n and l are the values from the last test case; i is n; j is 0.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of an integer `n` and a list `p` of `n` distinct integers. For each test case, it checks if there exists an index `i` such that the value at `p[i-1]` points back to `i`. If such an index exists, it outputs `2`; otherwise, it outputs `3`. The function does not return a value but prints the result for each test case.

