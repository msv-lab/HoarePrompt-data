#State of the program right berfore the function call: n and m are integers such that 1 <= n <= 30 and 1 <= m <= 30, r is an integer such that 1 <= r <= 1000, s is a list of n integers where each s[i] (1 <= s[i] <= 1000) represents the price to buy shares, and b is a list of m integers where each b[i] (1 <= b[i] <= 1000) represents the price to sell shares.
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
        
    #State of the program after the  for loop has been executed: `shares` is the total number of shares obtained using the original value of `r` with the elements of `s`, `r` is the remaining value after all applicable divisions, `n` and `m` are integers between 1 and 30, `s` is a sorted list of `n` integers in ascending order, and `b` is a list of integers sorted in descending order.
    for i in range(m):
        if shares > 0:
            r += shares * b[i]
            shares = 0
        else:
            break
        
    #State of the program after the  for loop has been executed: `shares` is 0, `r` is updated to the original value of `r` plus the total contribution from up to the first `m` elements of list `b` (if `shares` was greater than 0 in each iteration), `n` and `m` remain integers between 1 and 30, `s` is a sorted list of `n` integers in ascending order, `b` is a list of integers sorted in descending order. If `shares` was initially 0, then `r` remains unchanged and the loop does not execute.
    print(r)
#Overall this is what the function does:The function accepts input values for `n`, `m`, and `r`, along with two lists `s` and `b`, which represent share prices for buying and selling, respectively. It calculates the total number of shares that can be bought with the available funds `r`, updating it based on the selling prices from list `b`. It then prints the remaining value of `r` after the buying and selling process. If no shares can be bought, the original value of `r` remains unchanged. The function does not accept parameters directly and relies on user input.

