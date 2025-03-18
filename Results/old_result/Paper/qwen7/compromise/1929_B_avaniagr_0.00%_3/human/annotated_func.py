#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000, and for each test case, n and k are integers such that 2 ≤ n ≤ 10^8 and 1 ≤ k ≤ 4n - 2.
def func():
    for s in [*open(0)][1:]:
        n, k = map(int, s.split())
        
        print((k // 2 + k % 2) * (k < 4 * n - 3) + 2 * n * (k >= 4 * n - 3) + (k ==
            4 * n - 2))
        
    #State: Output State: The output state will consist of a series of integers printed based on the given conditions for each test case within the loop. For each test case, if \( k < 4n - 3 \), the output will be \((k // 2 + k \% 2)\). If \( k \geq 4n - 3 \), the output will be \(2n\). Additionally, if \( k = 4n - 2 \), the output will be \(2n\) as well. The specific values depend on the input values of \( n \) and \( k \) for each test case.
#Overall this is what the function does:The function processes multiple test cases, each defined by integers \( n \) and \( k \). For each test case, it calculates and prints an integer value based on the relationship between \( n \) and \( k \). Specifically, if \( k < 4n - 3 \), it prints \((k // 2 + k \% 2)\). If \( k \geq 4n - 3 \), it prints \(2n\). Additionally, if \( k = 4n - 2 \), it also prints \(2n\). The function does not return any value; instead, it outputs the calculated values for each test case.

