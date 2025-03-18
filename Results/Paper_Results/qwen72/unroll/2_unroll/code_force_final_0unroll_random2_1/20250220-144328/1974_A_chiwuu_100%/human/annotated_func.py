#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, x and y are integers such that 0 <= x, y <= 99.
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
        
    #State: For each test case, the value of `t` is adjusted based on the input values `a` and `b` such that `t` is the minimum number of 15-minute intervals needed to cover the difference `a - t1` (where `t1 = t * 15 - b * 4`), ensuring that `t1` is at least `a`. The final value of `t` for each test case is printed. The values of `a`, `b`, and `n` remain unchanged.
#Overall this is what the function does:The function processes a series of test cases, where each test case includes two integers `a` and `b` such that 0 <= a, b <= 99. For each test case, it calculates and prints the minimum number of 15-minute intervals (`t`) required to ensure that the value `t1 = t * 15 - b * 4` is at least `a`. The function does not return any value; it only prints the result for each test case. The values of `a`, `b`, and `n` remain unchanged after the function execution.

