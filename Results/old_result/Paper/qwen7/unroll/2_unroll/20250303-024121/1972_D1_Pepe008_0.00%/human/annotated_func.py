#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4, and for each test case, n and m are positive integers such that 1 ≤ n, m ≤ 2 ⋅ 10^6. It is also guaranteed that the sum of n and the sum of m over all test cases do not exceed 2 ⋅ 10^6.
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
        
    #State: Output State: T is an input integer such that 1 ≤ T ≤ 10^4, and for each iteration t in the range of T, the variable `suma` is calculated based on the given formula and printed, then the process repeats until all iterations are completed. The final output state will have executed all the iterations and printed the value of `suma - 1` for each iteration.
#Overall this is what the function does:The function processes a series of test cases, each containing two positive integers. For each test case, it calculates a value based on a specific formula and prints the result minus one. The function does not return any value but prints the results for each test case.

