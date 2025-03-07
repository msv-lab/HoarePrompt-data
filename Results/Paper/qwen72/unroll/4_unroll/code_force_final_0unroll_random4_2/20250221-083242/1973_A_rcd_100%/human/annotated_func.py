#State of the program right berfore the function call: t is an integer such that 1 <= t <= 500, and for each test case, p_1, p_2, and p_3 are integers such that 0 <= p_1 <= p_2 <= p_3 <= 30.
def func():
    t = int(input())
    for _ in range(t):
        p1, p2, p3 = map(int, input().split())
        
        if (p1 + p2 + p3) % 2 != 0:
            print(-1)
            continue
        
        if p3 >= p1 + p2:
            print(p1 + p2)
        else:
            x = 0
            y = p3
            while y >= x:
                if p1 - x <= p2 - y:
                    print(p1 - x + p3)
                    break
                else:
                    x += 1
                    y -= 1
            else:
                print(p3)
        
    #State: The values of `t`, `p1`, `p2`, and `p3` remain unchanged, but the loop has printed the results of the calculations for each test case. For each test case, if the sum of `p1`, `p2`, and `p3` is odd, `-1` is printed. If `p3` is greater than or equal to the sum of `p1` and `p2`, the sum of `p1` and `p2` is printed. Otherwise, the loop finds a pair `(x, y)` such that `p1 - x <= p2 - y` and prints `p1 - x + p3`. If no such pair is found, `p3` is printed.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, where `1 <= t <= 500`, indicating the number of test cases. For each test case, it reads three integers `p1`, `p2`, and `p3` from the input, where `0 <= p1 <= p2 <= p3 <= 30`. The function then processes these values and prints a result for each test case. If the sum of `p1`, `p2`, and `p3` is odd, it prints `-1`. If `p3` is greater than or equal to the sum of `p1` and `p2`, it prints the sum of `p1` and `p2`. Otherwise, it finds a pair `(x, y)` such that `p1 - x <= p2 - y` and prints `p1 - x + p3`. If no such pair is found, it prints `p3`. The values of `t`, `p1`, `p2`, and `p3` remain unchanged after the function concludes.

