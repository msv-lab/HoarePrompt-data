#State of the program right berfore the function call: t is an integer such that 1 <= t <= 5000, and for each test case, n is an integer such that 2 <= n <= 50, and p is a list of n integers where each p_i is an integer such that 1 <= p_i <= n and p_i ≠ i, and all p_i are distinct.
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
        
    #State: For each test case, the loop will either print 2 if it finds a pair (i, p) such that l[p - 1] == i + 1, or it will print 3 if no such pair is found. The variables t, n, and l will retain their values as they were before the loop started, and the variables i and j will be reset to 0 for each new test case.
#Overall this is what the function does:The function processes `t` test cases, where each test case includes an integer `n` and a list `l` of `n` distinct integers, each not equal to its index. For each test case, the function checks if there exists a pair `(i, p)` such that `l[p - 1] == i + 1`. If such a pair is found, it prints `2`; otherwise, it prints `3`. The function does not return any values, and the state of the program after each test case is that the variables `t`, `n`, and `l` retain their values, while `i` and `j` are reset for the next test case.

