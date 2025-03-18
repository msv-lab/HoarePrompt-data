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
        
    #State: t is an integer such that 1 ≤ t ≤ 10^4 - (number of iterations - 1), n, a, and b are integers as described, and all iterations of the loop have been executed.
#Overall this is what the function does:The function processes multiple test cases, each containing integers \( t \), \( n \), \( a \), and \( b \). For each test case, it calculates and prints either \( a \times n \) or \( \frac{n}{2} \times b + a \) or \( \frac{n}{2} \times b \) based on the conditions provided. After processing all test cases, the function does not return any value.

