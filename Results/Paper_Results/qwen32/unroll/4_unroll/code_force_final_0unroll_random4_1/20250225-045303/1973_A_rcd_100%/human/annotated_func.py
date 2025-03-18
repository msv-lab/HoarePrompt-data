#State of the program right berfore the function call: Each test case contains three integers p_1, p_2, and p_3 (0 ≤ p_1 ≤ p_2 ≤ p_3 ≤ 30) representing the scores of the three players, sorted in non-decreasing order. The number of test cases t satisfies 1 ≤ t ≤ 500.
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
        
    #State: Each test case contains three integers `p_1`, `p_2`, and `p_3` (0 ≤ `p_1` ≤ `p_2` ≤ `p_3` ≤ 30) representing the scores of the three players, sorted in non-decreasing order.
#Overall this is what the function does:The function processes multiple test cases, each consisting of three integers representing the scores of three players in non-decreasing order. For each test case, it determines and prints the maximum possible score that can be achieved under specific conditions, or -1 if no valid score can be computed.

