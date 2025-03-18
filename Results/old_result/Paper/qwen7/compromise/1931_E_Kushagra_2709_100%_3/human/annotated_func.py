#State of the program right berfore the function call: n is an integer representing the number of integers in the list, m is an integer representing the parameter determining when Sasha wins, and nums is a list of integers where each integer is between 1 and 10^9 inclusive.
def func_1(n, m, nums):
    tot = sum(len(val) for val in map(str, nums))
    cntvals = sorted((zerocnts(val) for val in nums), reverse=True)
    for i in range(0, len(cntvals), 2):
        tot -= cntvals[i]
        
    #State: Output State: `cntvals` is a list of the counts of zeros in each integer of `nums`, sorted in descending order but with every second element removed; `tot` is the sum of the lengths of the string representations of each integer in `nums` minus the values at even indices of `cntvals`; `n` is an integer representing the number of integers in the list, `m` is an integer representing the parameter determining when Sasha wins, and `nums` is a list of integers where each integer is between 1 and 10^9 inclusive.
    return 'Sasha' if tot >= m + 1 else 'Anna'
    #The program returns 'Sasha' if the sum of the lengths of the string representations of each integer in `nums` minus the values at even indices of `cntvals` is greater than or equal to `m + 1`, otherwise it returns 'Anna'.
#Overall this is what the function does:The function accepts three parameters: `n`, representing the number of integers in the list `nums`; `m`, determining when Sasha wins; and `nums`, a list of integers each between 1 and 10^9 inclusive. It calculates the sum of the lengths of the string representations of each integer in `nums` and subtracts the values at even indices of the sorted zero counts of each integer in `nums`. If this result is greater than or equal to `m + 1`, it returns 'Sasha', otherwise it returns 'Anna'.

#State of the program right berfore the function call: num is an integer such that 1 <= num <= 10^9.
def zerocnts(num):
    num = str(num)
    tot = 0
    for i in range(len(num) - 1, -1, -1):
        if num[i] != '0':
            break
        
        tot += 1
        
    #State: Output State: `num` is a string representation of an integer such that 1 <= num <= 10^9; `tot` is the number of trailing zeros in the string `num`.
    return tot
    #The program returns the number of trailing zeros in the string representation of the integer `num`, where 1 <= num <= 10^9.
#Overall this is what the function does:The function accepts an integer `num` (where 1 ≤ num ≤ 10^9) and returns the count of trailing zeros in its string representation.

