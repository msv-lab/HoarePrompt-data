#State of the program right berfore the function call: n is an integer representing the number of integers in the list, m is an integer representing the parameter determining when Sasha wins, nums is a list of n integers where each integer is between 1 and 10^9 inclusive.
def func_1(n, m, nums):
    tot = sum(len(val) for val in map(str, nums))
    cntvals = sorted((zerocnts(val) for val in nums), reverse=True)
    for i in range(0, len(cntvals), 2):
        tot -= cntvals[i]
        
    #State: `n` is an integer representing the number of integers in the list, `m` is an integer representing the parameter determining when Sasha wins, `nums` is a list of `n` integers where each integer is between 1 and 10^9 inclusive, `tot` is the sum of the number of digits in all integers in `nums` minus the sum of every second element in `cntvals` starting from the first, `cntvals` is a sorted list of the number of zeros in the binary representation of each integer in `nums` in descending order.
    return 'Sasha' if tot >= m + 1 else 'Anna'
    #The program returns 'Sasha' if the sum of the number of digits in all integers in `nums` minus the sum of every second element in `cntvals` starting from the first is greater than or equal to `m + 1`; otherwise, it returns 'Anna'.
#Overall this is what the function does:The function determines the winner of a game between Sasha and Anna based on the sum of the number of digits in a list of integers (`nums`), adjusted by subtracting the sum of every second element in a list of zero counts in the binary representations of those integers. The function returns 'Sasha' if the adjusted sum is greater than or equal to `m + 1`; otherwise, it returns 'Anna'.

#State of the program right berfore the function call: num is an integer greater than or equal to 0.
def zerocnts(num):
    num = str(num)
    tot = 0
    for i in range(len(num) - 1, -1, -1):
        if num[i] != '0':
            break
        
        tot += 1
        
    #State: `num` is a string representation of an integer greater than or equal to 0; `tot` is the count of trailing zeros in `num`.
    return tot
    #The program returns `tot`, which is the count of trailing zeros in the string representation of the integer `num`.
#Overall this is what the function does:The function accepts an integer `num` that is greater than or equal to 0 and returns the count of trailing zeros in its string representation.

