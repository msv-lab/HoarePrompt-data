#State of the program right berfore the function call: Each test case contains three integers p_1, p_2, and p_3 (0 ≤ p_1 ≤ p_2 ≤ p_3 ≤ 30) representing the scores of the three players, sorted in non-decreasing order. The number of test cases t satisfies 1 ≤ t ≤ 500.
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
        
    #State: The loop has executed `t` times, where `t` is the initial number of test cases. For each test case, the program reads three integers `a`, `b`, and `c`. If the sum `(a + b + c)` is odd, it prints `-1`. Otherwise, it calculates `x` as `(a + b + c) // 2` and `y` as `a + b`, then prints the minimum of `x` and `y`.
#Overall this is what the function does:The function processes multiple test cases, each consisting of three sorted integer scores. For each test case, it checks if the sum of the scores is odd. If it is, the function outputs `-1`. Otherwise, it calculates two values: half the sum of the scores and the sum of the first two scores, then outputs the smaller of these two values.

