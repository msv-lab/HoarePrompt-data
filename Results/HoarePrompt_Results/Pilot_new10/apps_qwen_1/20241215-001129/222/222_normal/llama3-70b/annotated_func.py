#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 1000, and k is an integer such that 0 ≤ k ≤ 1000.
def func():
    n, k = map(int, input().split())
    l = (n + k - 1) // (k * 2 + 1)
    res = []
    for i in range(l):
        res.append(i * (k * 2 + 1) + 1)
        
    #State of the program after the  for loop has been executed: - `n` is an integer such that \(1 \leq n \leq 1000\).
    #- `k` is an integer such that \(0 \leq k \leq 1000\).
    #- `l` is calculated as \((n + k - 1) // (k * 2 + 1)\).
    #- `res` is a list containing integers of the form `i * (k * 2 + 1) + 1` for \(i\) ranging from 0 to \(l-1\) if \(l > 0\). If \(l = 0\), `res` is an empty list.
    #
    #Thus, the final output state is:
    print(l)
    print(' '.join(map(str, res)))
#Overall this is what the function does:The function reads two integers `n` and `k` from input, calculates `l` using the formula `(n + k - 1) // (k * 2 + 1)`, and constructs a list `res` containing integers starting from 1 and increasing by `k * 2 + 1` for `l` times. It then prints the value of `l` followed by the elements of `res` separated by spaces.

