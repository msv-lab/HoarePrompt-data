#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 500, and for each test case, p_1, p_2, and p_3 are non-negative integers such that 0 ≤ p_1 ≤ p_2 ≤ p_3 ≤ 30.
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
        
    #State: `t` is 0, `p1` is an input integer, `p2` is an input integer, `p3` is an input integer, `low` is `min(p3 - p1, p3 - p2)`, `high` is `max(p3 - p1, p3 - p2)`, and `cur` is `high`.
#Overall this is what the function does:The function processes a series of test cases, each consisting of three integers \( p_1 \), \( p_2 \), and \( p_3 \). It checks if the sum of these integers is even. If not, it prints -1 and moves to the next test case. If the sum is even and \( p_3 \) is greater than or equal to \( p_1 + p_2 \), it prints \( p_1 + p_2 \). Otherwise, it calculates two values, `low` and `high`, based on the differences between \( p_3 \) and \( p_1 \) and \( p_3 \) and \( p_2 \). It then iteratively adjusts a variable `cur` within the range defined by `low` and `high` until it finds a value that satisfies a specific condition, printing the result accordingly. After processing all test cases, it outputs the last computed value.

