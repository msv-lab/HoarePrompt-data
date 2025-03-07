#State of the program right berfore the function call: n is a positive integer, m is a non-negative integer, and nums is a list of positive integers such that 1 <= n <= 2 * 10^5, 0 <= m <= 2 * 10^6, and 1 <= nums[i] <= 10^9 for all 0 <= i < n.
def func_1(n, m, nums):
    tot = sum(len(val) for val in map(str, nums))
    cntvals = sorted((zerocnts(val) for val in nums), reverse=True)
    for i in range(0, len(cntvals), 2):
        tot -= cntvals[i]
        
    #State: `n` is a positive integer, `m` is a non-negative integer, `nums` is a list of positive integers, `tot` is the sum of the lengths of the string representations of the elements in `nums` minus the sum of every second element in `cntvals` starting from index 0, `cntvals` is a list of the zero counts of each element in `nums`, sorted in descending order, and `i` is the largest even index less than the length of `cntvals`.
    return 'Sasha' if tot >= m + 1 else 'Anna'
    #The program returns 'Sasha' if the value of `tot` is greater than or equal to `m + 1`, otherwise it returns 'Anna'. Here, `tot` is calculated as the sum of the lengths of the string representations of the elements in `nums` minus the sum of every second element in `cntvals` starting from index 0. `m` is a non-negative integer, and `cntvals` is a list of the zero counts of each element in `nums`, sorted in descending order.
#Overall this is what the function does:The function `func_1` takes three parameters: `n` (a positive integer), `m` (a non-negative integer), and `nums` (a list of positive integers). It calculates the total length of the string representations of the numbers in `nums` and subtracts the sum of every second element in a sorted list of zero counts of each number in `nums`. The function returns 'Sasha' if the resulting total is greater than or equal to `m + 1`; otherwise, it returns 'Anna'. The parameters `n`, `m`, and `nums` remain unchanged after the function call.

#State of the program right berfore the function call: num is an integer.
def zerocnts(num):
    num = str(num)
    tot = 0
    for i in range(len(num) - 1, -1, -1):
        if num[i] != '0':
            break
        
        tot += 1
        
    #State: `num` remains as the string representation of the original integer value of `num`. The variable `i` is the index of the first non-zero digit from the right (or -1 if all digits are zero). The variable `tot` is the count of trailing zeros in `num`.
    return tot
    #The program returns the count of trailing zeros in the string representation of `num`.
#Overall this is what the function does:The function `zerocnts` accepts an integer `num` and returns the count of trailing zeros in the string representation of `num`. After the function concludes, the input `num` remains unchanged, and the returned value is the number of consecutive zeros at the end of the string representation of `num`. If `num` has no trailing zeros, the function returns 0.

