#State of the program right berfore the function call: The function should accept three integers p_1, p_2, and p_3 as input, where 0 ≤ p_1 ≤ p_2 ≤ p_3 ≤ 30, and it should be called within a loop that processes multiple test cases, each defined by a different set of p_1, p_2, and p_3 values.
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
        
    #State: The loop processes `t` test cases, each defined by a different set of integers `a`, `b`, and `c`. For each test case, if the sum of `a`, `b`, and `c` is odd, it prints `-1`. Otherwise, it calculates `x` as half the sum of `a`, `b`, and `c`, and `y` as the sum of `a` and `b`, then prints the minimum of `x` and `y`. After all iterations, the values of `t`, `a`, `b`, and `c` are unchanged, but the loop has printed the results for each test case.
#Overall this is what the function does:The function `func` processes a series of test cases. It reads an integer `t` from the input, which specifies the number of test cases. For each test case, it reads three integers `a`, `b`, and `c` from the input. If the sum of `a`, `b`, and `c` is odd, it prints `-1`. Otherwise, it calculates `x` as half the sum of `a`, `b`, and `c`, and `y` as the sum of `a` and `b`, then prints the minimum of `x` and `y`. After processing all `t` test cases, the function concludes, and the values of `t`, `a`, `b`, and `c` are unchanged. The function does not return any value.

