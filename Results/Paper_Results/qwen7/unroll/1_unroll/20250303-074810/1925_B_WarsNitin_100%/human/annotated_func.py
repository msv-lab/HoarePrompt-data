#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^3, and for each test case, x and n are positive integers such that 1 ≤ x ≤ 10^8 and 1 ≤ n ≤ x.
def func():
    for q in range(int(input())):
        x, n = list(map(int, input().split(' ')))
        
        ans = 1
        
        for i in range(1, int(sqrt(x)) + 1):
            if x % i == 0:
                if x - n * i >= 0 and (x - n * i) % i == 0:
                    ans = max(ans, i)
                if x - n * (x // i) >= 0 and x // i > 0 and (x - n * (x // i)) % (x //
                    i) == 0:
                    ans = max(ans, x // i)
        
        print(ans)
        
    #State: Output State: t is a positive integer such that 1 ≤ t ≤ 10^3, and for each test case, x and n are positive integers such that 1 ≤ x ≤ 10^8 and 1 ≤ n ≤ x. After executing the loop, ans is the maximum value among all possible divisors i of x that satisfy the conditions: x - n * i ≥ 0 and (x - n * i) % i == 0, or x - n * (x // i) ≥ 0, x // i > 0, and (x - n * (x // i)) % (x // i) == 0.
#Overall this is what the function does:The function processes multiple test cases, each defined by positive integers \( x \) and \( n \) where \( 1 \leq x \leq 10^8 \) and \( 1 \leq n \leq x \). For each test case, it calculates and prints the maximum divisor \( i \) of \( x \) that satisfies either of two conditions: \( x - n \cdot i \geq 0 \) and \( (x - n \cdot i) \% i == 0 \), or \( x - n \cdot (x // i) \geq 0 \), \( x // i > 0 \), and \( (x - n \cdot (x // i)) \% (x // i) == 0 \). The function does not return any value but prints the result for each test case.

