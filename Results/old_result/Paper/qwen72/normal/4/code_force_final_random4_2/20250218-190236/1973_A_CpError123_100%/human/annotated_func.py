#State of the program right berfore the function call: The function should take three integers p_1, p_2, and p_3 as input such that 0 ≤ p_1 ≤ p_2 ≤ p_3 ≤ 30, representing the scores of the three players, sorted in non-decreasing order.
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
        
    #State: The values of `p_1`, `p_2`, and `p_3` remain unchanged, `t` is 0, and for each iteration that was executed, `a`, `b`, and `c` were integers provided by the user, `x` was `(a + b + c) // 2`, and `y` was `a + b`. If the sum of `a`, `b`, and `c` was odd for any iteration, the program printed `-1` and continued to the next iteration. Otherwise, the program printed the minimum of `x` and `y`.
#Overall this is what the function does:The function reads an integer `t` from the user, indicating the number of test cases. For each test case, it reads three integers `a`, `b`, and `c` from the user, representing the scores of three players. If the sum of these scores is odd, the function prints `-1` and moves to the next test case. If the sum is even, it calculates `x` as the integer division of the sum by 2 and `y` as the sum of `a` and `b`. The function then prints the minimum of `x` and `y`. After processing all test cases, the function terminates, leaving the input variables `a`, `b`, and `c` unchanged for each iteration, and `t` is reduced to 0.

