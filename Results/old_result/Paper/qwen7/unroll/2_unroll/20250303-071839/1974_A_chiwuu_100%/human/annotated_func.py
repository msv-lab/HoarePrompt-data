#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, x and y are non-negative integers such that 0 ≤ x, y ≤ 99.
def func():
    n = int(input())
    for i in range(n):
        a, b = input().split()
        
        a = int(a)
        
        b = int(b)
        
        t = b
        
        if t % 2 == 0:
            t = t // 2
        else:
            t = t // 2 + 1
        
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
        
    #State: Output State: `t` is the final value of `t` after all iterations of the loop have executed, based on the given operations and conditions within the loop. The value of `t` is determined by the inputs `a` and `b` for each iteration of the loop, and it is updated according to the specified rules. The initial value of `t` from the precondition is modified by these operations, and the final value of `t` after all iterations is the output state.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two non-negative integers \(x\) and \(y\), and a positive integer \(t\) (where \(1 \leq t \leq 10^4\)). For each test case, it calculates a final value of \(t\) based on specific operations involving \(x\) and \(y\). The function updates \(t\) according to predefined rules and prints the final value of \(t\) for each test case. The overall effect is to transform the initial value of \(t\) into a new value based on the given inputs and conditions.

