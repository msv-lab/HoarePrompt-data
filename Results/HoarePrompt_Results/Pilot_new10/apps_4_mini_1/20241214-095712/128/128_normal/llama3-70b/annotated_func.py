#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 10^5) representing the number of days, f is a non-negative integer (0 ≤ f ≤ n) representing the number of days chosen for sell-out, and for each of the n days, k_i and l_i are non-negative integers (0 ≤ k_i, l_i ≤ 10^9) representing the number of products available and the number of clients on day i respectively.
def func():
    n, f = map(int, input().split())
    days = []
    for _ in range(n):
        k, l = map(int, input().split())
        
        days.append((k, l))
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `f` is a non-negative integer, `days` is a list containing `n` tuples of integers `(k, l)` received as input, `_` is `n - 1`, each `k` is an input integer, each `l` is an input integer.
    days.sort(key=lambda x: x[1] - x[0], reverse=True)
    sold = 0
    for i in range(n):
        if i < f:
            sold += min(days[i][0] * 2, days[i][1])
        else:
            sold += min(days[i][0], days[i][1])
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `f` is a non-negative integer, `days` is sorted in descending order, `_` is `n - 1`, and `sold` is equal to the sum of the minimums based on the logic defined in the loop: for each `i` from 0 to `n-1`, if `i < f`, `sold` increments by `min(days[i][0] * 2, days[i][1])`; otherwise, it increments by `min(days[i][0], days[i][1])`.
    print(sold)
#Overall this is what the function does:The function accepts input representing the number of days (`n`) and the number of days chosen for sell-out (`f`), as well as the number of products available (`k_i`) and the number of clients (`l_i`) for each day. It then calculates and prints the total number of products sold based on these inputs. For the first `f` days, it allows doubling the available products when calculating the sold amount, while for the remaining days, it uses the actual available products. It assumes valid input will be provided as specified, but it does not ensure any edge case handling for improper input values.

