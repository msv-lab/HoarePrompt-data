#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 10^5, f is a non-negative integer such that 0 ≤ f ≤ n, and for each day i (1 ≤ i ≤ n), k_i and l_i are non-negative integers such that 0 ≤ k_i, l_i ≤ 10^9.
def func():
    n, f = map(int, input().split())
    days = []
    for _ in range(n):
        k, l = map(int, input().split())
        
        days.append((k, l))
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 ≤ `n` ≤ 10^5; `f` is a non-negative integer such that 0 ≤ `f` ≤ `n`; `days` now contains `n` tuples of the form `(k, l)` where each `k` and `l` are integers inputted during each iteration of the loop.
    days.sort(key=lambda x: x[1] - x[0], reverse=True)
    sold = 0
    for i in range(n):
        if i < f:
            sold += min(days[i][0] * 2, days[i][1])
        else:
            sold += min(days[i][0], days[i][1])
        
    #State of the program after the  for loop has been executed: `sold` is the sum of `min(days[i][0] * 2, days[i][1])` for `i` from `0` to `f-1` and `min(days[i][0], days[i][1])` for `i` from `f` to `n-1`, `n` is an integer such that 1 ≤ `n` ≤ 10^5, `f` is a non-negative integer such that 0 ≤ `f` ≤ `n`, `days` is sorted in descending order based on the values of `l - k`.
    print(sold)
#Overall this is what the function does:The function accepts input values for `n` and `f`, then reads `n` pairs of non-negative integers `(k_i, l_i)`. It calculates the total number `sold` based on specific rules: for the first `f` days, it takes the minimum of `k_i * 2` and `l_i`, and for the remaining days, it takes the minimum of `k_i` and `l_i`. Finally, it prints the total `sold`. The function does not handle invalid inputs nor does it return any value; it only prints the result.

