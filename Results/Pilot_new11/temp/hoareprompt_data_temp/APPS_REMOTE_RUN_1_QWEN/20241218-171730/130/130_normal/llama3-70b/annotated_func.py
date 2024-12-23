#State of the program right berfore the function call: $N$, $M$, $K$, and $L$ are positive integers such that $1 \le K \le N \le 10^{18}$ and $1 \le M, L \le 10^{18}$.
def func():
    N, M, K, L = map(int, input().split())
    if (M >= N - K + 1 and M >= L) :
        print(1)
    else :
        print(-1)
    #State of the program after the if-else block has been executed: `N`, `M`, `K`, `L` are input integers satisfying \(1 \le K \le N \le 10^{18}\) and \(1 \le M, L \le 10^{18}\). If both conditions `M >= N - K + 1` and `M >= L` are true, the console prints `1`. Otherwise, the console prints `-1`.
#Overall this is what the function does:The function takes four positive integers \(N\), \(M\), \(K\), and \(L\) as input, where \(1 \le K \le N \le 10^{18}\) and \(1 \le M, L \le 10^{18}\). It checks two conditions: \(M \ge N - K + 1\) and \(M \ge L\). If both conditions are satisfied, the function prints `1`. Otherwise, it prints `-1`. There are no additional actions performed by the function other than printing `1` or `-1` based on the conditions. The function does not modify any of the input variables and only uses them in its conditional logic. The final state of the program after the function concludes is that it has printed either `1` or `-1` based on the evaluated conditions.

