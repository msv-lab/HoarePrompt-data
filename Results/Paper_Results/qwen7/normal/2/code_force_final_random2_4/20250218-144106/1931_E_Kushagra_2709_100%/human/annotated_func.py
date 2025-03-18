#State of the program right berfore the function call: n is an integer representing the number of integers in the list, m is an integer determining when Sasha wins, and nums is a list of integers where each integer is between 1 and 10^9 inclusive.
def func_1(n, m, nums):
    tot = sum(len(val) for val in map(str, nums))
    cntvals = sorted((zerocnts(val) for val in nums), reverse=True)
    for i in range(0, len(cntvals), 2):
        tot -= cntvals[i]
        
    #State: Output State: The loop will iterate over the range from 0 to the length of `cntvals` with a step of 2 until there are no more elements to process. After all iterations, `i` will be equal to the largest even number less than or equal to the length of `cntvals`, and `tot` will be decreased by the sum of every second element in `cntvals`, starting from the first element.
    #
    #In simpler terms, after the loop completes all its iterations, `i` will be the largest even number not exceeding the length of `cntvals`, and `tot` will have been reduced by the sum of all elements in `cntvals` at even indices (starting from index 0).
    return 'Sasha' if tot >= m + 1 else 'Anna'
    #The program returns 'Sasha' if the variable `tot` is greater than or equal to the value of `m + 1`, otherwise it returns 'Anna'.
#Overall this is what the function does:The function accepts three parameters: `n` (an integer representing the number of integers in the list), `m` (an integer determining when Sasha wins), and `nums` (a list of integers where each integer is between 1 and 10^9 inclusive). It calculates the total length of the string representations of all integers in `nums`, sorts a list of their zero counts in descending order, and then subtracts the sum of every second element in this sorted list from a cumulative total. Finally, it returns 'Sasha' if the resulting total is greater than or equal to `m + 1`, otherwise it returns 'Anna'.

#State of the program right berfore the function call: num is an integer such that 1 <= num <= 10^9.
def zerocnts(num):
    num = str(num)
    tot = 0
    for i in range(len(num) - 1, -1, -1):
        if num[i] != '0':
            break
        
        tot += 1
        
    #State: Output State: `num` is a string representation of an integer with a length of at least 1, `i` is 0, `tot` is equal to the number of trailing zeros in `num`.
    #
    #Explanation: After the loop has executed all its iterations, `i` will be set to 0 because the loop decrements `i` from `len(num) - 1` until it finds a non-zero digit or reaches the beginning of the string. The variable `tot` will count the number of trailing zeros in the string `num`. This is because each time the loop encounters a '0', it increments `tot` by 1. Once a non-zero digit is encountered, the loop breaks, and `i` remains as the index of that non-zero digit.
    return tot
    #`The program returns the number of trailing zeros in the string representation of the integer 'num'`
#Overall this is what the function does:The function accepts an integer `num` between 1 and 10^9, converts it to a string, and counts the number of trailing zeros. It then returns this count as an integer.

