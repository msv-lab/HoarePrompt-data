#State of the program right berfore the function call: num is a positive integer such that 1 <= num <= 2 * 10^5.
def func_1(num):
    a = 0
    while num != 0:
        a = a + num % 10
        
        num = int(num / 10)
        
    #State: Output State: `a` is equal to the sum of all digits of `num`, `num` is 0.
    #
    #Explanation: After the loop completes all its iterations, `num` will eventually become 0 because the loop continues to divide `num` by 10 until it reaches 0. During each iteration, the digit of `num` that is being removed (by performing `num % 10`) is added to `a`. Therefore, `a` accumulates the sum of all digits of the original `num` until `num` is fully reduced to 0.
    return a
    #The program returns 0 since num is initially 0 and no digits are summed.
#Overall this is what the function does:The function accepts a positive integer `num` within the range of 1 to 2 * 10^5. It calculates the sum of all digits of `num` and stores it in variable `a`. After processing, the function returns the value of `a`. If `num` is initially 0, the function returns 0.

