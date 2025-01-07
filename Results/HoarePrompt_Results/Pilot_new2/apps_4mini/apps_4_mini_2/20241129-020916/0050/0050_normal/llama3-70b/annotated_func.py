#State of the program right berfore the function call: n is an integer such that 1 <= n <= 30, m is an integer such that 1 <= m <= 30, r is an integer such that 1 <= r <= 1000, s is a list of n integers where each s[i] (1 <= s[i] <= 1000) represents the price to buy shares, and b is a list of m integers where each b[i] (1 <= b[i] <= 1000) represents the price to sell shares.
def func():
    n, m, r = map(int, input().split())
    s = list(map(int, input().split()))
    b = list(map(int, input().split()))
    s.sort()
    b.sort(reverse=True)
    shares = 0
    for i in range(n):
        if r >= s[i]:
            shares += r // s[i]
            r %= s[i]
        else:
            break
        
    #State of the program after the  for loop has been executed: `n` is an integer (1 <= n <= 30), `m` is an integer (1 <= m <= 30), `r` is an integer in the range (1 <= r <= 1000) that is less than all elements of `s` after all iterations, `s` is a sorted list of `n` integers (1 <= s[i] <= 1000), `b` is a list of `m` integers sorted in descending order, `shares` is the total number of shares calculated from dividing `r` by each element of `s` that `r` was greater than or equal to, and `i` is equal to the total number of iterations executed (0 <= i <= n). If the loop didn't execute, `shares` remains 0.
    for i in range(m):
        if shares > 0:
            r += shares * b[i]
            shares = 0
        else:
            break
        
    #State of the program after the  for loop has been executed: `n` is an integer (1 <= n <= 30), `m` is an integer (1 <= m <= 30), `r` is an integer (1 <= r <= 1000) that is less than all elements of `s`, `s` is a sorted list of `n` integers (1 <= s[i] <= 1000), `b` is a list of `m` integers sorted in descending order, `shares` is 0, and `i` is equal to `m`. After all iterations, `r` remains less than all elements of `s`, as `shares` was never greater than 0 to update `r`.
    print(r)
#Overall this is what the function does:The function accepts integers `n`, `m`, `r`, a list `s` of buying prices, and a list `b` of selling prices. It calculates the total number of shares that can be bought with `r` and attempts to sell them at the prices in `b`, printing the final amount of `r`, which may remain unchanged if no shares were bought.

