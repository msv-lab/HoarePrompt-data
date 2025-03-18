#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000. For each test case, n is an integer such that 2 <= n <= 50, and the second line contains a list of n integers a_i where each a_i is either 0 or 1. In each test case, there is at least one a_i that equals 1.
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
        
    #State: `t` remains unchanged; `n` and `a` are not part of the output state as they are redefined in each iteration. The final printed results are the trimmed lists and the counts of zeros for each test case.
#Overall this is what the function does:The function processes `t` test cases, where each test case consists of an integer `n` and a list of `n` binary integers (0s and 1s). For each test case, it trims leading and trailing zeros from the list, prints the trimmed list, and then counts and prints the number of zeros remaining in the trimmed list.

