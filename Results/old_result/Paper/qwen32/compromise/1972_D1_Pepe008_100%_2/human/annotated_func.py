#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 10^4. For each test case, n and m are positive integers such that 1 <= n, m <= 2 * 10^6. The sum of n and the sum of m over all test cases do not exceed 2 * 10^6.
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
        
    #State: The final value of `suma - 2` after processing all `T` inputs.
#Overall this is what the function does:The function `func` processes multiple test cases, each defined by two integers `a` and `b`. For each test case, it calculates a specific sum based on these integers and outputs the result minus 2. The function handles up to 10,000 test cases, with each integer in the range of 1 to 2,000,000, and the cumulative sum of all integers does not exceed 2,000,000.

