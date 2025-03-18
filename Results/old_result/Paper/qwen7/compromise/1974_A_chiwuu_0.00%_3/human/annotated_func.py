#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, x and y are integers such that 0 ≤ x, y ≤ 99.
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
        
    #State: Output State: `t` is an integer such that 1 ≤ t ≤ 10^4, `n` is an input integer after all iterations of the loop have executed. The value of `t` is determined by the operations inside the loop based on the inputs provided for each iteration of `i` in `range(n)`. Specifically, `t` is updated based on the conditions involving `a`, `b`, and arithmetic operations, ensuring it never falls below 1 or exceeds 10^4.
#Overall this is what the function does:The function processes a series of test cases, each consisting of three integers: t, x, and y. For each test case, it calculates an integer t based on the values of x and y, ensuring t remains within the range of 1 to 10^4. It updates t according to specific conditions involving arithmetic operations and prints the final value of t for each test case.

