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
        
    #State: The values of `n` and `m` remain unchanged, and `T` is decremented by the number of iterations the loop has executed. For each iteration of the loop, the value of `suma` is calculated and printed, but `suma` is reset to 0 at the beginning of each iteration. Therefore, the final value of `suma` after the loop finishes is 0.
#Overall this is what the function does:The function `func` reads an integer `T` from the input, which represents the number of test cases. For each test case, it reads two positive integers `a` and `b` from the input, performs a series of calculations to compute a value `suma`, and prints `suma - 2`. The values of `n` and `m` (mentioned in the preconditions) are not modified by the function. After processing all test cases, the function does not return any value, and the final state of `suma` is 0 for each test case.

