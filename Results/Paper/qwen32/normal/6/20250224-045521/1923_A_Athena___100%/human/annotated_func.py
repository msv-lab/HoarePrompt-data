#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000. For each test case, n is an integer such that 2 ≤ n ≤ 50, and the second line contains a list of n integers a_1, a_2, ..., a_n where each a_i is either 0 or 1. In each test case, there is at least one a_i that equals 1.
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
        
    #State: `t` is an integer such that 0 ≤ t ≤ 1000, `a` is a non-empty list with all leading and trailing zeros removed (or an empty list if `a` originally contained only zeros), `n` is the integer input by the user, and `res` is the total count of zeros in the list `a` for the last iteration.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of a list of integers (each either 0 or 1). For each test case, it counts and prints the number of zeros in the list after removing any leading and trailing zeros.

