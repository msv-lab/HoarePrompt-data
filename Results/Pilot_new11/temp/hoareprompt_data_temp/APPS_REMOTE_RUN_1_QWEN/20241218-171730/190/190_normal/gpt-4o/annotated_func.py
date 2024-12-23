#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 1000, and a is a list of n integers where each integer a_i satisfies 1 ≤ a_i ≤ 100.
def func():
    n = int(input())
    a = list(map(int, input().split()))
    min_cost = float('inf')
    best_t = -1
    for t in range(1, 101):
        current_cost = 0
        
        for length in a:
            if length < t - 1:
                current_cost += t - 1 - length
            elif length > t + 1:
                current_cost += length - (t + 1)
        
        if current_cost < min_cost:
            min_cost = current_cost
            best_t = t
        
    #State of the program after the  for loop has been executed: `a` is a non-empty list of integers, `min_cost` is the minimum cumulative cost calculated during the loop execution based on the conditions given, `best_t` is the value of `t` when `min_cost` is updated, `t` is 101, and `current_cost` is the cumulative cost calculated during the loop execution based on the conditions given for each element in `a`. If `current_cost` is less than `min_cost`, `min_cost` is updated to `current_cost` and `best_t` is updated to the corresponding value of `t`. Otherwise, `min_cost` and `best_t` retain their final updated values, and `current_cost` retains its final value.
    print(best_t, min_cost)
#Overall this is what the function does:The function accepts an integer \(n\) such that \(1 \leq n \leq 1000\) and a list \(a\) of \(n\) integers where each integer \(a_i\) satisfies \(1 \leq a_i \leq 100\). It then iterates over all possible values of \(t\) from 1 to 100 to find the value of \(t\) that minimizes the cumulative cost defined as follows: for each element \(length\) in the list \(a\), if \(length < t - 1\), the cost contribution is \(t - 1 - length\); if \(length > t + 1\), the cost contribution is \(length - (t + 1)\). The function prints the value of \(t\) that minimizes the cumulative cost and the minimum cumulative cost itself.

