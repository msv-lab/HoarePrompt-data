#State of the program right berfore the function call: num is a positive integer such that 1 <= num <= 2 * 10^5.
def func_1(num):
    a = 0
    while num != 0:
        a = a + num % 10
        
        num = int(num / 10)
        
    #State: `num` is 0, and `a` is the sum of the digits of the original `num`.
    return a
    #The program returns 0.
#Overall this is what the function does:The function `func_1` accepts a positive integer `num` (where 1 <= num <= 2 * 10^5) and returns the sum of its digits. After the function executes, `num` is reduced to 0, and the returned value is the sum of the digits of the original `num`.

