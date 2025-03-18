#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 500, and for each test case, p_1, p_2, and p_3 are integers satisfying 0 ≤ p_1 ≤ p_2 ≤ p_3 ≤ 30.
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
        
    #State: After all iterations of the loop have finished, the variable `t` will be 0, indicating that there are no more inputs to process. The variables `p1`, `p2`, and `p3` will retain their final values from the last iteration of the loop.
#Overall this is what the function does:The function processes `t` test cases, where for each case, it reads three integers `p1`, `p2`, and `p3`. It checks if the sum of these integers is even. If not, it prints `-1` and continues to the next test case. Otherwise, it calculates and prints a specific value based on the relationship between `p1`, `p2`, and `p3`. After processing all test cases, it ensures that `t` is reduced to `0`, indicating all inputs have been processed.

