#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, n and m are integers such that 1 ≤ n, m ≤ 2 ⋅ 10^6. It is also guaranteed that the sum of n and the sum of m over all test cases do not exceed 2 ⋅ 10^6.
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
        
    #State: Output State: The value of `T`, which is the input integer, will determine the number of times the outer loop runs. For each iteration of the outer loop, the inner loop calculates a sum (`suma`) based on the values of `a` and `b` provided by the user input. After all iterations of the loops are completed, the final value of `suma` minus 2 is printed for each test case. The exact numerical value of the output depends on the specific inputs provided for each test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `t` (1 ≤ t ≤ 10^4) and pairs of integers `n` and `m` (1 ≤ n, m ≤ 2 ⋅ 10^6). For each test case, it reads the values of `a` and `b` from user input, calculates a sum (`suma`) based on these values using a nested loop, and finally prints the result as `suma - 2`. The function does not return any value but prints the calculated result for each test case.

