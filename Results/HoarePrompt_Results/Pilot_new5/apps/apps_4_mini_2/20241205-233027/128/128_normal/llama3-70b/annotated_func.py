#State of the program right berfore the function call: n is a positive integer representing the number of days in the shop's plan, f is a non-negative integer such that 0 <= f <= n, and for each day i (1 <= i <= n), k_i and l_i are non-negative integers representing the number of products available and the number of clients coming to the shop, respectively, with 0 <= k_i, l_i <= 10^9.
def func():
    n, f = map(int, input().split())
    days = []
    for _ in range(n):
        k, l = map(int, input().split())
        
        days.append((k, l))
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `f` is a non-negative integer such that 0 <= `f` <= `n`, `days` contains `n` tuples of input integers `(k, l)`.
    days.sort(key=lambda x: x[1] - x[0], reverse=True)
    sold = 0
    for i in range(n):
        if i < f:
            sold += min(days[i][0] * 2, days[i][1])
        else:
            sold += min(days[i][0], days[i][1])
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `f` is a non-negative integer such that 0 <= `f` <= `n`, `days` is sorted based on the difference between the second and first elements of each tuple `(k, l)` in descending order, and `sold` is equal to the sum of `min(days[i][0] * 2, days[i][1])` for `i` in the range `[0, f - 1]` and `min(days[i][0], days[i][1])` for `i` in the range `[f, n - 1]`.
    print(sold)
#Overall this is what the function does:The function accepts input values representing the number of days `n`, a non-negative integer `f`, and for each day, the number of available products `k` and the number of clients `l`. It calculates the total products sold over the `n` days, allowing double sales for the first `f` days and normal sales for the remaining days, then prints the total sold. The function does not handle any edge cases related to invalid input values (like negative `n` or `f` values) since it assumes valid inputs are provided.

