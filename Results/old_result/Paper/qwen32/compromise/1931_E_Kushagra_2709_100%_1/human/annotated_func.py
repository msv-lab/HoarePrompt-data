#State of the program right berfore the function call: n is an integer representing the number of integers in the list, m is a non-negative integer representing the parameter determining when Sasha wins, and nums is a list of integers where each integer is between 1 and 10^9 inclusive.
def func_1(n, m, nums):
    tot = sum(len(val) for val in map(str, nums))
    cntvals = sorted((zerocnts(val) for val in nums), reverse=True)
    for i in range(0, len(cntvals), 2):
        tot -= cntvals[i]
        
    #State: n is an integer representing the number of integers in the list, m is a non-negative integer representing the parameter determining when Sasha wins, nums is a list of integers where each integer is between 1 and \(10^9\) inclusive, tot is the sum of the number of digits in all integers in nums minus the sum of the number of trailing zeros of every second element in cntvals, cntvals is a sorted list (in descending order) of values returned by zerocnts for each value in nums.
    return 'Sasha' if tot >= m + 1 else 'Anna'
    #The program returns 'Sasha' if `tot` is greater than or equal to `m + 1`, otherwise it returns 'Anna'.
#Overall this is what the function does:The function determines the winner of a game between Sasha and Anna based on the total sum of the number of digits in a list of integers, adjusted by the number of trailing zeros of every second element when sorted in descending order. It returns 'Sasha' if this adjusted sum is greater than or equal to `m + 1`, otherwise it returns 'Anna'.

#State of the program right berfore the function call: num is an integer such that 1 <= num <= 10^9.
def zerocnts(num):
    num = str(num)
    tot = 0
    for i in range(len(num) - 1, -1, -1):
        if num[i] != '0':
            break
        
        tot += 1
        
    #State: `num` is a string representation of the original integer such that 1 <= int(num) <= 10^9; `tot` is the number of trailing zeros in `num`.
    return tot
    #The program returns the number of trailing zeros in the string representation of the integer `num`
#Overall this is what the function does:The function accepts an integer `num` within the range of 1 to 1,000,000,000 and returns the count of trailing zeros in its string representation.

