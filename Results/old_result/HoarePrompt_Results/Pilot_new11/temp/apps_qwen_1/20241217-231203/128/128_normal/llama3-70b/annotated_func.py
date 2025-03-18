#State of the program right berfore the function call: n and f are integers such that 1 ≤ n ≤ 10^5 and 0 ≤ f ≤ n. For each i in range(n), k_i and l_i are integers such that 0 ≤ k_i, l_i ≤ 10^9.
def func():
    n, f = map(int, input().split())
    days = []
    for _ in range(n):
        k, l = map(int, input().split())
        
        days.append((k, l))
        
    #State of the program after the  for loop has been executed: `days` is a list of tuples, each tuple contains two integers (`k_i`, `l_i`) for `i` in range `n`, `n` is an integer such that `0 ≤ n ≤ 10^5`, `f` is an integer such that `0 ≤ f ≤ n`, and remains unchanged.
    days.sort(key=lambda x: x[1] - x[0], reverse=True)
    sold = 0
    for i in range(n):
        if i < f:
            sold += min(days[i][0] * 2, days[i][1])
        else:
            sold += min(days[i][0], days[i][1])
        
    #State of the program after the  for loop has been executed: `days` is a list of tuples sorted in descending order based on the difference between the second element and the first element of each tuple, `f` is an integer such that \(0 \leq f \leq n\), `sold` is the sum of `sold + min(days[i][0] * 2, days[i][1])` if `i < f`, otherwise `sold + min(days[i][0], days[i][1])` for all valid `i` in the range `0` to `n-1`, `i` is `n`, and `n` is a non-negative integer.
    print(sold)
#Overall this is what the function does:The function processes input data consisting of `n` pairs of integers `(k_i, l_i)` where `n` and `f` are also integers such that `1 ≤ n ≤ 10^5` and `0 ≤ f ≤ n`. It sorts these pairs in descending order based on the difference between the second and first elements of each pair. Then, it calculates the total amount `sold` by considering the first `f` pairs differently (each item's contribution is doubled) and the remaining pairs normally. Finally, it prints the total amount `sold`. The function handles the edge case where `f` might be `0` or `n`, meaning only the first `f` pairs are doubled or none of them are, respectively. If `n` is `0`, it means there are no pairs to process, and the function will still execute the sorting and calculation steps, though `days` would be an empty list.

