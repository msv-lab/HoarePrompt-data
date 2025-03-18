#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. Each of the following t lines contains two integers n and m such that 1 <= n, m <= 2 * 10^6. The sum of all n and the sum of all m across all test cases do not exceed 2 * 10^6.
def func():
    T = int(input())
    for t in range(T):
        info = input().split()
        
        a, b = int(info[0]), int(info[1])
        
        """for i in range(1,a+1):
                for j in range(4,b+1):
                    if int((j+i)%(j*math.gcd(i,j))) == 0:
                        print(i,j)"""
        
        suma = 0
        
        for i in range(1, b + 1):
            x = (a - i * (i - 1)) // i ** 2 + 1
            if a - i * (i - 1) > 0:
                suma += x
        
        print(suma - 1)
        
    #State: The output state consists of T lines, each containing the result of the computation `suma - 1` for each test case.
#Overall this is what the function does:The function processes `t` test cases, where each test case consists of two integers `n` and `m`. For each test case, it calculates and prints a result based on the values of `n` and `m`. Specifically, it computes a sum `suma` by iterating through values from 1 to `b` and adjusting `suma` based on the formula `(a - i * (i - 1)) // i

