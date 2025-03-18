#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, and for each test case, a, b, and m are integers such that 1 <= a, b, m <= 10^18.
def func():
    t = int(input())
    for _ in range(t):
        a, b, m = map(int, input().split())
        
        A = int(m / a) + 1
        
        B = int(m / b) + 1
        
        print(A + B)
        
    #State: The loop will execute `t` times, and for each iteration, it will read three integers `a`, `b`, and `m` from the input, compute `A` and `B` as `int(m / a) + 1` and `int(m / b) + 1` respectively, and print the sum `A + B`. After all iterations, the values of `t`, `a`, `b`, and `m` will be unchanged, but the loop will have printed the sum `A + B` for each test case.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, which represents the number of test cases, with 1 <= t <= 10^4. For each test case, it reads three integers `a`, `b`, and `m` from the input, where 1 <= a, b, m <= 10^18. It then computes two values, `A` and `B`, as `int(m / a) + 1` and `int(m / b) + 1` respectively, and prints the sum `A + B`. After processing all `t` test cases, the function does not return any value, but the sum `A + B` for each test case is printed to the output. The values of `t`, `a`, `b`, and `m` are not modified by the function.

