#State of the program right berfore the function call: n is an integer representing the number of integers in the list, m is an integer representing the parameter determining when Sasha wins, and nums is a list of integers where 1 ≤ n ≤ 2 × 10^5, 0 ≤ m ≤ 2 × 10^6, and 1 ≤ a_i ≤ 10^9 for each a_i in nums.
def func_1(n, m, nums):
    tot = sum(len(val) for val in map(str, nums))
    cntvals = sorted((zerocnts(val) for val in nums), reverse=True)
    for i in range(0, len(cntvals), 2):
        tot -= cntvals[i]
        
    #State: Output State: `i` is equal to `2 * (len(cntvals) // 2)`, `tot` is decreased by the sum of every second element in `cntvals` starting from the first element, and `len(cntvals)` must be greater than or equal to `2 * (len(cntvals) // 2)`.
    #
    #In simpler terms, after the loop has executed all its iterations, the variable `i` will be twice the number of elements in `cntvals` divided by 2 (which is essentially the number of elements in `cntvals` if `len(cntvals)` is even, or one less than that if it's odd). The variable `tot` will have been reduced by the sum of every second value in the `cntvals` list, starting with the first value. This process continues until there are no more pairs of elements left in `cntvals`.
    return 'Sasha' if tot >= m + 1 else 'Anna'
    #The program returns 'Sasha' if the value of `tot` is greater than or equal to `m + 1`, otherwise it returns 'Anna'.
#Overall this is what the function does:The function accepts three parameters: `n`, representing the number of integers in the list; `m`, determining when Sasha wins; and `nums`, a list of integers. It calculates the total length of the string representations of all numbers in `nums`, sorts a count of zeros in each number in descending order, and then subtracts every second element from this sorted list starting from the first element. Finally, it returns 'Sasha' if the resulting total is greater than or equal to `m + 1`, otherwise it returns 'Anna'.

#State of the program right berfore the function call: num is an integer between 1 and 10^9 inclusive, representing an element in the list provided to Anna.
def zerocnts(num):
    num = str(num)
    tot = 0
    for i in range(len(num) - 1, -1, -1):
        if num[i] != '0':
            break
        
        tot += 1
        
    #State: Output State: `num` is a string representation of an integer between 1 and \(10^9\) inclusive, `i` is 0, `tot` is the length of `num`.
    #
    #Explanation: The loop continues to decrement `i` until it encounters a character in `num` that is not '0'. Since the loop increments `tot` each time it iterates without breaking, `tot` will count the number of trailing zeros in `num`. Once `i` reaches 0 (meaning there are no more characters left to check), the loop terminates. Therefore, after all iterations, `i` will be 0, and `tot` will be equal to the total number of trailing zeros in `num`.
    return tot
    #The program returns the total number of trailing zeros in the string representation of `num`
#Overall this is what the function does:The function accepts an integer `num` between 1 and \(10^9\) inclusive and returns the total number of trailing zeros in its string representation.

