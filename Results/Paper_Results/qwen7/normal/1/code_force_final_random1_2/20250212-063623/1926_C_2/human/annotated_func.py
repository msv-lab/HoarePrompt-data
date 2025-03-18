#State of the program right berfore the function call: num is a positive integer such that 1 <= num <= 2 * 10^5.
def func_1(num):
    a = 0
    while num != 0:
        a = a + num % 10
        
        num = int(num / 10)
        
    #State: Output State: `a` is the sum of all digits of the initial `num`, `num` is 0.
    #
    #Explanation: After the loop executes all iterations, `num` will eventually become 0 because the loop continues to divide `num` by 10 until it reaches 0. During each iteration, the last digit of `num` is added to `a`. Therefore, by the end of the loop, `a` contains the sum of all the digits of the original `num`.
    return a
    #The program returns 0 since the initial value of `num` is 0, and there are no digits to sum.
#Overall this is what the function does:The function accepts a positive integer `num` within the range of 1 to 2 * 10^5 and calculates the sum of its digits. It then returns this sum. However, if the initial value of `num` is 0, the function returns 0.

