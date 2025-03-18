#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, n and k are integers such that 1 ≤ n ≤ 2·10^5 and 1 ≤ k ≤ 10^9. The sum of all n over all test cases does not exceed 2·10^5.
def func_1(n):
    if (n == 0) :
        return -1
        #The program returns -1
    #State: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, n and k are integers such that 1 ≤ n ≤ 2·10^5 and 1 ≤ k ≤ 10^9, with n not equal to 0. The sum of all n over all test cases does not exceed 2·10^5.
    position = 0
    while n != 0:
        n >>= 1
        
        position += 1
        
    #State: Output State: `t` is an integer such that 1 ≤ t ≤ 10^4, `position` is the number of times `n` can be right-shifted until it becomes 0, `n` is 0.
    #
    #Explanation: The loop continues to right-shift `n` by 1 bit until `n` becomes 0. The variable `position` keeps track of how many times the loop has executed, which is equivalent to the number of bits in the binary representation of `n`. Therefore, once `n` becomes 0, the loop terminates, and `position` will be the total number of bits in the binary representation of the initial value of `n`.
    return position - 1
    #The program returns a value that is one less than the number of bits in the binary representation of the initial value of `t`
#Overall this is what the function does:The function accepts an integer `n` and returns -1 if `n` is 0. Otherwise, it returns a value that is one less than the number of bits in the binary representation of the initial value of `n`.

