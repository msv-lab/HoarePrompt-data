#State of the program right berfore the function call: N, M, K, L are integers such that 1 ≤ K ≤ N ≤ 10^18 and 1 ≤ M, L ≤ 10^18, and M * (N - K) ≥ L.
def func():
    input = sys.stdin.read
    N, M, K, L = map(int, input().split())
    min_x = (L + M - 1) // M
    if (M * min_x <= N - K) :
        print(min_x)
    else :
        print(-1)
    #State of the program after the if-else block has been executed: *`N`, `M`, `K`, `L` are integers such that 1 ≤ `K` ≤ `N` ≤ 10^18 and 1 ≤ `M`, `L` ≤ 10^18, and `M` * (`N` - `K`) ≥ `L`; `min_x` = (L + M - 1) // M. If `M * min_x` is less than or equal to `N - K`, `min_x` is printed. Otherwise, `-1` is printed.
#Overall this is what the function does:The function reads four integers \(N\), \(M\), \(K\), and \(L\) from standard input, where \(1 \leq K \leq N \leq 10^{18}\) and \(1 \leq M, L \leq 10^{18}\), and \(M \times (N - K) \geq L\). It calculates the minimum integer value of \(x\) such that \(M \times x \leq N - K\). If such an \(x\) exists, it prints \(x\); otherwise, it prints \(-1\). The function does not accept any parameters and returns nothing.

