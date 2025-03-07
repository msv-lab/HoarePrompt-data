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
        
    #State: All values of `p1`, `p2`, `p3`, `t`, and `_` remain unchanged.
#Overall this is what the function does:The function processes multiple test cases, each defined by three non-negative integers \(p_1\), \(p_2\), and \(p_3\) where \(0 \leq p_1 \leq p_2 \leq p_3 \leq 30\). For each test case, it checks if the sum of \(p_1\), \(p_2\), and \(p_3\) is even. If the sum is odd, it prints \(-1\) and moves to the next test case. Otherwise, it calculates and prints one of two possible values: either \(p_1 + p_2\) or \(p_1 - x + p_3\), depending on the relationship between \(p_1\), \(p_2\), and \(p_3\). After processing all test cases, the function does not return any value but prints the results for each test case.

