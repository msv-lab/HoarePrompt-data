#State of the program right berfore the function call: n and m are non-negative integers such that 1 <= n <= 2 * 10^5 and 0 <= m <= 2 * 10^6, and nums is a list of n integers where 1 <= nums[i] <= 10^9.
def func_1(n, m, nums):
    tot = sum(len(val) for val in map(str, nums))
    cntvals = sorted((zerocnts(val) for val in nums), reverse=True)
    for i in range(0, len(cntvals), 2):
        tot -= cntvals[i]
        
    #State: `n` and `m` remain unchanged, `nums` remains unchanged, `tot` is reduced by the sum of the counts of zeros in the integers of `nums` at even indices, `cntvals` remains unchanged.
    return 'Sasha' if tot >= m + 1 else 'Anna'
    #The program returns 'Sasha' if the value of `tot` (after being reduced by the sum of the counts of zeros in the integers of `nums` at even indices) is greater than or equal to `m + 1`; otherwise, the program returns 'Anna'.
#Overall this is what the function does:The function `func_1` accepts three parameters: `n` (a non-negative integer), `m` (a non-negative integer), and `nums` (a list of `n` integers). It calculates the total number of digits in the integers of `nums` and then subtracts the sum of the counts of zeros in the integers at even indices of `cntvals` (a sorted list of zero counts in `nums`). The function returns 'Sasha' if the adjusted total is greater than or equal to `m + 1`; otherwise, it returns 'Anna'. The parameters `n`, `m`, and `nums` remain unchanged after the function execution.

#State of the program right berfore the function call: num is an integer such that 1 <= num <= 10^9.
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
#Overall this is what the function does:The function `zerocnts` accepts an integer `num` within the range 1 to 1,000,000,000 (inclusive) and returns the number of trailing zeros in the string representation of `num`. After the function concludes, the input variable `num` remains unchanged, and the function returns an integer representing the count of trailing zeros.

