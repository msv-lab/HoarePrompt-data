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
        
    #State: `t` is 0, `_` is `t - 1`, `p1`, `p2`, and `p3` are input integers, and the sum of `p1`, `p2`, and `p3` is odd. If `p3` is greater than or equal to `p1 + p2`, the program continues to the next iteration of the loop. Otherwise, `low` is the minimum of `p3 - p1` and `p3 - p2`, `high` is the maximum of `p3 - p1` and `p3 - p2`. If the loop condition `high >= cur` is true and `p1 - cur <= p2 - (p3 - cur)` at any point, the loop will print `p1 - cur + p3` and break. If the loop completes all iterations without breaking, `cur` will be equal to `high + 1` and the loop will print `p3`.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, which represents the number of test cases. For each test case, it reads three integers `p1`, `p2`, and `p3` from the input. If the sum of `p1`, `p2`, and `p3` is odd, the function prints `-1` and moves to the next test case. If `p3` is greater than or equal to the sum of `p1` and `p2`, the function prints the sum of `p1` and `p2`. Otherwise, it calculates a value based on the difference between `p3` and `p1` or `p2` and prints the result. After processing all test cases, the function concludes with `t` being 0.

