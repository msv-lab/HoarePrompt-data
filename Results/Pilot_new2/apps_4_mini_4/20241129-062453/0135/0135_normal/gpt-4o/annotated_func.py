#State of the program right berfore the function call: n and k are integers such that 1 ≤ n, k ≤ 10^18.
def func_1(n, k):
    if (k >= n) :
        return 'No'
        #The program returns 'No' as the output based on the statement provided.
    #State of the program after the if block has been executed: *n and k are integers such that 1 ≤ n, k ≤ 10^18, and k is less than n.
    seen_remainders = set()
    for i in range(1, k + 1):
        remainder = n % i
        
        if remainder in seen_remainders:
            return 'No'
        
        seen_remainders.add(remainder)
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 ≤ `n` ≤ 10^18, `k` is an integer such that 1 ≤ `k` ≤ 10^18 and `k` < `n`, `seen_remainders` contains all unique remainders from `n % 1` to `n % k`, `i` is `k`, and `remainder` is `n % k`
    return 'Yes'
    #The program returns 'Yes', indicating a positive outcome based on the given conditions.
#Overall this is what the function does:The function accepts two integers `n` and `k`, checks if `k` is greater than or equal to `n`, returning 'No' if it is. It then calculates the unique remainders of `n` divided by each integer from 1 to `k`, returning 'No' if any remainder is duplicated, and 'Yes' if all remainders are unique.

