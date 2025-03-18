#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000, and for each test case, n and k are integers such that 2 ≤ n ≤ 10^8 and 1 ≤ k ≤ 4n - 2.
def func():
    for s in [*open(0)][1:]:
        n, k = map(int, s.split())
        
        print((k // 2 + k % 2) * (k < 4 * n - 3) + 2 * n * (k >= 4 * n - 3) + (k ==
            4 * n - 2))
        
    #State: Output State: The output state consists of a series of integers printed based on the conditions given in the loop. For each test case, if \( k < 4n - 3 \), the output is \((k // 2 + k \% 2)\). If \( k \geq 4n - 3 \), the output is \(2n\). If \( k = 4n - 2 \), the output is also \(2n\).
    #
    #This means the output will vary depending on the values of \( n \) and \( k \) for each test case, but it will always follow one of these three rules.
#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case contains two integers \( n \) and \( k \). For each test case, it calculates and prints a value based on the conditions: if \( k < 4n - 3 \), it prints \( k // 2 + k \% 2 \); if \( k \geq 4n - 3 \), it prints \( 2n \); and if \( k = 4n - 2 \), it also prints \( 2n \). The function does not return any value but outputs the calculated values for each test case.

