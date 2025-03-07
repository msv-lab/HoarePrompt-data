#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^3, and for each test case, x is an integer such that 1 ≤ x ≤ 10^8 and n is an integer such that 1 ≤ n ≤ x.
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
        
    #State: Output State: The value of `ans` will be the maximum value it attains during the entire execution of the loop for all test cases. This value is determined by checking all possible `i` values from 1 to `int(sqrt(x)) + 1` for each test case, and updating `ans` whenever a larger valid `i` is found that meets the specified conditions.
    #
    #In simpler terms, after the loop executes all its iterations, `ans` will hold the highest value that satisfies the given conditions for any `i` within the specified range for each test case.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it reads two integers \(x\) and \(n\). It then finds the maximum integer \(i\) such that \(x - n \cdot i \geq 0\) and both \(x - n \cdot i\) and \(x\) are divisible by \(i\), for all \(i\) in the range from 1 to \(\sqrt{x}\). After processing all test cases, it prints the maximum value of \(i\) found for each test case.

