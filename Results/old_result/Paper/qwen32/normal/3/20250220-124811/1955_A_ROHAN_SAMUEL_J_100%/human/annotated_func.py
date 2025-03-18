#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each of the t test cases, n, a, and b are integers such that 1 ≤ n ≤ 100 and 1 ≤ a, b ≤ 30.
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
        
    #State: t is an integer such that 0 < t ≤ 10^4; all t test cases have been processed. For each test case, the values of n, a, and b were read from the input, and the output was determined based on the conditions specified in the loop: if n is odd and 2 * a < b, the output was a * n; otherwise, the output was n // 2 * b + a if n is odd, or n // 2 * b if n is even.
#Overall this is what the function does:The function processes a series of test cases, each defined by integers `n`, `a`, and `b`. For each test case, it calculates and prints a result based on whether `n` is odd or even and the relative values of `2 * a` and `b`. If `n` is odd and `2 * a` is less than `b`, it outputs `a * n`. Otherwise, it outputs `n // 2 * b + a` if `n` is odd, or `n // 2 * b` if `n` is even.

