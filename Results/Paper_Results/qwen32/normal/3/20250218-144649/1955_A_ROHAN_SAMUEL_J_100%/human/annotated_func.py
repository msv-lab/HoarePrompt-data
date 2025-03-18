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
        
    #State: The loop has processed all `t` test cases, and the final output consists of the results of each test case based on the provided conditions.
#Overall this is what the function does:The function processes a series of test cases, each defined by three integers `n`, `a`, and `b`. For each test case, it computes and prints a result based on whether `n` is odd or even and the relative values of `a` and `b`. The result is printed for each test case.

