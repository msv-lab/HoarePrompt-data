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
        
    #State: Output State: After all iterations of the loop have finished, the value of `t` will be the final value it takes after processing all the inputs provided by the user within the range specified by `n`. The value of `t` will be updated based on the conditions given in each iteration of the loop. Specifically, `t` starts as `b` and is modified according to the following rules:
    #- If `t` is even, it is halved (`t = t // 2`).
    #- If `t` is odd, it is halved and incremented by one (`t = t // 2 + 1`).
    #- After modifying `t`, `t1` is calculated as `t * 15 - b * 4`.
    #- If `t1 >= a`, `t` remains unchanged.
    #- If `t1 < a`, `t` is updated based on the value of `t2 = a - t1`:
    #  - If `t2` is divisible by 15, `t` is increased by `t2 // 15`.
    #  - Otherwise, `t` is increased by `(t2 // 15) + 1`.
    #
    #The final value of `t` will reflect these operations applied sequentially for each input pair `(a, b)` provided within the loop's range `n`.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a positive integer \( t \) and pairs of non-negative integers \( a \) and \( b \). For each test case, it modifies \( t \) based on specific conditions involving \( a \) and \( b \), and outputs the final value of \( t \) after all modifications. Specifically, \( t \) is first adjusted by halving it or halving it and adding one if it is odd. Then, a new value \( t1 \) is calculated based on \( t \) and \( b \). If \( t1 \) is greater than or equal to \( a \), \( t \) remains unchanged; otherwise, \( t \) is further adjusted based on the difference between \( a \) and \( t1 \). The function ultimately prints the final value of \( t \) for each test case.

