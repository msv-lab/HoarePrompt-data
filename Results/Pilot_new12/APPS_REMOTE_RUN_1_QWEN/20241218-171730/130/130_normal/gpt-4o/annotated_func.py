#State of the program right berfore the function call: $N$, $M$, $K$, and $L$ are integers such that $1 \le K \le N \le 10^{18}$, $1 \le M, L \le 10^{18}$, and $M \cdot N \ge K + L$.
def func():
    input = sys.stdin.read
    N, M, K, L = map(int, input().split())
    min_x = (L + M - 1) // M
    if (M * min_x <= N - K) :
        print(min_x)
    else :
        print(-1)
    #State of the program after the if-else block has been executed: *`N` is an integer such that \(1 \le K \le N \le 10^{18}\); `M` is an integer such that \(1 \le M \le 10^{18}\); `K` is an integer such that \(1 \le K \le N\); `L` is an integer such that \(1 \le L \le 10^{18}\); `min_x` is \(\left\lfloor \frac{L + M - 1}{M} \right\rfloor\); and the function prints either `min_x` if \(M \cdot min_x \le N - K\) or -1 if \(M \cdot min_x > N - K\).
#Overall this is what the function does:The function reads four integers \(N\), \(M\), \(K\), and \(L\) from standard input where \(1 \le K \le N \le 10^{18}\), \(1 \le M, L \le 10^{18}\), and \(M \cdot N \ge K + L\). It then calculates the minimum value of \(x\) such that \(M \cdot x \le N - K\), where \(x = \left\lfloor \frac{L + M - 1}{M} \right\rfloor\). If such an \(x\) exists, it prints \(x\); otherwise, it prints \(-1\). The function does not accept any parameters and returns nothing. Potential edge cases include when \(M \cdot x > N - K\), in which case \(-1\) is printed. The function ensures that the conditions specified in the problem statement are met.

