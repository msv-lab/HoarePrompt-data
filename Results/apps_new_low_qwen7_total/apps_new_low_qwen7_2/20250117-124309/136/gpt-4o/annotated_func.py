#State of the program right berfore the function call: n and k are non-negative integers such that 1 ≤ n, k ≤ 10^18.
def func_1(n, k):
    if (k >= n) :
        return 'No'
        #The program returns 'No'
    #State of the program after the if block has been executed: n and k are non-negative integers such that 1 ≤ n, k ≤ 10^18, and k is less than n
    seen_remainders = set()
    for i in range(1, k + 1):
        remainder = n % i
        
        if remainder in seen_remainders:
            return 'No'
        
        seen_remainders.add(remainder)
        
    #State of the program after the  for loop has been executed: `i` is `k + 1`, `k` is a valid non-negative integer such that \(1 \leq k < n\), `remainder` is irrelevant, `seen_remainders` is a set containing unique remainders from `n % 1` to `n % k` and the function returns 'Yes'.
    return 'Yes'
    #The program returns 'Yes'
#Overall this is what the function does:The function `func_1` accepts two non-negative integers `n` and `k` as parameters, where both `n` and `k` are constrained such that \(1 \leq n, k \leq 10^{18}\). It checks whether the remainders of `n` divided by each integer from 1 to `k` are unique. If any remainder repeats, the function returns 'No'. If all remainders are unique, the function returns 'Yes'.

