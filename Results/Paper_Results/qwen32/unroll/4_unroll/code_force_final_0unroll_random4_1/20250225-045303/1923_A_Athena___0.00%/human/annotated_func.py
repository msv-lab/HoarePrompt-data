#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000. For each test case, n is an integer such that 2 <= n <= 50, and the second line contains n integers a_i where each a_i is either 0 or 1. There is at least one 1 in each test case.
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
        
    #State: `t` is unchanged, `n`, `a`, and `res` are the final values from the last test case.
#Overall this is what the function does:The function processes `t` test cases, each consisting of a list of `n` binary integers (0s and 1s) with at least one 1. For each test case, it removes leading and trailing 0s from the list, prints the modified list, and then counts and prints the number of 0s remaining in the list.

