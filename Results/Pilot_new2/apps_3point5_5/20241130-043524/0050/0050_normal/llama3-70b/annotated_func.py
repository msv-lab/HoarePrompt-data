#State of the program right berfore the function call: **Precondition**: **n, m, r are integers such that 1 <= n <= 30, 1 <= m <= 30, 1 <= r <= 1000. s_i and b_i are integers such that 1 <= s_i, b_i <= 1000.**
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
        
    #State of the program after the  for loop has been executed: `n` must be greater than 0, `shares` contains the total number of shares earned after dividing and updating `r` by each element in `s`, and `r` contains the final remainder after the division is completed for all elements in `s`.
    for i in range(m):
        if shares > 0:
            r += shares * b[i]
            shares = 0
        else:
            break
        
    #State of the program after the  for loop has been executed: `n` is greater than 0, `shares` is 0, `r` contains the final remainder after the division is completed for all elements in `s`. The loop does not execute as `shares` is initially 0, and the program immediately breaks out of the loop without executing any iterations.
    print(r)
#Overall this is what the function does:The function `func` reads input for `n`, `m`, and `r`, followed by lists `s` and `b`. It sorts `s` in ascending order and `b` in descending order. It then iterates through `s` and calculates the total number of shares earned based on the remainder `r` after division. After the first loop completes, it iterates through `b` and updates `r` based on shares earned. The final value of `r` is printed. The function does not accept any parameters, and it does not have a return value.

