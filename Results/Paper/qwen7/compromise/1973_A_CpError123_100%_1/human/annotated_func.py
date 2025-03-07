#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 500, and for each test case, p_1, p_2, and p_3 are non-negative integers such that 0 ≤ p_1 ≤ p_2 ≤ p_3 ≤ 30.
def func():
    t = int(input())
    for _ in range(t):
        a, b, c = map(int, input().split())
        
        if (a + b + c) % 2 != 0:
            print(-1)
            continue
        
        x = (a + b + c) // 2
        
        y = a + b
        
        print(min(x, y))
        
    #State: Output State: t is the number of iterations that completed, and for each iteration, either -1 or the minimum value of (a+b+c)//2 and (a+b) was printed based on the given conditions.
#Overall this is what the function does:The function reads a positive integer `t` and `t` test cases, each consisting of three non-negative integers `a`, `b`, and `c`. It checks if the sum of `a`, `b`, and `c` is even. If the sum is odd, it prints `-1`. Otherwise, it calculates the minimum value between half of the sum `(a + b + c) // 2` and the sum of `a` and `b` (`a + b`). It then prints this minimum value for each test case.

