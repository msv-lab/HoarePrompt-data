#State of the program right berfore the function call: t is an integer such that 1 <= t <= 500, and for each test case, p_1, p_2, and p_3 are integers such that 0 <= p_1 <= p_2 <= p_3 <= 30.
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
        
    #State: For each test case, the loop will print either -1 or the minimum of `(a + b + c) // 2` and `a + b`, where `a`, `b`, and `c` are the input integers for that test case. The values of `t`, `p_1`, `p_2`, and `p_3` remain unchanged.
#Overall this is what the function does:The function `func` reads an integer `t` indicating the number of test cases, where `1 <= t <= 500`. For each test case, it reads three integers `p_1`, `p_2`, and `p_3` such that `0 <= p_1 <= p_2 <= p_3 <= 30`. If the sum of `p_1`, `p_2`, and `p_3` is odd, it prints `-1`. Otherwise, it calculates the minimum of `(p_1 + p_2 + p_3) // 2` and `p_1 + p_2` and prints this value. The function does not return any value; it only prints the results for each test case. After the function concludes, the values of `t`, `p_1`, `p_2`, and `p_3` remain unchanged.

