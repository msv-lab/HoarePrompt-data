#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4, and for each test case, n and m are positive integers such that 1 ≤ n, m ≤ 2 \cdot 10^6. It is also guaranteed that the sum of n and the sum of m over all test cases does not exceed 2 \cdot 10^6.
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
        
    #State: Output State: `t` is 9999, `a` is `int(info[0])`, `b` is the maximum value of `b` passed into the loop, `i` is `b + 1`, `x` is `(a - i * (i - 1)) // i ** 2 + 1`, and `suma` is the cumulative sum of all `x` values that satisfy the conditions `(a - i * (i - 1)) % i ** 2 == 0 and i * (i - 1) % i ** 2 == 0` throughout the loop's iterations.
    #
    #Explanation: After the loop completes all its iterations, the variable `t` will be equal to the total number of inputs processed, which is 9999 given the constraint `1 ≤ T ≤ 10^4`. The variable `a` retains its initial value as it is not modified within the loop. The variable `b` will be set to the highest value it reached during the loop's execution, and `i` will be one more than the final value of `b`. The variable `x` is calculated based on the last iteration's values, and `suma` accumulates the value of `x` for each iteration of the loop, adding 1 to `suma` if the specific condition is met for any `i`.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two positive integers `a` and `b`. For each test case, it calculates a cumulative sum (`suma`) based on a specific formula involving `a` and `i` (where `i` ranges from 1 to `b`). If certain conditions are met during the calculation, 1 is added to `suma`. Finally, it prints the result of `suma - 2`. The function implicitly handles up to 10,000 test cases, with each test case involving integers `a` and `b` such that 1 ≤ `a`, `b` ≤ 2 * 10^6 and the total sum of `a` and `b` across all test cases does not exceed 2 * 10^6.

