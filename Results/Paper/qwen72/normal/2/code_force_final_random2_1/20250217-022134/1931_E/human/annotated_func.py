#State of the program right berfore the function call: n is a positive integer representing the number of integers in the list, m is a non-negative integer representing the threshold for Sasha's win condition, and nums is a list of n positive integers where each integer is between 1 and 10^9 inclusive.
def func_1(n, m, nums):
    if (n == 1) :
        return 'Sasha' if len(str(min(n, int(str(n)[::-1])))) >= m + 1 else 'Anna'
        #The program returns 'Anna'.
    #State: n is a positive integer representing the number of integers in the list, m is a non-negative integer representing the threshold for Sasha's win condition, and nums is a list of n positive integers where each integer is between 1 and 10^9 inclusive. Additionally, n is greater than 1.
    tot = sum(len(val) for val in map(str, nums))
    cntvals = sorted((zerocnts(val) for val in nums), reverse=True)
    for i in range(0, len(cntvals), 2):
        tot -= cntvals[i]
        
    #State: `n` is a positive integer, `m` is a non-negative integer, `nums` is a list of `n` positive integers where each integer is between 1 and 10^9 inclusive, `tot` is the sum of the lengths of the string representations of the elements in `nums` minus the sum of the even-indexed elements in `cntvals`, `cntvals` is a list of zero counts of each element in `nums`, sorted in descending order, and `i` is the largest even index less than the length of `cntvals`.
    return 'Sasha' if tot >= m + 1 else 'Anna'
    #The program returns 'Sasha' if the sum of the lengths of the string representations of the elements in `nums` minus the sum of the even-indexed elements in `cntvals` (which is a list of zero counts of each element in `nums`, sorted in descending order) is greater than or equal to `m + 1`. Otherwise, it returns 'Anna'.
#Overall this is what the function does:The function `func_1` takes three parameters: `n` (a positive integer representing the number of integers in the list), `m` (a non-negative integer representing the threshold for Sasha's win condition), and `nums` (a list of `n` positive integers where each integer is between 1 and 10^9 inclusive). It returns 'Sasha' if the sum of the lengths of the string representations of the elements in `nums` minus the sum of the even-indexed elements in `cntvals` (a list of zero counts of each element in `nums`, sorted in descending order) is greater than or equal to `m + 1`. Otherwise, it returns 'Anna'. If `n` is 1, it returns 'Anna' if the length of the string representation of the minimum of `n` and its reverse is less than `m + 1`; otherwise, it returns 'Sasha'.

#State of the program right berfore the function call: num is an integer such that 1 ≤ num ≤ 10^9.
def zerocnts(num):
    num = str(num)
    tot = 0
    for i in range(len(num) - 1, -1, -1):
        if num[i] != '0':
            break
        
        tot += 1
        
    #State: `num` is a string representation of an integer such that 1 ≤ `num` ≤ 10^9, `tot` is the number of trailing zeros in `num`, and `i` is the index of the first non-zero digit from the right, or -1 if all digits are zero.
    return tot
    #The program returns the number of trailing zeros in the string representation of `num`.
#Overall this is what the function does:The function `zerocnts` accepts an integer `num` within the range 1 ≤ num ≤ 10^9 and returns the number of trailing zeros in the string representation of `num`. After the function concludes, `num` remains unchanged, and the returned value represents the count of consecutive zeros at the end of the string representation of `num`.

