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
        
    #State: Output State: All variables outside the loop, including `T`, `a`, and `b`, retain their final values from the last iteration. Specifically, `t` equals `T-1`, indicating the loop has completed all iterations. `a` and `b` hold the values from the last input `info` provided. The variable `suma` contains the cumulative sum of `x` values calculated over all iterations where `a - i * (i - 1) > 0` for each `i` in the range from 1 to `b`. After the loop completes, `i` would be `b + 1` for the next potential iteration, but since the loop has finished, `i` is no longer tracked individually.
    #
    #In simpler terms, after the loop finishes all its iterations, `T` will be decremented by the number of times the loop ran, `a` and `b` will be the values from the last input, and `suma` will be the total sum of `x` values calculated throughout all iterations.
#Overall this is what the function does:The function processes multiple test cases, each defined by two integers \(a\) and \(b\). For each test case, it calculates a sum based on a specific formula involving \(a\) and \(i\) (where \(i\) ranges from 1 to \(b\)). The final output is the cumulative sum of these calculations for all test cases. The function does not return any value but prints the result for each test case.

