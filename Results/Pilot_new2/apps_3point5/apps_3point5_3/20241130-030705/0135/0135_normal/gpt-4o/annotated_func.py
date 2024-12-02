#State of the program right berfore the function call: n and k are integers such that 1 <= n, k <= 10^18.
def func_1(n, k):
    if (k >= n) :
        return 'No'
        #The program returns the string 'No'
    #State of the program after the if block has been executed: *n and k are integers such that 1 <= n, k <= 10^18. k is less than n.
    seen_remainders = set()
    for i in range(1, k + 1):
        remainder = n % i
        
        if remainder in seen_remainders:
            return 'No'
        
        seen_remainders.add(remainder)
        
    #State of the program after the  for loop has been executed: `n` and `k` are integers such that 1 <= n, k <= 10^18, `k` is less than `n`, `seen_remainders` is a set containing the remainder of dividing `n` by each `i` from 1 to `k`, and `remainder` is the remainder of dividing `n` by `k`. If any remainder from 1 to `k` is repeated, the loop returns 'No'. Otherwise, all unique remainders are stored in `seen_remainders`.
    return 'Yes'
    #The program returns 'Yes' if all unique remainders of dividing 'n' by each 'i' from 1 to 'k' are stored in 'seen_remainders' without any repetitions. Otherwise, it returns 'No'
#Overall this is what the function does:The function `func_1` accepts two integer parameters `n` and `k`, where both `n` and `k` are integers satisfying the constraint 1 <= n, k <= 10^18. The function calculates the remainder of dividing `n` by each integer from 1 to `k` and checks if there are any repeated remainders. If there are repeated remainders, it returns 'No'. If all unique remainders are stored in `seen_remainders` without repetitions, it returns 'Yes'. The function covers the cases where the program returns 'No' for multiple potential cases as annotated, and returns 'Yes' if the condition for unique remainders is met.

