#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, representing the number of test cases. For each test case, x and y are integers where 0 ≤ x, y ≤ 99, representing the number of applications with a 1 × 1 icon and the number of applications with a 2 × 2 icon, respectively.
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
        
    #State: After the loop executes all iterations, `i` is equal to `n - 1`, `a` and `b` are the last integers read from the input (converted to integers), `t` is the final value computed based on the conditions inside the loop, and `t1` is the last computed value of `t * 15 - b * 4`. The values of `x`, `y`, and `n` remain unchanged.
#Overall this is what the function does:The function reads an integer `n` indicating the number of test cases. For each test case, it reads two integers `a` and `b`, representing the number of applications with 1 × 1 and 2 × 2 icons, respectively. It then calculates a value `t` based on these inputs, which is the minimum number of 15 × 15 grid cells required to fit all the applications, considering the space occupied by both 1 × 1 and 2 × 2 icons. The function prints the calculated value `t` for each test case. After processing all test cases, the function terminates, leaving the input variables `a`, `b`, and `t` in their final states for the last test case.

