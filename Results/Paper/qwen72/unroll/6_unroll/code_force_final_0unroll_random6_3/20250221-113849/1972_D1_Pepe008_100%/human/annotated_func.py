#State of the program right berfore the function call: The function `func` is expected to take two parameters, `n` and `m`, which are positive integers such that 1 <= n, m <= 2 * 10^6. The function should handle multiple test cases, where the number of test cases `t` is a positive integer such that 1 <= t <= 10^4. For each test case, the function calculates the number of ordered pairs (a, b) where 1 <= a <= n and 1 <= b <= m, and a + b is a multiple of b * gcd(a, b).
def func():
    T = int(input())
    for t in range(T):
        info = input().split()
        
        a, b = int(info[0]), int(info[1])
        
        suma = 0
        
        for i in range(1, b + 1):
            x = (a - i * (i - 1)) // i ** 2 + 1
            if (a - i * (i - 1)) // i ** 2 + 1 > 0:
                suma += x
                if (a - i * (i - 1)) % i ** 2 == 0 and i * (i - 1) % i ** 2 == 0:
                    suma += 1
        
        print(suma - 2)
        
    #State: The loop will execute `T` times, and for each execution, it will read two integers `a` and `b` from the input, perform the specified calculations, and print the result. After all iterations, the variable `t` will be equal to `T - 1` (the last index of the range), and the variables `info`, `a`, `b`, and `suma` will retain their values from the last iteration. The initial value of `T` will remain unchanged.
#Overall this is what the function does:The function `func` reads an integer `T` from the input, representing the number of test cases. For each test case, it reads two integers `a` and `b` from the input, performs calculations to determine the number of ordered pairs (a, b) that satisfy a specific condition, and prints the result. The function does not return any value. After all test cases are processed, the variable `T` remains unchanged, while `a`, `b`, and `suma` retain their values from the last iteration, and the loop index `t` is equal to `T - 1`.

