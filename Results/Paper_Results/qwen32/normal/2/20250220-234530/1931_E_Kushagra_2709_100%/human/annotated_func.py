#State of the program right berfore the function call: n is an integer representing the number of integers in the list, m is a non-negative integer determining when Sasha wins, and nums is a list of n integers where each integer is between 1 and 10^9 inclusive.
def func_1(n, m, nums):
    tot = sum(len(val) for val in map(str, nums))
    cntvals = sorted((zerocnts(val) for val in nums), reverse=True)
    for i in range(0, len(cntvals), 2):
        tot -= cntvals[i]
        
    #State: `n` is an integer representing the number of integers in the list, `m` is a non-negative integer determining when Sasha wins, `nums` is a list of `n` integers where each integer is between 1 and \(10^9\) inclusive, `tot` is the total number of digits in all integers in `nums` minus the sum of all elements at even indices in `cntvals`, `cntvals` is a list of zero counts for each number in `nums` sorted in descending order, `i` is the last even index processed in the loop.
    return 'Sasha' if tot >= m + 1 else 'Anna'
    #The program returns 'Sasha' if tot (which is the total number of digits in all integers in nums minus the sum of all elements at even indices in cntvals) is greater than or equal to m + 1; otherwise, it returns 'Anna'.
#Overall this is what the function does:The function determines the winner of a game between Sasha and Anna based on the total number of digits in a list of integers, adjusted by the count of zeros in each integer. It returns 'Sasha' if the adjusted digit count is at least one more than a given threshold `m`; otherwise, it returns 'Anna'.

#State of the program right berfore the function call: num is an integer such that 1 <= num <= 10^9.
def zerocnts(num):
    num = str(num)
    tot = 0
    for i in range(len(num) - 1, -1, -1):
        if num[i] != '0':
            break
        
        tot += 1
        
    #State: - The loop will stop when it encounters a non-'0' character.
    #- `tot` will be equal to the number of trailing '0's in `num`.
    #
    #Thus, the final output state will be:
    #- `num` remains the same.
    #- `tot` will be the total number of trailing '0's in `num`.
    #
    #Output State:
    return tot
    #The program returns `tot`, which is the total number of trailing '0's in `num`.
#Overall this is what the function does:The function accepts an integer `num` within the range 1 to 10^9 and returns the count of trailing zeros in its decimal representation.

