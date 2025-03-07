#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000. For each test case, n is an integer such that 2 <= n <= 50, and the second line contains a list of n integers a_i where each a_i is either 0 or 1. There is at least one a_i equal to 1 in each test case.
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
        
    #State: `t` is an integer such that 1 <= `t` <= 1000; `n` is an input integer; `a` is a list of integers with leading and trailing zeros removed from the last iteration's input; `res` is the total number of `0`s in the list `a` from the last iteration's input.
#Overall this is what the function does:The function reads multiple test cases, each consisting of a list of binary integers (0s and 1s) with at least one 1. For each test case, it removes leading and trailing zeros, then counts and prints the number of zeros remaining in the list.

