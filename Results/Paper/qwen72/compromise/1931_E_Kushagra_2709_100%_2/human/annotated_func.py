#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 2 · 10^5), m is a non-negative integer (0 ≤ m ≤ 2 · 10^6), and nums is a list of n positive integers (1 ≤ a_i ≤ 10^9).
def func_1(n, m, nums):
    tot = sum(len(val) for val in map(str, nums))
    cntvals = sorted((zerocnts(val) for val in nums), reverse=True)
    for i in range(0, len(cntvals), 2):
        tot -= cntvals[i]
        
    #State: `n` is a positive integer (1 ≤ n ≤ 2 · 10^5), `m` is a non-negative integer (0 ≤ m ≤ 2 · 10^6), `nums` is a list of n positive integers (1 ≤ a_i ≤ 10^9), `tot` is the total number of digits in the list `nums` minus the sum of counts of zeros in the elements at even indices of `cntvals`, `cntvals` is a list of the counts of zeros in each element of `nums`, sorted in descending order.
    return 'Sasha' if tot >= m + 1 else 'Anna'
    #The program returns 'Sasha' if the total number of digits in the list `nums` minus the sum of counts of zeros in the elements at even indices of `cntvals` is greater than or equal to `m + 1`. Otherwise, it returns 'Anna'.
#Overall this is what the function does:The function `func_1` takes three parameters: `n` (a positive integer), `m` (a non-negative integer), and `nums` (a list of `n` positive integers). It calculates the total number of digits in the list `nums` and subtracts the sum of counts of zeros in the elements at even indices of a sorted list of zero counts from each element of `nums`. The function returns 'Sasha' if the resulting value is greater than or equal to `m + 1`; otherwise, it returns 'Anna'.

#State of the program right berfore the function call: num is an integer.
def zerocnts(num):
    num = str(num)
    tot = 0
    for i in range(len(num) - 1, -1, -1):
        if num[i] != '0':
            break
        
        tot += 1
        
    #State: `tot` is the number of trailing zeros in the string `num`.
    return tot
    #The program returns the number of trailing zeros in the string `num`.
#Overall this is what the function does:The function `zerocnts` accepts an integer `num` and returns the number of trailing zeros in the string representation of `num`. After the function concludes, the input parameter `num` remains unchanged, and the function returns an integer representing the count of trailing zeros.

