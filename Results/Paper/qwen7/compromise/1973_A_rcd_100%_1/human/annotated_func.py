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
        
    #State: Output State: After the loop executes all iterations, `t` will be 0, indicating that there are no more iterations left to perform. The values of `p1`, `p2`, and `p3` will be the last set of values entered by the user for which the loop did not encounter an odd sum of `p1`, `p2`, and `p3`, and the condition `p3 < p1 + p2` was satisfied. If the loop terminated normally without any odd sums or if all possible inputs led to printing `p3`, then `x` will be 0 and `y` will be equal to `p3`. If the loop terminated due to an odd sum, `x` and `y` will not be updated and their values will depend on the last iteration where the condition `p1 - x <= p2 - y` was checked.
#Overall this is what the function does:The function reads multiple test cases, each consisting of three integers \( p_1 \), \( p_2 \), and \( p_3 \). It checks if the sum of these integers is even. If the sum is odd, it prints -1 and moves to the next test case. If the sum is even and \( p_3 \) is greater than or equal to \( p_1 + p_2 \), it prints \( p_1 + p_2 \). Otherwise, it finds integers \( x \) and \( y \) such that \( p_1 - x \leq p_2 - y \) and prints \( p_1 - x + p_3 \). If no valid \( x \) and \( y \) are found, it prints \( p_3 \). After processing all test cases, the function outputs the results for each test case.

