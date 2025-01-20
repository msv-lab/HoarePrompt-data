#State of the program right berfore the function call: n and k are non-negative integers such that 1 ≤ n, k ≤ 10^18.
def func_1(n, k):
    if (k >= n) :
        return 'No'
        #The program returns 'No'
    #State of the program after the if block has been executed: `n` and `k` are non-negative integers such that 1 ≤ n, k ≤ 10^18, and k is less than n
    seen_remainders = set()
    for i in range(1, k + 1):
        remainder = n % i
        
        if remainder in seen_remainders:
            return 'No'
        
        seen_remainders.add(remainder)
        
    #State of the program after the  for loop has been executed: `i` is `k`, `k` remains unchanged, `seen_remainders` is a set containing remainders of `n % i` for all `i` in the range from 1 to `k`, and the function returns 'No' if any of these remainders are found in `seen_remainders` at any point during the loop.
    return 'Yes'
    #The program returns 'Yes'
#Overall this is what the function does:The function `func_1` accepts two non-negative integer parameters `n` and `k` (both within the range 1 to \(10^{18}\)). It checks whether for all integers `i` in the range from 1 to `k`, the remainder of `n` divided by `i` is unique. If any remainder is repeated before the loop completes, the function returns 'No'. Otherwise, if all remainders are unique, the function returns 'Yes'.

