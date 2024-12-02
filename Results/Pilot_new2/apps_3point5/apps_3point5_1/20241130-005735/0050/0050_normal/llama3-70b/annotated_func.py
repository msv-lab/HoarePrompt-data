#State of the program right berfore the function call: n, m, r are all positive integers such that 1 <= n <= 30, 1 <= m <= 30, 1 <= r <= 1000. s_i and b_i are positive integers representing the prices of buying and selling shares respectively, such that 1 <= s_i, b_i <= 1000.**
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
        
    #State of the program after the  for loop has been executed: After the loop executes, the value of `shares` will be the total number of shares bought, `r` will be the remaining amount of money, and `i` will be equal to the number of iterations that the loop went through. The values of `n`, `m`, `s`, and `b` will remain the same as their original values as they are not modified within the loop.
    for i in range(m):
        if shares > 0:
            r += shares * b[i]
            shares = 0
        else:
            break
        
    #State of the program after the  for loop has been executed: `shares` is 0, `r` is the sum of `shares * b[i]` for all i in range(m) such that shares > 0, `i` is equal to the number of iterations the loop went through, `n`, `m`, `s`, and `b` remain the same as their original values, `m` must be greater than or equal to 1
    print(r)
#Overall this is what the function does:The function accepts inputs `n`, `m`, and `r` satisfying certain constraints. It then processes the prices of buying and selling shares, calculates the total profit earned from buying and selling shares, and outputs the final amount `r`. The function ensures that shares are bought based on the available amount `r` and the share prices `s`, and then calculates the profit after selling shares according to prices `b`. However, there is a missing edge case where if the shares bought cannot be sold due to unsuitable market conditions, the function might not provide an accurate profit calculation.

