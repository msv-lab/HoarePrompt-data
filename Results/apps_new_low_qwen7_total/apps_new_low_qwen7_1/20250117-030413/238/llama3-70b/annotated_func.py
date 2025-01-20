#State of the program right berfore the function call: The input consists of three integers n, m, and k, where 1 ≤ n ≤ m ≤ 10^9 and 1 ≤ k ≤ n.
def func():
    n, m, k = map(int, input().split())
    if (k == 1) :
        print(min(m // n, m - (n - 1)))
    else :
        print(min(m // n + 1, m - (n - k)))
    #State of the program after the if-else block has been executed: *`n`, `m`, and `k` are integers. If `k` equals 1, the function prints `m // n`. Otherwise, the function compares `m // n + 1` and `m - n + k` to determine the output.
#Overall this is what the function does:The function accepts three parameters \( n \), \( m \), and \( k \). It prints the minimum value between two expressions: \( \text{min}(m // n, m - (n - 1)) \) if \( k = 1 \), and \( \text{min}(m // n + 1, m - (n - k)) \) otherwise. The function does not return any value but outputs the result directly. Potential edge cases include when \( k > n \), which is not handled in the given code, leading to an incorrect behavior since the condition \( k \leq n \) is not checked explicitly.

