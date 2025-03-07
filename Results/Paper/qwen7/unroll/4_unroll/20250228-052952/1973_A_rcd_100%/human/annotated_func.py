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
        
    #State: Output State: The output state will consist of a series of integers or -1, depending on the input provided within each iteration of the loop. Each integer in the output corresponds to the result of one iteration of the loop, where the result is either \(p1 - x + p3\) if \(y \geq x\) holds true until the end of the while loop, or \(p3\) if the condition is never met. If the sum \(p1 + p2 + p3\) is odd, the output for that iteration will be -1 and the loop will continue to the next iteration.
#Overall this is what the function does:The function processes a series of test cases, each consisting of three integers \(t\), \(p_1\), \(p_2\), and \(p_3\). For each test case, it checks if the sum \(p_1 + p_2 + p_3\) is even. If the sum is odd, it outputs \(-1\) and moves to the next test case. Otherwise, it calculates and outputs either \(p_1 - x + p_3\) or \(p_3\), depending on the values of \(x\) and \(y\) derived from a specific condition. If no valid \(x\) and \(y\) satisfy the condition, it outputs \(p_3\). The function returns a series of integers or \(-1\) corresponding to each test case.

