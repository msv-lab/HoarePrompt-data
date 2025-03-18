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
        
    #State: Output State: The final value of `ans` will be the maximum value among all possible values of `i` and `x // i` that satisfy the conditions within the loop for all iterations of `q` from 1 to the total number of test cases.
    #
    #In simpler terms, after the loop executes all its iterations, the variable `ans` will hold the highest value of `i` or `x // i` that meets the specified conditions for every test case provided. This means `ans` will be updated in each iteration of the outer loop (`for q in range(int(input()))`) with the maximum valid value found for `i` or `x // i` based on the conditions given in the inner loop.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it takes two integers \( x \) and \( n \). It calculates the maximum value of \( i \) or \( \frac{x}{i} \) that satisfies specific conditions: \( x - n \cdot i \geq 0 \) and \( (x - n \cdot i) \% i == 0 \), or \( x - n \cdot \left(\frac{x}{i}\right) \geq 0 \) with \( \frac{x}{i} > 0 \) and \( (x - n \cdot \left(\frac{x}{i}\right)) \% \left(\frac{x}{i}\right) == 0 \). After processing all test cases, it prints the maximum value found for each test case.

