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
        
    #State: `n` and `m` are positive integers such that \(1 \leq n, m \leq 2 \times 10^6\), `T` is a positive integer, `t` is `T - 1`, `info` is a list of strings obtained from splitting the last input, `a` is the integer value of `info[0]`, `b` is the integer value of `info[1]` and must be at least 1, `i` is `b + 1`, `suma` is the sum of \((a - i * (i - 1)) // i^2 + 1\) for all valid `i` from 1 to `b` where \(a - i * (i - 1) > 0\) for each iteration.
#Overall this is what the function does:The function reads a series of inputs, processes them, and prints a result for each set of inputs. Specifically, it first reads an integer `T` indicating the number of test cases. For each test case, it reads two integers `a` and `b`. It then calculates a sum based on a specific formula involving `a` and `b`, and prints the result of this calculation minus one. The function does not return any values; it only prints results to the console. After the function concludes, the state includes the processed inputs and the printed results, but the original input variables `n` and `m` are not affected.

