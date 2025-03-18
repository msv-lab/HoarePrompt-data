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
        
    #State: Output State: The values of `n`, `a`, and `b` will remain unchanged after all iterations of the loop have finished. The loop processes each set of inputs (`n`, `a`, `b`) independently based on the given conditions and prints the result, but it does not modify the values of `n`, `a`, or `b` within the loop itself. Therefore, after all iterations, `n`, `a`, and `b` retain their original values from the last input provided.
    #
    #In Natural Language: After the loop has executed all its iterations, the values of `n`, `a`, and `b` will be the same as the values of the last set of inputs provided to the loop. The loop does not alter these values; it only uses them to perform calculations and prints the results.
#Overall this is what the function does:The function processes multiple test cases, each consisting of three integers \( n \), \( a \), and \( b \). For each test case, it calculates and prints a value based on specific conditions. The function does not modify the input values \( n \), \( a \), and \( b \) across different test cases. After processing all test cases, the final values of \( n \), \( a \), and \( b \) are the same as the values of the last set of inputs provided.

