#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n and m are positive integers such that 1 ≤ n, m ≤ 2 \cdot 10^6, and the sum of n and the sum of m over all test cases does not exceed 2 \cdot 10^6.
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
        
    #State: Output State: The loop will have executed for all values of `t` from 0 to `T-1`. Therefore, `t` will be equal to `T-1`. The variable `T` remains as the initial positive integer provided. The variable `info` remains unchanged, holding the list of strings split from the input. The variable `a` remains as the first element of `info` converted to an integer. The variable `b` remains as the second element of `info` converted to an integer. The variable `suma` is the sum of all `x` values calculated during the loop's iterations for each `t` from 0 to `T-1`, where `a - i * (i - 1) > 0` for all `i` in the range 1 to `b`. After all iterations, `suma` will be printed, followed by `suma - 1`.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two positive integers \( n \) and \( m \). For each test case, it calculates a value based on the formula involving \( a \) and \( b \), where \( a \) and \( b \) are derived from \( n \) and \( m \). Specifically, it computes the sum of certain terms \( x \) for each \( i \) in the range from 1 to \( b \), where \( x \) is determined by the condition \( a - i \cdot (i - 1) > 0 \). Finally, it prints the computed sum minus one for each test case.

