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
        
    #State: Output State: `t` is an integer such that 1 ≤ t ≤ 10^4, `n` is an input integer after all iterations of the loop have executed.
    #
    #In this output state, the value of `t` will be determined by the series of operations performed within the loop for each iteration from `i` in `range(n)`. The exact value of `t` will depend on the inputs provided for `a` and `b` in each iteration, but it will always be constrained between 1 and 10^4 inclusive. The value of `n` will be the number of times the loop has iterated, which is specified as an input integer.
#Overall this is what the function does:The function processes multiple test cases, each consisting of three integers \( t \), \( x \), and \( y \). For each test case, it calculates a value for \( t \) based on the given \( x \) and \( y \) values through a series of arithmetic operations. The final value of \( t \) is constrained between 1 and \( 10^4 \) inclusive and is printed for each test case. The function does not return any value explicitly but prints the calculated \( t \) for each test case.

