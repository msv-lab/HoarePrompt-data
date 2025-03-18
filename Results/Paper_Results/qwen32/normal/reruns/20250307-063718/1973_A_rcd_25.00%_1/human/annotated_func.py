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
        
    #State: The loop prints `-1` exactly `t` times.
#Overall this is what the function does:The function processes `t` test cases, each consisting of three integers `p1`, `p2`, and `p3` (where 0 <= p1 <= p2 <= p3 <= 30). For each test case, it prints a value based on the sum of `p1`, `p2`, and `p3` and their relationships. If the sum is odd, it prints `-1`. Otherwise, it calculates and prints the maximum possible value that can be achieved under the given constraints.

