#State of the program right berfore the function call: Each test case contains three integers p_1, p_2, and p_3 such that 0 ≤ p_1 ≤ p_2 ≤ p_3 ≤ 30. The number of test cases t satisfies 1 ≤ t ≤ 500.
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
        
    #State: The output state after all iterations will be a series of printed values, each corresponding to the result of one test case. If the sum of `p1`, `p2`, and `p3` is odd, `-1` is printed. If `p3` is greater than or equal to `p1 + p2`, `p1 + p2` is printed. Otherwise, the nested loop determines the output based on the conditions `p1 - x <= p2 - y`.
#Overall this is what the function does:The function processes multiple test cases, each consisting of three integers `p1`, `p2`, and `p3` such that `0 ≤ p1 ≤ p2 ≤ p3 ≤ 30`. For each test case, it prints a value based on the conditions: if the sum of `p1`, `p2`, and `p3` is odd, it prints `-1`. If `p3` is greater than or equal to `p1 + p2`, it prints `p1 + p2`. Otherwise, it calculates and prints a value determined by the conditions `p1 - x ≤ p2 - y` within a nested loop.

