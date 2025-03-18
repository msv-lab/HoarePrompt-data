#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000. For each test case, n is an integer such that 2 <= n <= 50, and the second line contains n integers a_1, a_2, ..., a_n where each a_i is either 0 or 1. There is at least one 1 in each test case.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        res = 0
        
        while a and a[0] == 0:
            a.pop(0)
        
        while a and a[-1] == 0:
            a.pop()
        
        for i in range(len(a)):
            if a[i] == 0:
                res += 1
        
        print(res)
        
    #State: - After all `t` iterations, the output state will be a series of integers, each representing the count of zeros in the middle of the list `a` for each test case, after removing the leading and trailing zeros.
    #
    #Given that the output of the code for each test case is an integer representing the count of zeros in the middle of the list `a` after removing the leading and trailing zeros, the output state after all the iterations will be a sequence of these integers.
    #
    #Since we don't have specific values for `t` and the lists `a` in this problem statement, we cannot provide a concrete sequence of integers. However, the format of the output will be a series of integers, one for each test case.
    #
    #Output State:
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads a list of integers consisting of 0s and 1s, removes any leading and trailing 0s, and then counts the number of 0s remaining in the list. It outputs this count for each test case.

