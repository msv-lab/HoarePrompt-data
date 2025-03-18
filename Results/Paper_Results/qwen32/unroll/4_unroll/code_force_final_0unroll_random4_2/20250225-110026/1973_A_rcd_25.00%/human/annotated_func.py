#State of the program right berfore the function call: t is an integer such that 1 <= t <= 500. For each test case, p_1, p_2, and p_3 are integers such that 0 <= p_1 <= p_2 <= p_3 <= 30.
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
            low, high = min(p3 - p1, p3 - p2), max(p3 - p1, p3 - p2)
            cur = low
            while high >= cur:
                if p1 - cur <= p2 - (p3 - cur):
                    print(p1 - cur + p3)
                    break
                else:
                    cur += 1
            else:
                print(p3)
        
    #State: The output state consists of `t` lines, each corresponding to the result of each iteration of the loop. The value of `t` remains unchanged, and `p_1`, `p_2`, and `p_3` are updated with the values provided in each iteration's input. The output for each iteration is determined by the conditions specified in the loop: if the sum of `p1`, `p2`, and `p3` is odd, it prints `-1`. If `p3` is greater than or equal to the sum of `p1` and `p2`, it prints `p1 + p2`. Otherwise, it finds the maximum value that can be achieved under the given constraints and prints it. The state of other variables not involved in the loop remains unchanged.
#Overall this is what the function does:The function processes `t` test cases, where each test case consists of three integers `p1`, `p2`, and `p3`. It outputs `-1` if the sum of `p1`, `p2`, and `p3` is odd. Otherwise, it calculates and outputs the maximum possible value under the constraints given, which could be `p1 + p2` if `p3` is greater than or equal to `p1 + p2`, or a value derived from the conditions specified in the loop for other cases.

