#State of the program right berfore the function call: num is a positive integer such that 1 <= num <= 2 * 10^5.
def func_1(num):
    a = 0
    while num != 0:
        a = a + num % 10
        
        num = int(num / 10)
        
    #State: Output State: `a` will be equal to the sum of all digits of the initial value of `num`, and `num` will be reduced to 0.
    #
    #Explanation: The loop continues to extract the last digit of `num` and add it to `a` until `num` becomes 0. Therefore, after all iterations, `a` contains the sum of all digits of the original `num`, and `num` itself will be 0 since the loop terminates when `num` equals 0.
    return a
    #The program returns the sum of all digits of the initial value of num, and num is reduced to 0.
#Overall this is what the function does:The function accepts a positive integer `num` within the range of 1 to 2 * 10^5. It calculates the sum of all digits of `num` and returns this sum. Additionally, it modifies `num` to become 0 after performing these operations.

