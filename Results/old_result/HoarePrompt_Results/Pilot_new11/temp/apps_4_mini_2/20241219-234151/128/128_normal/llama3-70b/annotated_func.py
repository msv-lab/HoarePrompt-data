#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 100000, f is an integer such that 0 ≤ f ≤ n, and each of the k_i and l_i values (for i from 1 to n) are integers such that 0 ≤ k_i, l_i ≤ 10^9.
def func():
    n, f = map(int, input().split())
    days = []
    for _ in range(n):
        k, l = map(int, input().split())
        
        days.append((k, l))
        
    #State of the program after the  for loop has been executed: `days` is a list containing `n` tuples of input integers (k, l) where `k` and `l` are input integers; `n` is an integer such that 1 ≤ n ≤ 100000.
    days.sort(key=lambda x: x[1] - x[0], reverse=True)
    sold = 0
    for i in range(n):
        if i < f:
            sold += min(days[i][0] * 2, days[i][1])
        else:
            sold += min(days[i][0], days[i][1])
        
    #State of the program after the  for loop has been executed: `days` is a list of `n` tuples sorted by the difference `l - k`, `sold` is equal to the total calculated based on the given conditions for all `n` elements in the list. If `f` is less than `n`, the first `f` tuples will contribute double their first element to `sold` if `days[i][0] * 2` is less than `days[i][1]`, otherwise the second element will contribute; for the remaining tuples, `sold` will contribute their first element unless `days[i][1]` is less. If `n` is 0, `sold` will remain 0.
    print(sold)
#Overall this is what the function does:The function reads two integers, `n` (the number of days) and `f` (a threshold for special processing), along with `n` pairs of integers `(k, l)`, where each pair corresponds to the production and limit values for each day. It processes these inputs to compute a total amount sold based on specific rules: for the first `f` days, it considers double the production value if it does not exceed the limit; otherwise, it uses the limit. For days beyond `f`, it simply takes the production value unless the limit is less. After sorting the days based on the difference between `l` and `k`, the function accumulates the total sold value and prints it out. Notably, if `n` is 0 (though not allowed by input constraints), the result would be 0. Additionally, there is no validation for input limits or erroneous input handling, meaning invalid inputs could cause unexpected behavior.

