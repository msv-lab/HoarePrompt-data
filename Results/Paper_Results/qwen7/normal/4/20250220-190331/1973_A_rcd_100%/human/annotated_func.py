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
        
    #State: t is an integer within the range 1 to 500, `_` is t, `p1`, `p2`, `p3` are integers with the sum of `p1`, `p2`, and `p3` being even, `p3` is less than or equal to `p1 + p2`, and `p3` is at least 3. The variable `x` is either 0 or 1, and `y` is -1. If `p1 - x <= p2 - y` holds true at any point during the loop, the loop breaks and prints `p1 - x + p3`. Otherwise, the loop continues until `y` becomes -1, and it prints `p3` at the end.
#Overall this is what the function does:The function processes multiple test cases, each defined by three non-negative integers \( p_1 \), \( p_2 \), and \( p_3 \) under specific conditions. For each test case, it checks if the sum of \( p_1 \), \( p_2 \), and \( p_3 \) is even. If not, it prints -1 and moves to the next test case. If the sum is even and \( p_3 \) is greater than or equal to \( p_1 + p_2 \), it prints \( p_1 + p_2 \). Otherwise, it enters a loop where it adjusts two variables \( x \) and \( y \) to find a valid solution, printing either \( p_1 - x + p_3 \) if a valid solution is found or \( p_3 \) if no valid solution exists. The function returns a value based on these conditions for each test case.

