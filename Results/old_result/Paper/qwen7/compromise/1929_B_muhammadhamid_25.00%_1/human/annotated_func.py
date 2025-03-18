#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000, and for each test case, n and k are integers such that 2 ≤ n ≤ 10^8 and 1 ≤ k ≤ 4n - 2.
def func():
    for _ in range(int(input())):
        n, k = map(int, input().split())
        
        if k == 1:
            print(1)
            continue
        
        if k <= 2 * n:
            print(math.ceil(k / 2))
        else:
            print(k // 2 + 1)
        
    #State: Output State: The output state consists of a series of lines, each containing either 1, \(\text{math.ceil}(k/2)\), or \(\text{k} // 2 + 1\), depending on the values of \(n\) and \(k\) for each test case. Specifically, for each test case:
    #- If \(k = 1\), the output is 1.
    #- If \(k \leq 2n\), the output is \(\text{math.ceil}(k/2)\).
    #- Otherwise, the output is \(\text{k} // 2 + 1\).
#Overall this is what the function does:The function processes multiple test cases, each defined by integers \(n\) and \(k\). For each test case, it prints a specific value based on the conditions: if \(k = 1\), it prints 1; if \(k \leq 2n\), it prints \(\text{math.ceil}(k/2)\); otherwise, it prints \(\text{k} // 2 + 1\). After processing all test cases, it outputs a series of lines, each containing one of the aforementioned values.

