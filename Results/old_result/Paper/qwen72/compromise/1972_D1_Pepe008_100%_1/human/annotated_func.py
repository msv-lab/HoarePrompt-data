#State of the program right berfore the function call: n and m are positive integers such that 1 <= n, m <= 2 * 10^6.
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
        
    #State: The loop has completed all iterations. `n` and `m` are positive integers such that \(1 \leq n, m \leq 2 \times 10^6\), `T` is the input integer, `t` is `T - 1`, `info` is a list of strings from user input, `a` is the integer value of `info[0]` from the last iteration, `b` is the integer value of `info[1]` from the last iteration and must be greater than or equal to `a`, `i` is `b + 1`, `suma` is the sum of all valid `x` values calculated during the last iteration, where `x` is \(\left\lfloor \frac{a - i \cdot (i - 1)}{i^2} \right\rfloor + 1\) for each `i` from 1 to `b`, and `suma` is incremented by 1 for each `i` where \((a - i \cdot (i - 1)) \% i^2 == 0\) and \(i \cdot (i - 1) \% i^2 == 0\) and \(\left\lfloor \frac{a - i \cdot (i - 1)}{i^2} \right\rfloor + 1 > 0\).
#Overall this is what the function does:The function reads an integer `T` from the user, which represents the number of test cases. For each test case, it reads two integers `a` and `b` from the user, where `1 <= a, b <= 2 * 10^6`. It then calculates a sum `suma` based on a specific formula involving `a` and `b`. The final result for each test case is `suma - 2`, which is printed to the console. After processing all test cases, the function completes, and the state of the program is that `T` test cases have been processed, and the corresponding results have been printed.

