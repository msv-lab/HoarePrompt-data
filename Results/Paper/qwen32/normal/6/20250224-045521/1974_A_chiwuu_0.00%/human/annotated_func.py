#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each of the t test cases, there are two integers x and y such that 0 ≤ x, y ≤ 99.
def func():
    n = int(input())
    for i in range(n):
        a, b = input().split()
        
        a = int(a)
        
        b = int(b)
        
        t = b * 2
        
        if t % 5 == 0:
            t = t // 5
        else:
            t = t // 5 + 1
        
        t1 = t * 15 - b * 4
        
        if t1 >= a:
            t = t
        else:
            t2 = a - t1
            if t2 % 15 == 0:
                t = t + t2 // 15
            else:
                t = t + t2 // 15 + 1
        
        print(t)
        
    #State: the value of `t` after the `n`-th iteration, as determined by the last update in the loop.
#Overall this is what the function does:The function reads an integer `n` representing the number of test cases. For each test case, it reads two integers `a` and `b`. It then calculates a value `t` based on specific conditions and prints this value. The purpose of the function is to process each pair of integers `a` and `b` and output a computed value `t` for each test case.

