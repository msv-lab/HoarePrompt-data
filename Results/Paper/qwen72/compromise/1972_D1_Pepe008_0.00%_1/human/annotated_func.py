#State of the program right berfore the function call: n and m are positive integers such that 1 <= n, m <= 2 * 10^6.
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
        
    #State: `n` and `m` are positive integers such that \(1 \leq n, m \leq 2 \times 10^6\), `T` is greater than or equal to 0, `t` is `T-1`, `info` is a list of strings obtained from the input, `a` is the integer value of `info[0]`, `b` is the integer value of `info[1]` and must be at least 1, `i` is `b`, `suma` is the sum of \((a - i * (i - 1)) // i^2 + 1\) for \(i\) from 1 to `b` if \(a - i * (i - 1) > 0\), otherwise `x` is 0.
#Overall this is what the function does:The function reads a series of test cases, each containing two positive integers `a` and `b`. For each test case, it calculates a value based on a specific formula involving `a` and `b`, and prints the result. The function does not return any value. After processing all test cases, the state of the program includes the number of test cases `T`, the current test case index `t`, the input values `a` and `b`, and the calculated sum `suma`. The function effectively processes each test case independently and outputs the result for each.

