#State of the program right berfore the function call: n, m, r are integers such that 1 <= n <= 30, 1 <= m <= 30, 1 <= r <= 1000. s_i and b_i are integers such that 1 <= s_i, b_i <= 1000.**
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
        
    #State of the program after the  for loop has been executed: `n` is greater than or equal to 1, `m`, `r`, `s_i`, `b_i` are unchanged, `s` is a sorted list of integers in ascending order, `b` is a sorted list of integers in descending order, `shares` contains the total number of shares obtained by performing floor division operations during the loop for all valid `i` values. `i` is equal to n-1 at the end of the loop
    for i in range(m):
        if shares > 0:
            r += shares * b[i]
            shares = 0
        else:
            break
        
    #State of the program after the  for loop has been executed: If shares > 0, `r` is updated to its initial value plus the product of `shares` and the sum of `i` elements from the list `b`. All other variables remain unchanged except `i` which becomes equal to m, and `shares` is set to 0. If shares <= 0, all variables remain unchanged and the loop does not execute.
    print(r)
#Overall this is what the function does:The function `func` reads input values for `n`, `m`, and `r`, along with lists of integers for `s` and `b`. It then sorts `s` in ascending order and `b` in descending order. The function iterates through the elements of `s` and calculates the total number of shares based on the floor division of `r` by each element. After that, it iterates through the elements of `b` and updates `r` by adding the product of shares and the elements of `b` if shares are greater than 0. Finally, it prints the value of `r`. The function does not accept any parameters and operates solely on the predefined constraints. Missing functionality includes error handling for cases where input values do not meet the specified constraints.

