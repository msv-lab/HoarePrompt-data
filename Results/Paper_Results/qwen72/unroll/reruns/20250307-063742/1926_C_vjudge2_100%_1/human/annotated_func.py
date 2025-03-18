#State of the program right berfore the function call: num is an integer such that 1 <= num <= 2 * 10^5.
def func_1(num):
    a = 0
    while num != 0:
        a = a + num % 10
        
        num = int(num / 10)
        
    #State: `a` is the sum of the digits of the initial value of `num`, and `num` is 0.
    return a
    #The program returns 0.
#Overall this is what the function does:The function `func_1` accepts an integer `num` within the range 1 to 2 * 10^5. It calculates the sum of the digits of the initial value of `num` and returns this sum. After the function concludes, the parameter `num` is 0, and the return value is the sum of the digits of the initial `num`.

