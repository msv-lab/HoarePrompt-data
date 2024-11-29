#State of the program right berfore the function call: n and k are integers such that 1 ≤ n, k ≤ 10^18.
def func_1(n, k):
    if (k >= n) :
        return 'No'
        #The program returns 'No' since k is greater than or equal to n
    #State of the program after the if block has been executed: *`n` and `k` are integers such that 1 ≤ `n`, `k` ≤ 10^18, and `k` is less than `n`.
    seen_remainders = set()
    for i in range(1, k + 1):
        remainder = n % i
        
        if remainder in seen_remainders:
            return 'No'
        
        seen_remainders.add(remainder)
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 ≤ `n` ≤ 10^18, `k` is an integer such that 1 ≤ `k` < `n`, `seen_remainders` is a set containing the remainders of `n` divided by each integer from 1 to `k`, and the loop executes `k` times.
    return 'Yes'
    #The program returns 'Yes'
#Overall this is what the function does:The function accepts two integer parameters `n` and `k`. It first checks if `k` is greater than or equal to `n`, in which case it returns 'No'. Then, it computes the remainder of `n` when divided by each integer from 1 to `k`. If any remainder is repeated during these calculations, it returns 'No'. If all remainders are unique, it concludes by returning 'Yes'. Thus, it effectively checks whether the remainders of `n` divided by integers from 1 to `k` are all distinct, returning 'Yes' only if they are.

