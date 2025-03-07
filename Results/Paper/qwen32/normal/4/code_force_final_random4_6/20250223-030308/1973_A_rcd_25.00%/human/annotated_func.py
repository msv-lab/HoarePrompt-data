#State of the program right berfore the function call: t is an integer such that 1 <= t <= 500. Each of the following t lines contains three integers p_1, p_2, and p_3 such that 0 <= p_1 <= p_2 <= p_3 <= 30, representing the scores of the three players in a non-decreasing order.
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
        
    #State: The loop has processed all `t` input cases, each consisting of three integers `p1`, `p2`, and `p3`. For each case, the program checks if the sum of `p1`, `p2`, and `p3` is odd. If it is, the program prints `-1`. If the sum is even, the program checks if `p3` is greater than or equal to the sum of `p1` and `p2`. If true, it prints the sum of `p1` and `p2`. Otherwise, it finds the largest possible value of `cur` such that `p1 - cur <= p2 - (p3 - cur)` within the range defined by `low` and `high`, and prints `p1 - cur + p3`. If no such `cur` exists, it prints `p3`.
#Overall this is what the function does:The function processes a series of test cases, each consisting of three integer scores in non-decreasing order. For each test case, it determines and prints a specific value based on the scores. If the sum of the scores is odd, it prints `-1`. If the sum is even and the highest score is at least the sum of the other two scores, it prints the sum of the two lower scores. Otherwise, it calculates and prints the largest possible value that satisfies a certain condition involving the scores, or the highest score if no such value exists.

