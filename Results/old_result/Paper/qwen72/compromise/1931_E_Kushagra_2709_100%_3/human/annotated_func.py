#State of the program right berfore the function call: n is a positive integer, m is a non-negative integer, and nums is a list of positive integers such that 1 <= n <= 2 * 10^5, 0 <= m <= 2 * 10^6, and 1 <= a_i <= 10^9 for all a_i in nums.
def func_1(n, m, nums):
    tot = sum(len(val) for val in map(str, nums))
    cntvals = sorted((zerocnts(val) for val in nums), reverse=True)
    for i in range(0, len(cntvals), 2):
        tot -= cntvals[i]
        
    #State: `n` remains a positive integer, `m` remains a non-negative integer, `nums` remains a list of positive integers with the same constraints, `tot` is reduced by the sum of the elements in `cntvals` at even indices, and `cntvals` remains the same sorted list of results of `zerocnts(val)` for each `val` in `nums`.
    return 'Sasha' if tot >= m + 1 else 'Anna'
    #The program returns 'Sasha' if the value of `tot` is greater than or equal to `m + 1`, otherwise it returns 'Anna'. Here, `tot` is the original value of `tot` reduced by the sum of the elements in `cntvals` at even indices, and `m` is a non-negative integer.
#Overall this is what the function does:The function `func_1` accepts a positive integer `n`, a non-negative integer `m`, and a list of positive integers `nums`. It calculates the total number of digits in the elements of `nums` and then subtracts the sum of the counts of zeros in the elements of `nums` at even indices (after sorting these counts in descending order). The function returns 'Sasha' if the adjusted total is greater than or equal to `m + 1`, otherwise it returns 'Anna'. The parameters `n`, `m`, and `nums` remain unchanged after the function call.

#State of the program right berfore the function call: num is an integer.
def zerocnts(num):
    num = str(num)
    tot = 0
    for i in range(len(num) - 1, -1, -1):
        if num[i] != '0':
            break
        
        tot += 1
        
    #State: Output State: `num` remains the same string representation of the original integer `num`, `tot` is the number of trailing zeros in `num`.
    return tot
    #The program returns the number of trailing zeros in the string representation of the original integer `num`.
#Overall this is what the function does:The function `zerocnts` accepts an integer `num` and returns the number of trailing zeros in its string representation. The input integer `num` remains unchanged.

