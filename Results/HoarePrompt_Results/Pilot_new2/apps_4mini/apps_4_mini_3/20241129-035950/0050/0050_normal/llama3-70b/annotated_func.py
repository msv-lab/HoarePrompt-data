#State of the program right berfore the function call: n and m are integers such that 1 <= n <= 30 and 1 <= m <= 30; r is an integer such that 1 <= r <= 1000; s is a list of n integers where each s[i] (1 <= s[i] <= 1000) represents the price of shares to buy; b is a list of m integers where each b[i] (1 <= b[i] <= 1000) represents the price of shares to sell.
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
        
    #State of the program after the  for loop has been executed: `n` is an integer between 1 and 30, `m` is an integer between 1 and 30, `shares` is the total number of shares calculated using the values in `s`, `r` is the remaining amount after distributing shares according to the integers in `s`, and `s` must contain at least `n` elements. If `r` is less than the first element in `s`, then `shares` remains 0 and `r` is unchanged.
    for i in range(m):
        if shares > 0:
            r += shares * b[i]
            shares = 0
        else:
            break
        
    #State of the program after the  for loop has been executed: `n` is an integer between 1 and 30, `m` is an integer between 1 and 30, `shares` is 0, `r` is updated to the remaining amount after distributing shares according to the integers in `s`, which contains at least `n` elements. The loop executes a maximum of `m` times or until `shares` is greater than 0, whichever comes first. If the loop does not execute, `shares` remains the original value calculated from `s` and `r` remains unchanged.
    print(r)
#Overall this is what the function does:The function accepts three integers `n`, `m`, and `r`, where `n` is the number of buy prices, `m` is the number of sell prices, and `r` is the initial amount of money. It also accepts two lists: `s` containing `n` integers representing the buy prices of shares, and `b` containing `m` integers representing the sell prices of shares. The function calculates how many shares can be bought with the available amount `r` based on the lowest buy prices in `s` and then attempts to sell these shares at the highest prices in `b`. Finally, the function outputs the remaining amount of money `r`. If no shares can be bought, the output will be the initial value of `r`. The function does not handle cases where `n` or `m` might be zero as it assumes they are both at least one.

