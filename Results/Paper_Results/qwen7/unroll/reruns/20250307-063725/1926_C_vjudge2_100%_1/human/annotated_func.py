#State of the program right berfore the function call: num is a positive integer such that 1 <= num <= 2 * 10^5.
def func_1(num):
    a = 0
    while num != 0:
        a = a + num % 10
        
        num = int(num / 10)
        
    #State: a is the sum of all digits in the original value of num.
    return a
    #The program returns the sum of all digits in the original value of num.
#Overall this is what the function does:The function accepts a positive integer num within the range of 1 to 2 * 10^5 and returns the sum of all its digits.

