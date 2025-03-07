#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 500, and for each test case, p_1, p_2, and p_3 are integers satisfying 0 ≤ p_1 ≤ p_2 ≤ p_3 ≤ 30.
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
        
    #State: Output State: The output state will consist of a series of integers or -1, depending on the input provided to the loop. For each iteration, if the sum of \(p1\), \(p2\), and \(p3\) is even and \(p3\) is less than \(p1 + p2\), the output will be \(p1 + p2\). Otherwise, it will find a value of \(cur\) such that \(p1 - cur \leq p2 - (p3 - cur)\) and print \(p1 - cur + p3\). If no such \(cur\) is found, it will print \(p3\). Each output corresponds to the respective input triplet \((p1, p2, p3)\) provided in the loop.
#Overall this is what the function does:The function processes a series of input triplets \((p1, p2, p3)\) and a positive integer \(t\). For each triplet, it checks if the sum of \(p1\), \(p2\), and \(p3\) is even. If the sum is odd or \(p3\) is greater than or equal to \(p1 + p2\), it outputs \(-1\). Otherwise, it finds a value \(cur\) such that \(p1 - cur \leq p2 - (p3 - cur)\) and prints \(p1 - cur + p3\). If no such \(cur\) exists, it prints \(p3\). The function does not return any value but prints the results for each triplet.

