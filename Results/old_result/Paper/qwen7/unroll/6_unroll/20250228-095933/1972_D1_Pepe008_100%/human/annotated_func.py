#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4, and for each test case, n and m are positive integers such that 1 ≤ n, m ≤ 2 ⋅ 10^6. Additionally, the sum of n and the sum of m over all test cases do not exceed 2 ⋅ 10^6.
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
        
    #State: Output State: The value of `T`, which is the number of test cases, followed by `T` lines, each containing the result of the calculation for each test case. Each result is the value of `suma - 2` after executing the inner loop for the given `a` and `b` values.
#Overall this is what the function does:The function processes a series of test cases, each consisting of two positive integers \(a\) and \(b\). For each test case, it calculates a value based on the given formula and prints the result, which is the calculated value minus 2. The function reads the number of test cases from the input, then for each test case, it reads \(a\) and \(b\), and computes the sum based on the specified formula. If the conditions for \(a\) and \(b\) are met, it performs the computation; otherwise, it handles the error appropriately. The final output consists of the results for each test case.

