#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 500, and for each test case, p_1, p_2, and p_3 are non-negative integers satisfying 0 ≤ p_1 ≤ p_2 ≤ p_3 ≤ 30.
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
        
    #State: Output State: The output state will consist of a series of integers or -1, depending on the input values for each iteration of the loop. For each iteration, if the sum of `p1`, `p2`, and `p3` is odd, the output will be -1. Otherwise, if `p3` is greater than or equal to `p1 + p2`, the output will be `p1 + p2`. If `p3` is less than `p1 + p2`, the loop will attempt to find integers `x` and `y` such that `p1 - x` equals `p2 - y` and `p3`, and will output `p1 - x + p3` if such integers exist. If no such integers exist, the output will be `p3`.
#Overall this is what the function does:The function reads a positive integer `t` and then processes `t` test cases. For each test case, it reads three non-negative integers `p1`, `p2`, and `p3`. It checks if the sum of `p1`, `p2`, and `p3` is even. If the sum is odd, it prints `-1`. If the sum is even and `p3` is greater than or equal to `p1 + p2`, it prints `p1 + p2`. If `p3` is less than `p1 + p2`, it attempts to find integers `x` and `y` such that `p1 - x` equals `p2 - y` and `p3`. If such integers exist, it prints `p1 - x + p3`; otherwise, it prints `p3`. After processing all test cases, it outputs a series of integers or `-1` based on the conditions described.

