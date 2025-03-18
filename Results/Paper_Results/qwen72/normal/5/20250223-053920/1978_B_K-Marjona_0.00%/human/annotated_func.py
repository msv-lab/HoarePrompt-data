#State of the program right berfore the function call: The function `func` is expected to take three parameters: `n`, `a`, and `b`, where `n`, `a`, and `b` are integers such that 1 ≤ n, a, b ≤ 10^9.
def func():
    for _ in range(int(input())):
        n, a, b = map(int, input().split())
        
        k = min(n, b - a)
        
        if b <= a:
            print(a * n)
        else:
            print((b + (b - k + 1)) // 2 * k + (n - k) * a)
        
    #State: Output State: The function `func` will have processed all the iterations of the loop. For each iteration, it will have read three integers `n`, `a`, and `b` from the input, calculated the value of `k` as the minimum of `n` and `b - a`, and then printed the result based on the conditions provided in the loop body. The values of `n`, `a`, and `b` will be the last set of inputs read, and `k` will be the last calculated value. The state of the function will be unchanged except for the variables and conditions within the loop body that are used for each iteration.
#Overall this is what the function does:The function `func` reads multiple sets of three integers `n`, `a`, and `b` from the input, where each integer is in the range 1 ≤ n, a, b ≤ 10^9. For each set, it calculates a value based on the following logic: if `b` is less than or equal to `a`, it prints `a * n`. Otherwise, it calculates and prints a more complex expression involving `n`, `a`, and `b`. After processing all sets, the function does not return any value, but the last set of `n`, `a`, and `b` will be the final state of these variables. The function's primary purpose is to compute and print a specific value for each set of input integers based on the given conditions.

