#State of the program right berfore the function call: n, m, r are integers such that 1 <= n <= 30, 1 <= m <= 30, 1 <= r <= 1000. s_i and b_i are integers representing the prices of shares such that 1 <= s_i, b_i <= 1000.**
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
        
    #State of the program after the  for loop has been executed: `n`, `m`, `r`, `s`, `b`, `shares` are integers. `n` and `m` are between 1 and 30. `r` is between 0 and the maximum value of `s`. `s` is a list of integers in ascending order, `b` is a list of integers in descending order. `shares` is updated by adding the integer division of `r` by each element in `s` for each element in `s` where `r` is greater than or equal to the element in `s`. If `r` is less than the current element in `s`, we break out of the loop.
    for i in range(m):
        if shares > 0:
            r += shares * b[i]
            shares = 0
        else:
            break
        
    #State of the program after the  for loop has been executed: After the loop executes, `n`, `m`, `r`, `s`, `b`, `shares` are integers. `n` and `m` are between 1 and 30. `r` is between 0 and the maximum value of `s`. `s` is a list of integers in ascending order, `b` is a list of integers in descending order. If `shares` is greater than 0, then `r` is updated according to the formula `r += shares * b[i]` for each iteration of the loop where `shares` is greater than 0. If `shares` is less than or equal to 0, the loop breaks and all variables remain unchanged.
    print(r)
#Overall this is what the function does:The function `func` reads input for integers `n`, `m`, and `r`, along with lists of integers `s` and `b`. It sorts the lists `s` and `b`, then iterates through `s` to calculate the maximum number of shares that can be bought with `r`. It then iterates through `b` to update `r` based on the number of shares bought. The final value of `r` is printed. The function does not have explicit return values and operates on the predefined constraints.

