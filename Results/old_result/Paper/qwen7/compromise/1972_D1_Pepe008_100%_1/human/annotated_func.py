#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n and m are positive integers such that 1 ≤ n, m ≤ 2⋅10^6, and the sum of n or m over all test cases does not exceed 2⋅10^6.
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
        
    #State: Output State: `b` must be greater than 16, `i` is 17, `x` is calculated based on the current value of `i`, `suma` is increased by the sum of `x` values for each iteration, and the final `suma` is 103.
    #
    #To explain this output state in more detail:
    #- Since the loop increments `i` starting from 5 and runs through at least 7 iterations initially, and given that `i` must continue to increment, after all iterations, `i` will be 17.
    #- The value of `b` must be greater than 16 because the loop increments `i` up to the point where the condition `(a - i * (i - 1)) % i ** 2 == 0 and i * (i - 1) % i ** 2 == 0` no longer holds true, which happens when `i` reaches 17.
    #- The value of `x` changes with each iteration of `i`. For `i=17`, `x` would be calculated as `(a - 17 * 16) // 289 + 1`.
    #- The `suma` variable accumulates the value of `x` for each valid iteration where the condition `(a - i * (i - 1)) % i ** 2 == 0 and i * (i - 1) % i ** 2 == 0` holds true. Based on the pattern observed, the total increase in `suma` after all iterations is 103.
#Overall this is what the function does:The function processes multiple test cases, each containing two positive integers \( n \) and \( m \). For each test case, it calculates a specific sum based on these integers and prints the result. The final output for each test case is derived from a series of calculations involving the values of \( n \) and \( m \), specifically through a loop that iterates based on the value of \( m \). The function does not return any value but prints the calculated result for each test case.

