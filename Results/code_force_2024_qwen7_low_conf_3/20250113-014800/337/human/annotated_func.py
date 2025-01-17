#State of the program right berfore the function call: n is an integer such that 1 <= n <= 5000, and a is a list of n integers where 1 <= a_i <= 5000 for each i, and the sum of all elements in a does not exceed 5000.
def func_1(n, a):
    MOD = 998244353
    total_value = 0
    for mask in range(1 << n):
        max_balls = 0
        
        for i in range(n):
            if mask & 1 << i != 0:
                max_balls = max(max_balls, a[i])
        
        total_value = (total_value + max_balls) % MOD
        
    #State of the program after the  for loop has been executed: `total_value` is the sum of the maximum values for each possible subset of the list `a`, modulo `998244353`, `max_balls` is the maximum value found in the array `a` for indices where the corresponding bit in `mask` is set to 1, and `i` is `n`.
    return total_value
    #The program returns total_value which is the sum of the maximum values for each possible subset of the list 'a', modulo 998244353
#Overall this is what the function does:The function `func_1` accepts two parameters: `n`, an integer such that 1 ≤ n ≤ 5000, and `a`, a list of `n` integers where 1 ≤ a_i ≤ 5000 for each i, and the sum of all elements in `a` does not exceed 5000. It iterates over all possible subsets of the list `a` using bit masking. For each subset, it finds the maximum value among the elements whose corresponding bit in the subset's bitmask is set to 1. It then sums these maximum values and returns the result modulo 998244353. The function handles all possible subsets of the list `a`, including the empty subset, which contributes a value of 0 to the sum. There are no missing functionalities in the given code, and the postcondition accurately reflects the state of the program after the function executes.

