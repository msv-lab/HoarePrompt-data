#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000. For each test case, n is an integer such that 2 ≤ n ≤ 50, and a list of n integers a_1, a_2, ..., a_n where each a_i is either 0 or 1. There is at least one a_i equal to 1 in each test case.
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
        
    #State: After all the iterations of the loop, `t` will be 0, `n` will be the last input integer, `a` will be the last processed list with leading and trailing zeros removed, and `res` will be the count of zeros in the last processed list `a`.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer `n` and a list of `n` binary integers (0s and 1s) with at least one 1. It then removes any leading and trailing zeros from the list and counts the number of 0s in the modified list, printing this count for each test case.

