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
        
    #State: `n` and `m` are positive integers such that \(1 \leq n, m \leq 2 \times 10^6\), `T` is greater than or equal to the number of iterations, `t` is `T-1`, `info` is a list of strings obtained from the last input, `a` is the integer value of the last `info[0]`, `b` is the integer value of the last `info[1]` and must be at least 1, `i` is `b`, and `suma` is the sum of \((a - i * (i - 1)) // i
#Overall this is what the function does:The function reads an integer `T` indicating the number of test cases. For each test case, it reads two integers `a` and `b` from the input. It then calculates a value `suma` based on a specific formula involving `a` and `b`. Finally, it prints `suma - 1` for each test case. The function does not return any value; it only prints the results. After the function concludes, the state includes `T` being the total number of test cases processed, `a` and `b` being the last input values for the final test case, and `suma` being the calculated value for the final test case.

