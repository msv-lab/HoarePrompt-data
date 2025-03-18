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
        
    #State: Output State: t is a positive integer such that 1 ≤ t ≤ 10^3, and for each test case, x is a positive integer such that 1 ≤ x ≤ 10^8 and n is a positive integer such that 1 ≤ n ≤ x, and after executing the loop, ans is the maximum value of i or x // i that satisfies the given conditions for each test case.
#Overall this is what the function does:The function processes multiple test cases, each defined by values of \(x\) and \(n\), where \(1 \leq x \leq 10^8\) and \(1 \leq n \leq x\). For each test case, it calculates the maximum value of \(i\) or \(\frac{x}{i}\) such that \(x - n \cdot i \geq 0\) and \((x - n \cdot i) \% i == 0\), or \(x - n \cdot \left(\frac{x}{i}\right) \geq 0\) and \(\frac{x}{i} > 0\) and \((x - n \cdot \left(\frac{x}{i}\right)) \% \left(\frac{x}{i}\right) == 0\). After processing all test cases, it prints the result for each test case.

