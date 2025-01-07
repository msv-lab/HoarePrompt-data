#State of the program right berfore the function call: $N$, $M$, $K$, and $L$ are integers such that $1 \le K \le N \le 10^{18}$, $1 \le M, L \le 10^{18}$, and $M \times (\text{minimum number of coins one friend can gift}) \ge L$.
def func():
    input = sys.stdin.read
    N, M, K, L = map(int, input().split())
    min_x = (L + M - 1) // M
    if (M * min_x <= N - K) :
        print(min_x)
    else :
        print(-1)
    #State of the program after the if-else block has been executed: *`N`, `M`, `K`, and `L` are integers assigned values from input, such that \(1 \le K \le N \le 10^{18}\), \(1 \le M, L \le 10^{18}\), and \(M \times (\text{minimum number of coins one friend can gift}) \ge L\); `min_x` is \((L + M - 1) // M\). If \(M \times min_x \le N - K\), then `min_x` is printed. Otherwise, \(-1\) is printed.
#Overall this is what the function does:The function reads four integers \(N\), \(M\), \(K\), and \(L\) from standard input, where \(1 \le K \le N \le 10^{18}\), \(1 \le M, L \le 10^{18}\), and \(M \times (\text{minimum number of coins one friend can gift}) \ge L\). It calculates the minimum number of coins one friend can gift, denoted as `min_x`, using the formula \((L + M - 1) // M\). If \(M \times min_x \le N - K\), it prints `min_x`; otherwise, it prints \(-1\). If \(K\) exceeds \(N\), the function will still execute the calculation and print \(-1\).

