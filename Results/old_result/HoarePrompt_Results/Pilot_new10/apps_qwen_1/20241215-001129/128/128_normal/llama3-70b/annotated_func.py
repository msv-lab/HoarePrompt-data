#State of the program right berfore the function call: n and f are integers such that 1 ≤ n ≤ 10^5 and 0 ≤ f ≤ n. Each of the following n lines contains two integers k_{i} and l_{i} such that 0 ≤ k_{i}, l_{i} ≤ 10^9, representing the number of products to be put up for sale and the number of clients coming to the shop on the i-th day, respectively.
def func():
    n, f = map(int, input().split())
    days = []
    for _ in range(n):
        k, l = map(int, input().split())
        
        days.append((k, l))
        
    #State of the program after the  for loop has been executed: `i` is `n`, `n` is an integer such that \(1 \leq n \leq 10^5\), `f` is an integer such that \(0 \leq f \leq n\), `days` is a list containing `n` tuples \([(k_1, l_1), (k_2, l_2), \ldots, (k_n, l_n)]\), where each \((k_i, l_i)\) is a tuple of integers entered by the user.
    days.sort(key=lambda x: x[1] - x[0], reverse=True)
    sold = 0
    for i in range(n):
        if i < f:
            sold += min(days[i][0] * 2, days[i][1])
        else:
            sold += min(days[i][0], days[i][1])
        
    #State of the program after the  for loop has been executed: `i` is `n`, `f` is a float or integer, `sold` is the sum of the minimum values between `days[i][0] * 2` and `days[i][1]` for `i < f`, and the minimum value between `days[i][0]` and `days[i][1]` for `i >= f`.
    print(sold)
#Overall this is what the function does:The function reads the number of days `n` and the value of `f` from input, followed by `n` pairs of integers `(k_i, l_i)` representing the number of products to be put up for sale and the number of clients coming to the shop on the `i`-th day. It sorts these pairs based on the difference `l_i - k_i` in descending order. It then calculates the total number of products sold, where for the first `f` days, each product can be sold twice if there are more products than clients, and for the remaining days, each product can only be sold once. The function outputs the total number of products sold.

