#State of the program right berfore the function call: ** n and k are integers such that 1 ≤ n, k ≤ 10^18.
def func_1(n, k):
    if (k >= n) :
        return 'No'
        #The program returns the string 'No'
    #State of the program after the if block has been executed: *n and k are integers such that 1 ≤ n, k ≤ 10^18. k is strictly less than n.
    seen_remainders = set()
    for i in range(1, k + 1):
        remainder = n % i
        
        if remainder in seen_remainders:
            return 'No'
        
        seen_remainders.add(remainder)
        
    #State of the program after the  for loop has been executed: n and k are integers such that 1 ≤ n, k ≤ 10^18, k is strictly less than n, seen_remainders is a set containing all remainders from n % i where i ranges from 1 to k (inclusive)
    return 'Yes'
    #The program returns 'Yes'
#Overall this is what the function does:The function `func_1` accepts two integer parameters `n` and `k`, with 1 ≤ n, k ≤ 10^18. It then checks the relationship between n and k. If k is greater than or equal to n, it returns 'No'. If the remainder of dividing n by i, where i ranges from 1 to k, has been seen before, it returns 'No'. If none of the conditions are met, it returns 'Yes'.

