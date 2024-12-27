#State of the program right berfore the function call: n and f are non-negative integers such that 0 ≤ f ≤ n, and there are n pairs of non-negative integers (k, l) where 0 ≤ k, l ≤ 10^9, representing the number of products and clients for each day.
def func():
    n, f = map(int, input().split())
    days = []
    for _ in range(n):
        k, l = map(int, input().split())
        
        days.append((k, l))
        
    #State of the program after the  for loop has been executed: `n` is a non-negative integer, `f` is a non-negative integer where `0 ≤ f ≤ n`, `days` is a list containing `n` tuples of non-negative integer pairs `(k, l)` where `0 ≤ k, l ≤ 10^9`, or an empty list if `n` is 0.
    days.sort(key=lambda x: x[1] - x[0], reverse=True)
    sold = 0
    for i in range(n):
        if i < f:
            sold += min(days[i][0] * 2, days[i][1])
        else:
            sold += min(days[i][0], days[i][1])
        
    #State of the program after the  for loop has been executed: `n` is a non-negative integer, `f` is a non-negative integer where `0 ≤ f ≤ n`, `days` is a list containing `n` tuples of non-negative integer pairs `(k, l)` where `0 ≤ k, l ≤ 10^9`, sorted in descending order by `l - k`, and `sold` is the sum of `min(days[i][0] * 2, days[i][1])` for `i < f` and `min(days[i][0], days[i][1])` for `i ≥ f` for all `i` in the range of `n`, or 0 if `n` is 0.
    print(sold)
#Overall this is what the function does:The function calculates and prints the maximum number of products that can be sold over a period of `n` days, where each day has a certain number of products and clients. It operates on `n` non-negative integer pairs `(k, l)`, representing products and clients for each day, and two non-negative integers `n` and `f`, where `0 ≤ f ≤ n`. The function sorts the days based on the difference between the number of clients and products in descending order, then calculates the total sales by selling either `min(2 * products, clients)` products for the first `f` days or `min(products, clients)` products for the remaining days. The function does not handle cases where the input values are not valid integers or are outside the specified ranges, and it does not return any value, instead printing the total sales directly. The function will terminate and print the calculated total sales, leaving the input variables `n`, `f`, and the list of day pairs in their final state.

