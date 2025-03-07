#State of the program right berfore the function call: n is an integer representing the number of integers in the list, m is an integer determining when Sasha wins, and nums is a list of integers where each integer is between 1 and 10^9 inclusive.
def func_1(n, m, nums):
    tot = sum(len(val) for val in map(str, nums))
    cntvals = sorted((zerocnts(val) for val in nums), reverse=True)
    for i in range(0, len(cntvals), 2):
        tot -= cntvals[i]
        
    #State: Output State: `cntvals` is a list of the counts of zeros in each integer of `nums`, sorted in descending order but with every second element removed; `tot` is reduced by the sum of the counts of zeros at even indices in `cntvals`; `n` is an integer representing the number of integers in the list, `m` is an integer determining when Sasha wins, and `nums` is a list of integers where each integer is between 1 and 10^9 inclusive.
    return 'Sasha' if tot >= m + 1 else 'Anna'
    #Sasha if the total (tot) is greater than or equal to m + 1, otherwise Anna
#Overall this is what the function does:The function accepts three parameters: `n` (the number of integers in the list), `m` (an integer determining when Sasha wins), and `nums` (a list of integers). It calculates the total length of the string representations of the integers in `nums`, sorts the counts of zeros in each integer in descending order while removing every second count, and then subtracts the sum of the counts at even indices from the total. Finally, it returns "Sasha" if the adjusted total is greater than or equal to `m + 1`, otherwise it returns "Anna".

#State of the program right berfore the function call: num is an integer such that 1 ≤ num ≤ 10^9.
def zerocnts(num):
    num = str(num)
    tot = 0
    for i in range(len(num) - 1, -1, -1):
        if num[i] != '0':
            break
        
        tot += 1
        
    #State: Output State: `num` is a string representation of an integer such that 1 ≤ num ≤ 10^9; `tot` is the number of trailing zeros in the string representation of `num`.
    #
    #Explanation: The loop iterates over the string `num` from the last character to the first. It increments `tot` each time it encounters a '0' at the current position. The loop breaks when it encounters the first non-zero digit. Therefore, `tot` will be the count of trailing zeros in `num`.
    return tot
    #The program returns the count of trailing zeros in the string representation of `num`
#Overall this is what the function does:The function accepts an integer `num` within the range of 1 to 10^9, converts it to a string, and counts the number of trailing zeros in its string representation. It then returns this count as an integer.

