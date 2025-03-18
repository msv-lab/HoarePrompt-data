#State of the program right berfore the function call: n and m are even and positive integers such that 2 ≤ n, m ≤ 10^9, and k is an integer such that 0 ≤ k < n·m.
def func():
    n, m, k = map(int, input().split())
    k %= n * 2 - 2
    if (k < n - 1) :
        print(k + 1, 1)
    else :
        if (k < n * 2 - 2) :
            print(n - (k - n + 1) % (n - 1) - 1, (k - n + 1) // (n - 1) + 1)
        else :
            print(1, 2)
        #State of the program after the if-else block has been executed: *`n` is an even and positive integer within the range [2, \(10^9\)], `m` is an even and positive integer within the range [2, \(10^9\)], `k` is an integer such that \(0 \leq k < n \cdot m\) and `k` is updated to be `k % (n * 2 - 2)\), and `k` is greater than or equal to `n - 1`, and the output is determined as follows:
        #- If \( k < n * 2 - 2 \), the output consists of two numbers: \( 2n - k - 2 \) and \( (k - n + 1) // (n - 1) + 1 \).
        #- If \( k \geq n * 2 - 2 \), the output is 1 and 2.
    #State of the program after the if-else block has been executed: `n` is an even and positive integer within the range [2, \(10^9\)], `m` is an even and positive integer within the range [2, \(10^9\)], `k` is an integer such that \(0 \leq k < n \cdot m\). If `k < n - 1`, then `k` is incremented by 1 and 1 is printed. Otherwise, `k` is updated to `k % (n * 2 - 2)`, and the output is determined as follows:
    #- If \(0 \leq k < n * 2 - 2\), the output consists of two numbers: \(2n - k - 2\) and \(\frac{k - n + 1}{n - 1} + 1\).
    #- If \(k \geq n * 2 - 2\), the output is 1 and 2.
#Overall this is what the function does:The function accepts three integer inputs `n`, `m`, and `k` where `n` and `m` are even and positive integers within the range \(2 \leq n, m \leq 10^9\) and `k` is an integer such that \(0 \leq k < n \cdot m\). It calculates and prints a pair of integers based on the value of `k`. Specifically, `k` is first reduced modulo \(n \cdot 2 - 2\). Depending on the value of `k`:
- If \(0 \leq k < n - 1\), it prints \(k + 1\) and \(1\).
- If \(n - 1 \leq k < n \cdot 2 - 2\), it calculates and prints \(2n - k - 2\) and \(\frac{k - n + 1}{n - 1} + 1\).
- If \(k \geq n \cdot 2 - 2\), it prints \(1\) and \(2\).

This covers all possible values of `k` and ensures the correct output is produced based on the adjusted value of `k`. There are no explicit return values, so the function's effect is observable through its printed output.

