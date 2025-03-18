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
        
    #State: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, n, a, and b are the integers entered by the user during the input. The values of n, a, and b are updated according to the conditions inside the loop, but after all iterations, they retain the final values determined by the last input.
#Overall this is what the function does:The function processes multiple test cases, each containing integers \( n \), \( a \), and \( b \). For each test case, it calculates and prints a result based on specific conditions involving these integers. If \( n \) is odd, it checks whether \( 2a < b \); if true, it prints \( a \times n \), otherwise it prints \( \frac{n}{2} \times b + a \). If \( n \) is even, it directly prints \( a \times n \) if \( 2a < b \), otherwise it prints \( \frac{n}{2} \times b \). After processing all test cases, it does not return any value.

