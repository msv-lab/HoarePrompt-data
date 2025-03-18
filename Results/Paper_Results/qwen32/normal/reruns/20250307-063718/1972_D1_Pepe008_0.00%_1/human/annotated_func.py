#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 10^4. For each test case, n and m are positive integers such that 1 <= n, m <= 2 * 10^6. The sum of all n values and the sum of all m values across all test cases do not exceed 2 * 10^6.
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
        
    #State: After all iterations, `T` remains unchanged, `t` is `T - 1`, `info` contains the last input values, `a` and `b` are the last input integers, `i` is `b + 1`, and `suma` is the sum calculated for the last iteration. The program will have printed the results for each of the `T` iterations.
#Overall this is what the function does:The function reads an integer `T` representing the number of test cases. For each test case, it reads two integers `a` and `b`. It then computes a specific sum based on these integers and prints the result minus one for each test case.

