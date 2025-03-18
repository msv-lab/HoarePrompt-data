#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, and for each test case, x and y are integers where 0 ≤ x, y ≤ 99.
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
        
    #State: After all iterations of the loop, `i` will be equal to `n`, indicating the loop has completed all its iterations. The variable `t` will hold the final computed value for each iteration, which is updated based on the conditions inside the loop. Specifically, `t` starts as `b // 2` if `b` is even, or `(b // 2) + 1` if `b` is odd. If `t1` (calculated as `t * 15 - b * 4`) is greater than or equal to `a`, `t` remains the same. Otherwise, `t` is adjusted based on the difference `t2` (calculated as `a - t1`). If `t2` is divisible by 15, `t` is increased by `t2 // 15`. If `t2` is not divisible by 15, `t` is increased by `t2 // 15 + 1`. The variables `a` and `b` are updated with each iteration to the next pair of integers read from the input. The loop will have processed `n` pairs of integers (`a`, `b`), and the final state of `t` will reflect the last computation performed in the loop.
#Overall this is what the function does:The function reads an integer `n` indicating the number of test cases. For each test case, it reads two integers `a` and `b` from the input. It then calculates a value `t` based on the following rules: if `b` is even, `t` is set to `b // 2`; if `b` is odd, `t` is set to `(b // 2) + 1`. It further adjusts `t` based on the difference between `a` and a calculated value `t1` (which is `t * 15 - b * 4`). If `t1` is less than `a`, `t` is incremented by the ceiling of the division of the difference `a - t1` by 15. Finally, the function prints the computed value of `t` for each test case. The function does not return any value; it only prints the results.

