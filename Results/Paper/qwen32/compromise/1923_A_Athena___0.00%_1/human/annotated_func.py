#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000. For each test case, n is an integer such that 2 <= n <= 50, and there is a list of n integers a_1, a_2, ..., a_n where each a_i is either 0 or 1. At least one a_i is 1 in each test case.
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
        
        print(a)
        
        for i in range(len(a)):
            if a[i] == 0:
                res += 1
        
        print(res)
        
    #State: `t` is an input integer within the range 1 to 1000, `n` is an integer such that 2 <= n <= 50, `a` is an empty list, and `res` is 0.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it takes an integer `n` and a list of `n` integers (each being either 0 or 1 with at least one 1 present). It removes leading and trailing zeros from the list, then counts and prints the number of zeros remaining in the list.

