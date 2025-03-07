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
        
    #State: The loop has completed all its iterations, and the values of `t`, `p1`, `p2`, and `p3` reflect the inputs provided for each iteration.
#Overall this is what the function does:The function processes a series of test cases, each defined by three non-negative integers \(p_1\), \(p_2\), and \(p_3\) under specific constraints. For each test case, it calculates and prints a value based on these integers. If the sum of \(p_1\), \(p_2\), and \(p_3\) is odd, it prints \(-1\) and moves to the next test case. Otherwise, it determines a specific value to print according to certain conditions involving \(p_1\), \(p_2\), and \(p_3\). After processing all test cases, it outputs the calculated values for each case.

