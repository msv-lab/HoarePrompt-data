#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^3, and for each test case, x is a positive integer such that 1 ≤ x ≤ 10^8 and n is a positive integer such that 1 ≤ n ≤ x.
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
        
    #State: The final value of `ans` is the maximum value among all `i` and `x // i` that satisfy the conditions within the loop for all iterations.
#Overall this is what the function does:The function processes multiple test cases, each involving two integers \( x \) and \( n \). For each test case, it calculates the maximum value of \( i \) such that \( x - n \cdot i \) is divisible by \( i \) and \( x - n \cdot i \geq 0 \), and similarly for \( x // i \). The function prints the maximum value found for each test case.

