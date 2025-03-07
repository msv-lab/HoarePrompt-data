#State of the program right berfore the function call: n and m are positive integers such that 1 <= n, m <= 2 * 10^6.
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
        
    #State: The values of `n` and `m` remain unchanged. The loop prints a value for `suma - 2` for each of the `T` iterations, but `T` itself remains the same as the initial value.
#Overall this is what the function does:The function reads an integer `T` from the input, which represents the number of test cases. For each test case, it reads two positive integers `a` and `b` from the input, calculates a value `suma` based on these inputs, and prints `suma - 2`. The function does not return any value. After the function concludes, the values of `n` and `m` (if they exist outside the function) remain unchanged, and `T` remains the same as the initial value.

