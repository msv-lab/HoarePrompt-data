#State of the program right berfore the function call: n and m are integers such that 2 ≤ n, m ≤ 10^9 and n is always even, k is an integer such that 0 ≤ k < n * m.
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
        #State of the program after the if-else block has been executed: *`n` is an even integer such that \(2 \leq n \leq 10^9\), `m` is an integer such that \(2 \leq m \leq 10^9\), and `k` is an integer such that \(0 \leq k < n \times 2 - 2\) and \(k \geq n - 1\). If \(k < n \times 2 - 2\), the print statement outputs \((2n - k - 2, 1)\). If \(k \geq n \times 2 - 2\), the condition is impossible because \(k\) cannot be both less than \(n \times 2 - 2\) and greater than or equal to \(n \times 2 - 2\) simultaneously.
    #State of the program after the if-else block has been executed: *`n` is an even integer such that \(2 \leq n \leq 10^9\), `m` is an integer such that \(2 \leq m \leq 10^9\), and `k` is an integer such that \(0 \leq k < n \times 2 - 2\). If \(k < n - 1\), the current value of `k` is less than `n - 1`. If \(k \geq n - 1\), the print statement outputs \((2n - k - 2, 1)\).
#Overall this is what the function does:The function `func` reads three integers `n`, `m`, and `k` from the input, where `n` is an even integer such that \(2 \leq n \leq 10^9\), `m` is an integer such that \(2 \leq m \leq 10^9\), and `k` is an integer such that \(0 \leq k < n \times m\). It then modifies `k` to be within the range \(0 \leq k < 2n - 2\) by taking `k % (2n - 2)`. Based on the modified value of `k`, the function prints one of the following pairs of integers:
- If \(k < n - 1\), it prints \((k + 1, 1)\).
- If \(n - 1 \leq k < 2n - 2\), it prints \((n - (k - n + 1) \% (n - 1) - 1, (k - n + 1) // (n - 1) + 1)\).
- If \(k = 2n - 2\), it prints \((1, 2)\).

After the function concludes, the state of the program is that `n` remains an even integer such that \(2 \leq n \leq 10^9\), `m` remains an integer such that \(2 \leq m \leq 10^9\), and `k` is now within the range \(0 \leq k < 2n - 2\). The function does not return any value; it only prints the result.

