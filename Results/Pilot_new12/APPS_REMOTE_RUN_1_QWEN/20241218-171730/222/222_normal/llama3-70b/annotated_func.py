#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 1000, and k is an integer such that 0 ≤ k ≤ 1000.
def func():
    n, k = map(int, input().split())
    l = (n + k - 1) // (k * 2 + 1)
    res = []
    for i in range(l):
        res.append(i * (k * 2 + 1) + 1)
        
    #State of the program after the  for loop has been executed: `n` is an integer where \(1 \leq n \leq 1000\) and \(n > k + 2\); `k` is an integer where \(0 \leq k \leq 1000\); `l` is \(\frac{n + k - 1}{k * 2 + 1}\) and \(l > 0\); `res` is a list containing \([i * (k * 2 + 1) + 1 \mid 0 \leq i < l]\)
    print(l)
    print(' '.join(map(str, res)))
#Overall this is what the function does:The function takes two integers, `n` and `k`, as input where \(1 \leq n \leq 1000\) and \(0 \leq k \leq 1000\). It calculates the value of `l` as \(\left\lfloor \frac{n + k - 1}{k * 2 + 1} \right\rfloor\) and constructs a list `res` containing the first `l` numbers of the form \(i * (k * 2 + 1) + 1\) for \(0 \leq i < l\). The function then prints the value of `l` and the elements of `res` separated by spaces. The function does not return any value but prints the calculated `l` and `res`. There is no check to ensure \(n > k + 2\), which is stated in the annotation but not in the code, so the code can handle cases where \(n \leq k + 2\).

