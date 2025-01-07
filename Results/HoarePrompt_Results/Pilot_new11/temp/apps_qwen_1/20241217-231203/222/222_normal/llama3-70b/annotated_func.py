#State of the program right berfore the function call: n and k are integers such that 1 ≤ n ≤ 1000 and 0 ≤ k ≤ 1000.
def func():
    n, k = map(int, input().split())
    l = (n + k - 1) // (k * 2 + 1)
    res = []
    for i in range(l):
        res.append(i * (k * 2 + 1) + 1)
        
    #State of the program after the  for loop has been executed: `n` is an integer such that \(1 \leq n \leq 1000\); `k` is an integer such that \(0 \leq k \leq 1000\); `n > k + 2`; `res` is a list containing all integers of the form \(i * (k * 2 + 1) + 1\) for \(0 \leq i < l\).
    print(l)
    print(' '.join(map(str, res)))
#Overall this is what the function does:The function reads two integers \(n\) and \(k\) from the standard input, where \(1 \leq n \leq 1000\) and \(0 \leq k \leq 1000\). It calculates the largest integer \(l\) such that \(n > (k + 1) \cdot l\), and then generates a list of integers starting from 1 up to \(n\) in steps of \(k + 1\). Finally, it prints the value of \(l\) followed by the list of integers. If \(n \leq k + 1\), the list generated will be empty. If \(n\) is exactly divisible by \(k + 1\), the last number in the list will be equal to \(n\). If \(n\) is not exactly divisible, the last number in the list will be less than \(n\).

