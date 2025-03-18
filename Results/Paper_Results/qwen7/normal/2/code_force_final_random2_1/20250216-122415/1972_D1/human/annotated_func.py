#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, n and m are integers such that 1 ≤ n, m ≤ 2⋅10^6. It is also guaranteed that the sum of n and the sum of m over all test cases does not exceed 2⋅10^6.
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
        
    #State: Output State: All variables outside the loop, including `T`, `info`, `a`, and `b`, retain their final values from the last iteration of the loop. Specifically, `a` is the value from the last input `info[0]`, `b` is the maximum integer such that the loop ran from 1 to `b` for that particular input, `i` is `b + 1`, `x` is the value of `x` computed for the final iteration where `a - i * (i - 1) > 0` holds true, and `suma` is the cumulative sum of all valid `x` values calculated during each iteration where the condition `a - i * (i - 1) > 0` was satisfied.
    #
    #In simpler terms, after the loop completes all its iterations, `a` will be the last value from `info[0]`, `b` will be the highest integer that allowed the loop to run through all its iterations for that input, `i` will be `b + 1`, `x` will be the value of `x` computed for the final valid iteration, and `suma` will contain the sum of all valid `x` values from each iteration where the condition `a - i * (i - 1) > 0` was met.
#Overall this is what the function does:The function processes multiple test cases, each containing two integers \(a\) and \(b\). For each test case, it calculates a cumulative sum based on specific conditions involving \(a\) and \(b\). After processing all test cases, it prints the final cumulative sum minus one. The function does not return any value but outputs the result directly.

