#State of the program right berfore the function call: The function receives no direct input arguments but reads from standard input. The input consists of multiple test cases. The first line contains an integer t (1 ≤ t ≤ 10^4), which denotes the number of test cases. Each of the following t lines contains two integers n and m (1 ≤ n, m ≤ 2 · 10^6). The sum of n and the sum of m across all test cases do not exceed 2 · 10^6.
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
        
    #State: `T` is unchanged, `t` is equal to `T`, `info`, `a`, and `b` hold the values of the last test case, `suma` holds the final sum for the last test case, `i` is `b + 1`, and `x` holds the last calculated value of `x` for the last test case.
#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of two integers `n` and `m`. For each test case, it calculates a specific sum based on these integers and prints the result minus 2.

