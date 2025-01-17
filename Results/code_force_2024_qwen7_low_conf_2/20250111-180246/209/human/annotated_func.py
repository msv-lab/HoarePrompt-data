#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^3, and for each test case, x is an integer such that 1 ≤ x ≤ 10^8 and n is an integer such that 1 ≤ n ≤ x.
def func():
    for _ in range(int(input())):
        x, n = map(int, input().split())
        
        ans = 1
        
        for i in range(1, int(x ** 0.5) + 1):
            if x % i == 0:
                if n <= x // i:
                    ans = max(ans, i)
                if n <= i:
                    ans = max(ans, x // i)
        
        print(ans)
        
    #State of the program after the  for loop has been executed: `t` is the number of test cases, `x` is the last positive integer input, `n` is the last integer input such that \(1 \leq n \leq x\), and `ans` is the maximum value between any `i` such that `x % i == 0` and `n <= x // i` or any `x // i` such that `n <= i`.
#Overall this is what the function does:The function processes multiple test cases, each defined by three integers \(t\), \(x\), and \(n\) where \(1 \leq t \leq 10^3\), \(1 \leq x \leq 10^8\), and \(1 \leq n \leq x\). For each test case, it finds and prints the maximum integer \(i\) (where \(1 \leq i \leq \sqrt{x}\)) such that \(x\) is divisible by \(i\) and \(n \leq i\), or the maximum integer \(j = x // i\) such that \(n \leq j\) and \(x\) is divisible by \(j\). If \(t\) is out of the valid range, the function prints an error message.

