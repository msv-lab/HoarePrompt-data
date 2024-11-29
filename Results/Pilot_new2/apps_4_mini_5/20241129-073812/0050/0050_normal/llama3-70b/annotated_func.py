#State of the program right berfore the function call: n and m are integers such that 1 <= n, m <= 30; r is an integer such that 1 <= r <= 1000; s is a list of n integers where each element s[i] (1 <= s[i] <= 1000) represents the buying price of shares; b is a list of m integers where each element b[j] (1 <= b[j] <= 1000) represents the selling price of shares.
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
        
    #State of the program after the  for loop has been executed: `shares` is the sum of all `r // s[i]` for each `i` such that `r >= s[i]`, `r` is the remainder after the last valid division (or remains unchanged if no divisions were valid), `n` is the original number of elements in `s`, and `m` is the original size of `b`.
    for i in range(m):
        if shares > 0:
            r += shares * b[i]
            shares = 0
        else:
            break
        
    #State of the program after the  for loop has been executed: `shares` is the sum of all `r // s[i]` for each `i` such that `r >= s[i]` or `shares` is 0 if no valid divisions occurred, `r` is the original value plus `shares * b[i]` for each `i` where `shares` was greater than 0, `n` is the original number of elements in `s`, `m` is the original size of `b`, and `i` is equal to `m` if the loop executed completely or 0 if the loop did not execute.
    print(r)
#Overall this is what the function does:The function accepts integers `n`, `m`, and `r`, and two lists of integers `s` and `b` representing buying and selling prices of shares, respectively. It calculates how many shares can be bought with the amount `r` based on the buying prices in `s`, and then calculates the total amount after selling those shares at the prices in `b`. Finally, it prints the resulting amount `r`. If no shares can be bought initially, the function will simply print the original value of `r`.

