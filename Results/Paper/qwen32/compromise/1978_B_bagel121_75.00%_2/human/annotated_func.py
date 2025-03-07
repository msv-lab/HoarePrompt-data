#State of the program right berfore the function call: Each test case consists of three integers n, a, and b where 1 ≤ n, a, b ≤ 10^9. The input starts with an integer t (1 ≤ t ≤ 10^4) indicating the number of test cases.
def func():
    t = int(input())
    for _ in range(t):
        n, a, b = map(int, input().split())
        
        if a >= b:
            print(n * a)
        else:
            k = min(b - a + 1, n)
            ans = int((b + (b - k + 1)) / 2 * k)
            p2 = (n - k) * a
            print(ans + p2)
        
    #State: A series of integers, each representing the result of a test case, printed on a new line.
#Overall this is what the function does:The function processes a series of test cases, each consisting of three integers `n`, `a`, and `b`. For each test case, it calculates and prints a result based on these integers. The result is printed on a new line for each test case.

