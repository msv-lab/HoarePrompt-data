#State of the program right berfore the function call: num is an integer such that 1 <= num <= 10^9.
def func_1(num):
    counter = 0
    for i in range(len(num) - 1, -1, -1):
        if num[i] == '0':
            counter += 1
        else:
            break
        
    #State: The output state after the loop executes all the iterations is as follows: `counter` will hold the total count of '0' digits from the end of `num` until the first non-zero digit is encountered, `num` remains an integer such that \(1 \leq num \leq 10^9\), and `i` will be the index where the loop breaks, which is the position right after the last '0' digit or 0 if `num` consists entirely of '0's.
    return counter
    #The program returns the total count of '0' digits from the end of `num` until the first non-zero digit is encountered
#Overall this is what the function does:The function accepts an integer `num` within the range of 1 to 10^9. It counts the number of trailing zeros in `num` (zeros at the end of the number) until it encounters the first non-zero digit. The function then returns this count. If `num` consists entirely of zeros, the returned count is also zero.

