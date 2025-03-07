#State of the program right berfore the function call: Each test case consists of three integers n, a, and b where 1 ≤ n, a, b ≤ 10^9. The function will receive these values as input for each of the t test cases, where 1 ≤ t ≤ 10^4.
def func():
    for _ in range(int(input())):
        n, a, b = map(int, input().split())
        
        k = min(n, b - a)
        
        if b <= a:
            print(a * n)
        else:
            print(b * k - k * (k - 1) // 2 + (n - k) * a)
        
    #State: A series of integers, each representing the result of the calculation for one test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of three integers `n`, `a`, and `b`. For each test case, it calculates and prints a specific integer value based on the relationship between `a` and `b`, and the value of `n`. If `b` is less than or equal to `a`, it prints `a` multiplied by `n`. Otherwise, it computes a more complex expression involving `n`, `a`, and `b` and prints the result.

