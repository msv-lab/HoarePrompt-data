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
        
    #State of the program after the  for loop has been executed: ```plaintext
    #Output State:
    return total_value
    #The program returns total_value which is the sum of all elements that were originally present in the variable 'total'
#Overall this is what the function does:The function `func_1` accepts an integer `n` and a list `a` of `n` integers, where each integer in `a` satisfies \(1 \leq a_i \leq 5000\). It calculates and returns the sum of the maximum values of all possible non-empty subsets of `a`. This is achieved through a nested loop where the outer loop iterates over all possible bit masks (subsets) of the list `a`, and the inner loop determines the maximum value for each subset represented by the current bit mask. The result is accumulated in `total_value`, which is then returned modulo \(998244353\).

