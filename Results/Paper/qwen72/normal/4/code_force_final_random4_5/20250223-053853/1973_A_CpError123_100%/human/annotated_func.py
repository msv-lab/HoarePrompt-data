#State of the program right berfore the function call: The function should take three integers p_1, p_2, and p_3 as input, where 0 ≤ p_1 ≤ p_2 ≤ p_3 ≤ 30, and these integers represent the scores of three players after playing chess games. The function should also handle multiple test cases, where the number of test cases t is an integer such that 1 ≤ t ≤ 500.
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
        
    #State: The loop will print either -1 or the minimum of (x, y) for each test case, where x is half of the sum of a, b, and c, and y is the sum of a and b. The values of p_1, p_2, and p_3 remain unchanged.
#Overall this is what the function does:The function `func` takes an integer `t` as input, representing the number of test cases. For each test case, it reads three integers `a`, `b`, and `c` from the input, which represent the scores of three players. If the sum of `a`, `b`, and `c` is odd, the function prints `-1`. Otherwise, it calculates `x` as half of the sum of `a`, `b`, and `c`, and `y` as the sum of `a` and `b`, then prints the minimum of `x` and `y`. The values of `a`, `b`, and `c` are not modified by the function.

