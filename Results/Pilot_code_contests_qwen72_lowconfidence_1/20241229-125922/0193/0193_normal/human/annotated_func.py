#State of the program right berfore the function call: n is an integer where 2 ≤ n ≤ 2000, and ai is a list of n integers where 1 ≤ ai ≤ 5000, with all ai being distinct.
def func():
    n = int(raw_input())
    a = map(int, raw_input().split())
    d = [0] * 5000
    for i in xrange(n):
        for j in xrange(i + 1, n):
            d[a[j] - a[i]] += 1
        
    #State of the program after the  for loop has been executed: `n` is an integer where \(2 \leq n \leq 2000\), `a` is a list of `n` distinct integers where \(1 \leq a_i \leq 5000\), `d` is a list of 5000 integers where the value at index \( k \) (where \(1 \leq k \leq 4999\)) is the number of pairs `(i, j)` such that \( a[j] - a[i] = k \) for all \( 0 \leq i < j < n \).
    c = [0] * 5000
    for i in xrange(1, 5000):
        c[i] = c[i - 1] + d[i]
        
    #State of the program after the  for loop has been executed: `n` is an integer where \(2 \leq n \leq 2000\), `a` is a list of `n` distinct integers where \(1 \leq a_i \leq 5000\), `d` is a list of 5000 integers, `c` is a list of 5000 elements where `c[0]` is 0 and for \(1 \leq i \leq 4999\), `c[i]` is the cumulative sum of `d` from `d[1]` to `d[i]`, `i` is 4999.
    ans, m = 0.0, float(sum(d))
    for i in xrange(4999, 0, -1):
        if d[i] == 0:
            continue
        
        for j in xrange(i):
            ans += d[i] / m * (d[j] / m) * (c[i - j - 1] / m)
        
    #State of the program after the  for loop has been executed: `n` is an integer where \(2 \leq n \leq 2000\), `a` is a list of `n` distinct integers where \(1 \leq a_i \leq 5000\), `d` is a list of 5000 integers, `c` is a list of 5000 elements where `c[0]` is 0 and for \(1 \leq i \leq 4999\), `c[i]` is the cumulative sum of `d` from `d[1]` to `d[i]`, `i` is 0, `ans` is the sum of \(\frac{d[i]}{m} \times \frac{d[j]}{m} \times \frac{c[i - j - 1]}{m}\) for all \(1 \leq i \leq 4999\) and \(0 \leq j < i\) where `d[i]` and `d[j]` are not 0, `m` is the sum of all elements in `d` as a float.
    print('{0:.10f}'.format(ans))
#Overall this is what the function does:The function `func` reads an integer `n` and a list `a` of `n` distinct integers from the user, where `2 ≤ n ≤ 2000` and `1 ≤ ai ≤ 5000`. It then calculates the probability distribution of differences between pairs of elements in `a` and uses this distribution to compute a specific expected value. The final result, which is a floating-point number representing this expected value, is printed with 10 decimal places. The function does not return any value; instead, it directly prints the result. The state of the program after the function concludes includes the original input values `n` and `a`, and the computed expected value is printed to the console.

