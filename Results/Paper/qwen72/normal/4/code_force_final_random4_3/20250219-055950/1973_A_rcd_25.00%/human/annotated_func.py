#State of the program right berfore the function call: The function should accept three integers p_1, p_2, and p_3 as input such that 0 <= p_1 <= p_2 <= p_3 <= 30, and these integers represent the scores of three players in a series of chess games. The function should also handle multiple test cases, where the number of test cases t is an integer such that 1 <= t <= 500.
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
        
    #State: The loop has finished all iterations, and the value of `_` is `t - 1`. The values of `p1`, `p2`, and `p3` for each test case have been processed according to the loop logic, and the appropriate output has been printed for each test case. The values of `p1`, `p2`, `p3`, and `t` remain unchanged, and the loop has executed `t` times.
#Overall this is what the function does:The function `func` processes multiple test cases, where each test case consists of three integers `p1`, `p2`, and `p3` representing the scores of three players in a series of chess games. The function reads the number of test cases `t` and then, for each test case, reads the scores `p1`, `p2`, and `p3`. It checks if the sum of the scores is odd; if so, it prints `-1` and moves to the next test case. If the sum is even, it further checks if `p3` is greater than or equal to the sum of `p1` and `p2`; if true, it prints the sum of `p1` and `p2`. Otherwise, it calculates and prints a value based on a specific condition involving the differences between the scores. After processing all test cases, the function completes, and the values of `p1`, `p2`, `p3`, and `t` are unchanged.

