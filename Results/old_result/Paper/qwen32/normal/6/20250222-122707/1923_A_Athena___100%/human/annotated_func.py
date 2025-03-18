#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000. Each of the following t test cases consists of two lines: the first line contains an integer n such that 2 <= n <= 50, and the second line contains n integers a_1, a_2, ..., a_n where each a_i is either 0 or 1. In each test case, there is at least one a_i that equals 1.
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
        
    #State: `t` is an integer such that `t` = 0; `n` is undefined; `a` is undefined; `res` is undefined.
#Overall this is what the function does:The function processes `t` test cases, where each test case consists of a list of `n` integers (either 0 or 1) with at least one 1 present. For each test case, it calculates and prints the number of zeros between the first and last occurrence of 1 in the list.

