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
        
    #State: `n` and `m` are positive integers such that \(1 \leq n, m \leq 2 \times 10^6\), `T` is a positive integer, `t` is \(T - 1\), `info` is a list of strings from the last input, `a` is the integer value of the first string in `info`, `b` is the integer value of the second string in `info` and must be greater than or equal to 1, `suma` is the sum of all valid `x` values calculated in the loop for each iteration, where `x` is \(\left(\frac{a - i \cdot (i - 1)}{i^2} + 1\right)\) for \(i\) from 1 to `b`, and an additional 1 is added to `suma` for each `i` where \((a - i \cdot (i - 1)) \% i^2 == 0\) and \(i \cdot (i - 1) \% i^2 == 0\).
#Overall this is what the function does:The function reads an integer `T` from the input, which represents the number of test cases. For each test case, it reads two integers `a` and `b` from the input. It then calculates a sum `suma` based on a specific formula involving `a` and `b`, and prints `suma - 2` for each test case. The function does not return any value. After the function concludes, `T` is a positive integer, `t` is `T - 1`, `info` is a list of strings from the last input, `a` and `b` are the integer values from the last test case, and `suma` is the calculated sum for the last test case.

