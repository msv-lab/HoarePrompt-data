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
        
    #State: The final value of `t` after all iterations of the loop is determined by the last input values of `a` and `b`, and the operations performed within the loop.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two integers `a` and `b`. For each test case, it calculates a value `t` based on the given inputs and certain conditions. Specifically, it first doubles `b` and adjusts `t` based on whether the doubled value is divisible by 5. Then, it checks if `t` multiplied by 15 minus `b` times 4 is greater than or equal to `a`. If not, it calculates the difference and further adjusts `t` accordingly. Finally, it prints the resulting value of `t` for each test case.

