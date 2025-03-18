#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 10^4, and for each of the t test cases, n and m are positive integers such that 1 <= n, m <= 2 * 10^6. The sum of all n and the sum of all m across all test cases do not exceed 2 * 10^6.
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
        
    #State: After executing all iterations, the output state consists of T lines, each line containing the value of `suma - 2` for the respective test case, where `suma` is computed based on the values of `a` and `b` for that test case as described in the code.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads two integers `a` and `b`. It then calculates a value `suma` based on these inputs and outputs `suma - 2` for each test case.

