#State of the program right berfore the function call: n is an integer such that 1 <= n <= 5000, and a is a list of n integers where each integer a_i satisfies 1 <= a_i <= 5000.
def func_1(n, a):
    MOD = 998244353
    total_value = 0
    for mask in range(1 << n):
        max_balls = 0
        
        for i in range(n):
            if mask & 1 << i != 0:
                max_balls = max(max_balls, a[i])
        
        total_value = (total_value + max_balls) % MOD
        
    #State of the program after the  for loop has been executed: `total_value` is the sum of the maximum values for each possible subset of the list `a`, modulo `998244353`; `n` is a non-negative integer within the range `1 <= n <= 5000`; `a` is a list of `n` integers where each integer `a_i` satisfies `1 <= a_i <= 5000`; `mask` is an integer ranging from `0` to `2^n - 1`.
    return total_value
    #The program returns total_value which is the sum of the maximum values for each possible subset of the list 'a', modulo 998244353
#Overall this is what the function does:- The function correctly handles the case where `n` is 1, as there is only one non-empty subset.
- The function correctly handles the case where all elements in `a` are the same.
- The function correctly handles the case where `a` contains duplicate values.
- The function does not handle the case where `n` is 0. Since the problem statement specifies that `1 ≤ n ≤ 5000`, this edge case is not relevant here. However, if the function were to be extended to include `n = 0`, it would need to return 0, as there are no non-empty subsets.

