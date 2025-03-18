#State of the program right berfore the function call: n is a positive integer representing the number of integers in the list, m is a non-negative integer representing the parameter determining when Sasha wins, and nums is a list of n positive integers where 1 ≤ a_i ≤ 10^9.
def func_1(n, m, nums):
    tot = sum(len(val) for val in map(str, nums))
    cntvals = sorted((zerocnts(val) for val in nums), reverse=True)
    for i in range(0, len(cntvals), 2):
        tot -= cntvals[i]
        
    #State: `n` is a positive integer, `m` is a non-negative integer, `nums` is a list of `n` positive integers where \(1 \leq a_i \leq 10^9\), `tot` is the sum of the lengths of the string representations of the numbers in `nums` minus the sum of every second element starting from the first element of `cntvals`, `cntvals` is a list of the counts of zeros in each number in `nums`, sorted in descending order, and `i` is the last index processed by the loop, which is the largest even index less than or equal to the length of `cntvals` - 1.
    return 'Sasha' if tot >= m + 1 else 'Anna'
    #The program returns 'Sasha' if the sum of the lengths of the string representations of the numbers in `nums` minus the sum of every second element starting from the first element of `cntvals` (sorted in descending order) is greater than or equal to `m + 1`. Otherwise, it returns 'Anna'.
#Overall this is what the function does:The function `func_1` takes three parameters: `n` (a positive integer), `m` (a non-negative integer), and `nums` (a list of `n` positive integers). It calculates the sum of the lengths of the string representations of the numbers in `nums` and subtracts the sum of every second element starting from the first element of a sorted list of zero counts in each number in `nums` (in descending order). If the result is greater than or equal to `m + 1`, the function returns 'Sasha'; otherwise, it returns 'Anna'.

#State of the program right berfore the function call: num is an integer.
def zerocnts(num):
    num = str(num)
    tot = 0
    for i in range(len(num) - 1, -1, -1):
        if num[i] != '0':
            break
        
        tot += 1
        
    #State: `num` is a non-empty string, `tot` is the count of trailing zeros in `num`, `i` is the index of the first non-zero digit from the end of `num` or -1 if all digits are zero.
    return tot
    #The program returns the count of trailing zeros in the string `num`.
#Overall this is what the function does:The function `zerocnts` accepts an integer `num` and returns the count of trailing zeros in the string representation of `num`. After the function concludes, `num` remains unchanged, and the returned value represents the number of consecutive zeros at the end of the string representation of `num`. If `num` has no trailing zeros, the function returns 0.

