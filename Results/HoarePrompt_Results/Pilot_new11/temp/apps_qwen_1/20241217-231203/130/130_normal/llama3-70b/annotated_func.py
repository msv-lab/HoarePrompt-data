#State of the program right berfore the function call: $N$, $M$, $K$, and $L$ are integers such that $1 \le K \le N \le 10^{18}$, $1 \le M, \,\, L \le 10^{18}$, and $M \times \text{minimum number of coins each friend can gift} \ge L$.
def func():
    N, M, K, L = map(int, input().split())
    if (M >= N - K + 1 and M >= L) :
        print(1)
    else :
        print(-1)
    #State of the program after the if-else block has been executed: $N$, $M$, $K$, and $L$ are integers such that $1 \le K \le N \le 10^{18}$, $1 \le M, \,\, L \le 10^{18}$, and $M \times \text{minimum number of coins each friend can gift} \ge L$. The program prints `1` if $M \ge N - K + 1$ and $M \ge L$. Otherwise, the program prints `-1`.
#Overall this is what the function does:The function takes no direct parameters but operates on the integers \(N\), \(M\), \(K\), and \(L\) which are read from standard input. It checks two conditions: \(M \ge N - K + 1\) and \(M \ge L\). If both conditions are satisfied, it prints `1`. Otherwise, it prints `-1`. The function does not return a value; instead, it outputs either `1` or `-1` based on the evaluation of the conditions. There are no edge cases explicitly handled in the code that are not covered by the given constraints \(1 \le K \le N \le 10^{18}\) and \(1 \le M, L \le 10^{18}\), and the additional constraint \(M \times \text{minimum number of coins each friend can gift} \ge L\). However, the code assumes that the input values satisfy these constraints, and it does not perform any validation to ensure they do.

