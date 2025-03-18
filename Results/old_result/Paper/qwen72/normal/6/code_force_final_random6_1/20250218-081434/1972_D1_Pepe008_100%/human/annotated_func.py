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
        
    #State: `n` and `m` are positive integers such that 1 <= n, m <= 2 * 10^6, `T` is an input integer, `t` is `T - 1`, `a` is the integer value of `info[0]` from the last iteration, `b` is the integer value of `info[1]` from the last iteration, and `suma` is the sum of all valid `x` values for each iteration from 1 to `b` for each of the `T` iterations, with any additional 1s added when the conditions `(a - i * (i - 1)) % i
#Overall this is what the function does:The function `func` reads an integer `T` from the input, which represents the number of test cases. For each test case, it reads two integers `a` and `b` from the input, where `a` and `b` are positive integers. It then calculates a sum `suma` based on a specific formula involving `a` and `b`. The final result for each test case is `suma - 2`, which is printed to the output. The function does not return any value. After the function concludes, `T` is an input integer, `t` is `T - 1`, `a` is the integer value of `info[0]` from the last iteration, `b` is the integer value of `info[1]` from the last iteration, and `suma` is the sum of all valid `x` values for each iteration from 1 to `b` for each of the `T` iterations, with any additional 1s added when the conditions `(a - i * (i - 1)) % i

