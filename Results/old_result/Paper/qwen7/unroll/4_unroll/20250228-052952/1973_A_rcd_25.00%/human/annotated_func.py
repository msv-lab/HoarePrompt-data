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
        
    #State: Output State: The output state depends on the inputs provided within each iteration of the loop. For each iteration, if the sum of \(p1\), \(p2\), and \(p3\) is even and \(p3\) is less than \(p1 + p2\), the output will be \(p1 + p2\). Otherwise, it will find a value for \(cur\) such that \(p1 - cur \leq p2 - (p3 - cur)\) and print \(p1 - cur + p3\). If no such \(cur\) is found, it prints \(p3\). The final state will be a list of outputs from each iteration.
#Overall this is what the function does:The function processes multiple test cases, each defined by three non-negative integers \(p_1\), \(p_2\), and \(p_3\) where \(0 \leq p_1 \leq p_2 \leq p_3 \leq 30\). For each test case, it checks if the sum of \(p_1\), \(p_2\), and \(p_3\) is even. If the sum is odd or \(p_3\) is greater than or equal to \(p_1 + p_2\), it outputs \(-1\). Otherwise, it finds a value \(cur\) such that \(p_1 - cur \leq p_2 - (p3 - cur)\) and outputs \(p1 - cur + p3\). If no such \(cur\) exists, it outputs \(p3\). The function returns a list of outputs, one for each test case.

