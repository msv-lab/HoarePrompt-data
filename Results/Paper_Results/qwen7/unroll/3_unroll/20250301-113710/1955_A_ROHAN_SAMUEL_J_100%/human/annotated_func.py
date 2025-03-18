#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, n, a, and b are integers such that 1 ≤ n ≤ 100 and 1 ≤ a, b ≤ 30.
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
        
    #State: Output State: The output state will consist of a series of lines, each corresponding to the output of one test case. For each test case, if `n` is odd, it will print either `a * n` or `n // 2 * b + a`, depending on whether `2 * a < b` holds true. If `n` is even, it will print either `a * n` or `n // 2 * b`, again depending on whether `2 * a < b` holds true. The exact values printed will depend on the specific inputs provided for each test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of three integers \( n \), \( a \), and \( b \). For each test case, it calculates and prints a value based on the conditions provided. If \( n \) is odd, it prints \( a \times n \) or \( \frac{n}{2} \times b + a \) depending on whether \( 2a < b \) holds. If \( n \) is even, it prints \( a \times n \) or \( \frac{n}{2} \times b \) depending on the same condition. The function does not return any value but outputs the calculated values for each test case.

