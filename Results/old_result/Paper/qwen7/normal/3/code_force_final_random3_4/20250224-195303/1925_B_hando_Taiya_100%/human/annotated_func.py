#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^3, and for each test case, x is an integer such that 1 ≤ x ≤ 10^8 and n is an integer such that 1 ≤ n ≤ x.
def func_1():
    x, n = list(map(int, input().split()))
    ans = 0
    for i in range(1, isqrt(x) + 1):
        if x % i == 0:
            if n <= x // i:
                ans = max(ans, i)
            if n <= i:
                ans = max(ans, x // i)
        
    #State: Output State: The value of `ans` will be the largest integer \( d \) such that \( d \) is a divisor of \( x \) and either \( d \) or \( x / d \) is less than or equal to \( n \).
    #
    #This output state is derived from the loop's behavior. The loop iterates over all integers from 1 to \( \lfloor \sqrt{x} \rfloor \), checking if they are divisors of \( x \). For each divisor \( i \), it updates `ans` to be the maximum of its current value and either \( i \) or \( x // i \), provided that \( n \leq x // i \) or \( n \leq i \). After all iterations, `ans` will hold the largest divisor \( d \) of \( x \) that meets the specified condition.
    print(ans)
    #This is printed: ans (where ans is the largest divisor of x such that either d or x/d is less than or equal to n)
#Overall this is what the function does:The function processes multiple test cases, each consisting of three integers: t, x, and n. For each test case, it finds and prints the largest divisor of x such that either the divisor or its complement (x divided by the divisor) is less than or equal to n.

