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
        
    #State: Output State: The output state will consist of a series of lines, each containing the result of the conditional logic within the loop for each test case. Specifically, for each test case, if `n` is odd, it will print either `a * n` or `n // 2 * b + a`, depending on whether `2 * a < b` is true or false. If `n` is even, it will print either `a * n` or `n // 2 * b`, again depending on whether `2 * a < b` is true or false. The number of lines in the output will be equal to the number of test cases provided as input.
#Overall this is what the function does:The function processes multiple test cases, each consisting of three integers \( n \), \( a \), and \( b \). For each test case, it checks if \( n \) is odd or even and compares \( 2a \) with \( b \). Based on these conditions, it prints either \( a \times n \) or \( \frac{n}{2} \times b + a \) if \( n \) is odd, and either \( a \times n \) or \( \frac{n}{2} \times b \) if \( n \) is even. The function does not return any value but outputs the results for each test case.

