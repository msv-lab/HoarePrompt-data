#State of the program right berfore the function call: n is an integer representing the number of integers in the list, m is an integer representing the parameter determining when Sasha wins, and nums is a list of integers where each integer is between 1 and 10^9 inclusive.
def func_1(n, m, nums):
    tot = sum(len(val) for val in map(str, nums))
    cntvals = sorted((zerocnts(val) for val in nums), reverse=True)
    for i in range(0, len(cntvals), 2):
        tot -= cntvals[i]
        
    #State: Output State: `cntvals` is a list of the sorted counts of zeros in each integer of `nums`, excluding every second count in descending order; `tot` is the sum of the lengths of the string representations of each integer in `nums` minus the counts at even indices; `n` is an integer representing the number of integers in the list; `m` is an integer representing the parameter determining when Sasha wins; `nums` is a list of integers where each integer is between 1 and 10^9 inclusive.
    return 'Sasha' if tot >= m + 1 else 'Anna'
    #The program returns 'Sasha' if the sum of the lengths of the string representations of each integer in `nums` minus the counts at even indices is greater than or equal to `m + 1`, otherwise it returns 'Anna'.
#Overall this is what the function does:The function accepts three parameters: `n`, representing the number of integers in the list `nums`; `m`, representing the threshold for Sasha to win; and `nums`, a list of integers between 1 and 10^9. It calculates the sum of the lengths of the string representations of each integer in `nums`, subtracting the counts of zeros at even indices. If this result is greater than or equal to `m + 1`, it returns 'Sasha', otherwise it returns 'Anna'.

#State of the program right berfore the function call: num is an integer in the range 1 ≤ num ≤ 10^9.
def zerocnts(num):
    num = str(num)
    tot = 0
    for i in range(len(num) - 1, -1, -1):
        if num[i] != '0':
            break
        
        tot += 1
        
    #State: Output State: `num` is a string representation of an integer in the range 1 ≤ num ≤ 10^9; `tot` is the number of trailing zeros in the string representation of `num`.
    return tot
    #The program returns the number of trailing zeros in the string representation of `num`
#Overall this is what the function does:The function accepts an integer `num` in the range 1 ≤ num ≤ 10^9, converts it to a string, and counts the number of trailing zeros. It then returns this count.

