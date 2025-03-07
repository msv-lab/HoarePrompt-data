#State of the program right berfore the function call: Each test case consists of two positive integers n and m (1 ≤ n, m ≤ 2 · 10^6). The number of test cases t satisfies 1 ≤ t ≤ 10^4. The sum of n and the sum of m across all test cases do not exceed 2 · 10^6.
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
        
    #State: a series of integers, each representing the result of `suma - 2` for each test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two positive integers `n` and `m`. For each test case, it calculates a specific sum based on these integers and prints the result minus two.

