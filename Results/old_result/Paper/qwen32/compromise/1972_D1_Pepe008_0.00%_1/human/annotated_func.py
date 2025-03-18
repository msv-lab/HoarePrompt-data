#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. Each of the next t lines contains two integers n and m such that 1 ≤ n, m ≤ 2 · 10^6. The sum of all n and the sum of all m across all test cases do not exceed 2 · 10^6.
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
        
    #State: `t` is equal to `T`, `T` is the number of test cases, `info` is the list of strings from the last input line, `a` and `b` are the integer values from the last input line, `suma` is the accumulated sum of `x` for the last test case where `a - i * (i - 1) > 0`, and the final printed value is `suma - 1`.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads two integers `a` and `b`. It then computes a specific sum based on these integers and prints the result minus one for each test case.

