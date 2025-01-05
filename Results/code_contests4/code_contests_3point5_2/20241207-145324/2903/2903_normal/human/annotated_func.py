#State of the program right berfore the function call: w and l are integers such that 1 ≤ l < w ≤ 10^5. The list of stones a_1, a_2, ..., a_{w-1} contains integers where 0 ≤ a_i ≤ 10^4.**
def func():
    n, k, s, mn = map(int, raw_input().split() + [0, 10000000000])
    a = list(map(int, raw_input().split()))
    for i in range(0, n - 1):
        if i < k:
            s += a[i]
        else:
            mn = min(mn, s)
            s += a[i] - a[i - k]
        
    #State of the program after the  for loop has been executed: `w` and `l` are integers such that 1 ≤ l < w ≤ 10^5, `a_1, a_2, ..., a_{w-1}` contains integers where 0 ≤ a_i ≤ 10^4, `n` is greater than 1. `s` has been updated based on the conditions in the loop. `mn` has been updated to the minimum value between its current value and the sum of elements in `a` from index 0 to `n-1`.
    print(min(mn, s))
#Overall this is what the function does:The function `func` reads input values for `n`, `k`, `s`, and `mn`, along with a list of integers `a`. It then iterates through the list `a`, updating the values of `s` and `mn` based on certain conditions. Finally, it prints the minimum value between `mn` and `s`. The functionality of the function is to determine the minimum value between the sum of elements in `a` and the calculated `s` value after iterating through the list.

