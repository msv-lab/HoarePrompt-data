#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4, and for each test case, n and m are positive integers such that 1 ≤ n, m ≤ 2 ⋅ 10^6. It is also guaranteed that the sum of n and the sum of m over all test cases does not exceed 2 ⋅ 10^6.
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
        
    #State: Output State: `t` is `T`, `info` is a list of strings obtained from splitting the input, the first element of `info` is an integer `a`, `b` is the final value it was set to during the loop's execution, `suma` is the sum calculated based on the loop's conditions, `i` is `b + 1`, and `x` is `a - (b * (b - 1)) // b ** 2 + 1`.
    #
    #After the loop completes all its iterations, the variable `t` remains `T`, `info` stays as the list of strings obtained from splitting the input, and `b` takes its final value which is the upper limit of the range specified in the loop. The variable `suma` accumulates the value of `x` plus one under certain conditions throughout the loop's iterations. Specifically, `suma` is incremented by `x + 1` if `(a - i * (i - 1)) // i ** 2 + 1 > 0` and by an additional `1` if both `(a - i * (i - 1)) % i ** 2 == 0` and `i * (i - 1) % i ** 2 == 0` are true. The variable `i` starts from `1` and increments by `1` until it reaches `b + 1`, and `x` is calculated as `(a - i * (i - 1)) // i ** 2 + 1` for each iteration. Finally, `suma` is printed after all iterations, minus 2.
#Overall this is what the function does:The function processes a series of test cases, each containing two positive integers. For each test case, it calculates a sum based on a specific formula involving these integers and prints the result minus 2. The function reads the number of test cases from the input, followed by pairs of integers for each test case. It ensures that the values meet certain constraints and performs calculations to determine the final sum, which is then outputted.

