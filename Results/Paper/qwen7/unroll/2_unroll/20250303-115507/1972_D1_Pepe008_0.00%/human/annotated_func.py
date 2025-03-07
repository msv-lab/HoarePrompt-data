#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, n and m are integers such that 1 ≤ n, m ≤ 2 ⋅ 10^6. It is also guaranteed that the sum of n and the sum of m over all test cases does not exceed 2 ⋅ 10^6.
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
        
    #State: Output State: The value of `T`, which is the input integer, will determine the number of times the loop runs. For each iteration, the loop calculates a sum (`suma`) based on the values of `a` and `b` provided by the user input. The final output is the sum minus one, printed for each input pair `(a, b)`. The exact numerical value of the output state cannot be determined without specific values for `a` and `b` for each iteration, but it will be the sum of `x` values for all pairs `(a, b)` minus one for each input pair.
#Overall this is what the function does:The function processes a series of test cases, each containing two integers \(a\) and \(b\). For each pair \((a, b)\), it calculates a sum based on a specific formula and prints the sum minus one. The function does not return any explicit value but prints the result for each test case.

