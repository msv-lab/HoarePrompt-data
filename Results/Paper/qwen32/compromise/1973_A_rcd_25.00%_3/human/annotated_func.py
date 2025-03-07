#State of the program right berfore the function call: Each test case contains three integers p_1, p_2, and p_3 (0 ≤ p_1 ≤ p_2 ≤ p_3 ≤ 30) representing the scores of the three players, sorted in non-decreasing order. There are t (1 ≤ t ≤ 500) such test cases.
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
        
    #State: The loop has processed all `t` test cases and terminated. The variables `p1`, `p2`, and `p3` hold the values of the last test case, and `t` is 0.
#Overall this is what the function does:The function processes multiple test cases, each consisting of three integer scores representing the scores of three players in non-decreasing order. For each test case, it calculates and prints a result based on the scores. The result is determined by checking if the sum of the scores is even and then applying specific conditions to derive the output. If the sum is odd, it prints -1. Otherwise, it calculates the maximum possible score that can be achieved under the given constraints and prints that value.

