#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n, a, and b are integers such that 1 ≤ n ≤ 100 and 1 ≤ a, b ≤ 30.
def func():
    for _ in range(int(input())):
        n, a, b = map(int, input().split())
        
        if n % 2:
            if 2 * a < b:
                print(a * n)
            else:
                print(n // 2 * b + a)
        elif 2 * a < b:
            print(a * n)
        else:
            print(n // 2 * b)
        
    #State: Output State: The output state consists of a series of lines, each containing the result of the loop's computation for each test case. For each test case, if `n` is odd, it checks whether `2 * a < b`. If true, it prints `a * n`; otherwise, it prints `n // 2 * b + a`. If `n` is even, it directly prints `a * n` if `2 * a < b`, otherwise it prints `n // 2 * b`. The number of lines in the output state equals the number of test cases provided as input.
#Overall this is what the function does:The function processes a series of test cases, each defined by integers \( n \), \( a \), and \( b \). For each test case, it calculates and prints a value based on the conditions: if \( n \) is odd and \( 2a < b \), it prints \( an \); if \( n \) is odd and \( 2a \geq b \), it prints \( \frac{n}{2}b + a \); if \( n \) is even and \( 2a < b \), it prints \( an \); otherwise, it prints \( \frac{n}{2}b \). The function does not return any value but outputs the calculated values for each test case.

