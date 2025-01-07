#State of the program right berfore the function call: n, m, r are all integers such that 1 <= n <= 30, 1 <= m <= 30, 1 <= r <= 1000. s_i and b_i are integers indicating the price of shares such that 1 <= s_i, b_i <= 1000.**
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
        
    #State of the program after the  for loop has been executed: After the loop finishes executing, shares will contain the maximum number of shares that can be bought with the initial value of r, based on the prices of shares in the list s. n, m, r remain the same as in the initial state.
    for i in range(m):
        if shares > 0:
            r += shares * b[i]
            shares = 0
        else:
            break
        
    #State of the program after the  for loop has been executed: Shares contain the maximum number of shares that can be bought with the updated value of r based on the prices of shares in the list s. i is greater than or equal to m, m must be greater than 0. If shares > 0, r is increased by the product of shares and b[i], shares become 0. If shares <= 0, we break out of the most internal loop or if statement.
    print(r)
#Overall this is what the function does:The function `func` reads input values for `n`, `m`, `r`, a list of share prices `s`, and a list of share values `b`. It then calculates the maximum number of shares that can be bought with the initial value of `r` based on the share prices in list `s`. After that, it updates the value of `r` based on share values in list `b`. The final value of `r` is printed as output. The function does not return a specific value and operates within the given constraints.

