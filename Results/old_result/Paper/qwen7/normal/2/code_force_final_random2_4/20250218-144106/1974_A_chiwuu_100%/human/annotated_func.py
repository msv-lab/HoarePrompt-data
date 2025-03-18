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
        
    #State: Output State: After the loop executes all the iterations, the final value of `t` will be determined based on the last iteration's conditions. Specifically, `t` will be updated according to the logic inside the loop. If `t1 >= a` in the last iteration, `t` remains unchanged. Otherwise, `t` is increased by `t2 // 15 + 1` if `t2 % 15 == 0`, or `t + t2 // 15` otherwise, where `t2 = a - t1`. The value of `n` will be decremented to 0 after the loop completes, and `i` will be equal to `n`. The values of `a` and `b` will be the last values provided by the user during the loop iterations. The variable `t1` will be the result of the last calculation, which is `t * 15 - b * 4`.
    #
    #In summary, `t` will reflect the cumulative effect of all iterations, with the final update being based on the comparison between `t1` and `a` in the last iteration.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a positive integer \( t \) and two non-negative integers \( a \) and \( b \). For each test case, it calculates a modified value of \( t \) based on the given \( a \) and \( b \), and prints the final value of \( t \) after applying specific conditions. The final value of \( t \) reflects the cumulative effect of these calculations across all test cases.

