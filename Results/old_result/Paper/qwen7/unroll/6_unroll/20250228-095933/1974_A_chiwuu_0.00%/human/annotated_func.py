#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, x and y are non-negative integers such that 0 ≤ x, y ≤ 99.
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
        
    #State: Output State: `t` is a non-negative integer determined by the final value after executing the loop for each iteration based on the given conditions. The exact value of `t` depends on the inputs provided within each iteration of the loop, but it will always be a non-negative integer resulting from the specified operations.
#Overall this is what the function does:The function processes multiple test cases, each consisting of three integers: t, x, and y. For each test case, it calculates a non-negative integer t based on specific conditions involving x and y. The final value of t is determined through a series of arithmetic operations and conditional checks. After processing all test cases, the function outputs the calculated t for each case.

