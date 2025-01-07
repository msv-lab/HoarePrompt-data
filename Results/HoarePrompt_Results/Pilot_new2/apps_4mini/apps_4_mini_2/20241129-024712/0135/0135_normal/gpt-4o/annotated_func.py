#State of the program right berfore the function call: n and k are integers such that 1 ≤ n, k ≤ 10^18.
def func_1(n, k):
    if (k >= n) :
        return 'No'
        #The program returns 'No' because the current value of k is greater than or equal to n, where n and k are integers such that 1 ≤ n, k ≤ 10^18.
    #State of the program after the if block has been executed: *`n` and `k` are integers such that 1 ≤ `n`, `k` ≤ 10^18, and `k` is less than `n`.
    seen_remainders = set()
    for i in range(1, k + 1):
        remainder = n % i
        
        if remainder in seen_remainders:
            return 'No'
        
        seen_remainders.add(remainder)
        
    #State of the program after the  for loop has been executed: `n` and `k` are integers within the range specified, `seen_remainders` now contains all unique remainders obtained from `n % i` for `i` in the range 1 to `k`, and the loop executed `k` times.
    return 'Yes'
    #The program returns 'Yes' indicating a positive condition met, likely based on the unique remainders obtained from `n % i` for `i` in the range 1 to `k`.
#Overall this is what the function does:The function accepts two integers `n` and `k` (where 1 ≤ n, k ≤ 10^18) and returns 'No' if `k` is greater than or equal to `n`, or if any remainder obtained from `n % i` (for `i` ranging from 1 to `k`) has already been seen. It returns 'Yes' if all remainders are unique across that range.

