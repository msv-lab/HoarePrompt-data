#State of the program right berfore the function call: The function should accept three integers p_1, p_2, and p_3 as input, where 0 <= p_1 <= p_2 <= p_3 <= 30, representing the scores of the three players sorted in non-decreasing order.
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
        
    #State: `p_1`, `p_2`, and `p_3` are integers such that 0 <= `p_1` <= `p_2` <= `p_3` <= 30, `t` is 0, `_` is `t - 1`, `a`, `b`, and `c` are integers provided by user input. If the sum of `a`, `b`, and `c` is odd, the program continues to the next iteration of the loop. `x` is the integer result of `(a + b + c) // 2`, `y` is the sum of `a` and `b`.
#Overall this is what the function does:The function reads an integer `t` from user input, representing the number of test cases. For each test case, it reads three integers `a`, `b`, and `c` from user input, representing the scores of three players. If the sum of `a`, `b`, and `c` is odd, the function prints `-1` and moves to the next test case. Otherwise, it calculates `x` as the integer division of the sum of `a`, `b`, and `c` by 2, and `y` as the sum of `a` and `b`. It then prints the minimum of `x` and `y`. After processing all test cases, the function concludes.

