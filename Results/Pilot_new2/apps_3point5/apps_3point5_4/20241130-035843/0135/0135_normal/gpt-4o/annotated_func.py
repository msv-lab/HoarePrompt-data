#State of the program right berfore the function call: n and k are integers such that 1 <= n, k <= 10^18.**
def func_1(n, k):
    if (k >= n) :
        return 'No'
        #The program returns 'No'
    #State of the program after the if block has been executed: *n and k are integers such that 1 <= n, k <= 10^18. k is less than n
    seen_remainders = set()
    for i in range(1, k + 1):
        remainder = n % i
        
        if remainder in seen_remainders:
            return 'No'
        
        seen_remainders.add(remainder)
        
    #State of the program after the  for loop has been executed: n >= k, k < n, seen_remainders is a set containing all unique remainders of n modulo i for i in the range [1,k]. If any remainder is repeated, the program returns 'No'.
    return 'Yes'
    #The program returns 'Yes'
#Overall this is what the function does:The function `func_1` accepts two integer parameters `n` and `k`, where both `n` and `k` satisfy 1 <= n, k <= 10^18. The function checks if k is greater than or equal to n, in which case it returns 'No'. If k is less than n, the function iterates through the range [1, k] to calculate the remainder of n divided by i. If any remainder is repeated, the function returns 'No'. If no remainders are repeated, the function returns 'Yes'. The functionality covers the cases where k is equal to n, k is less than n, and also ensures that all unique remainders are accounted for.

