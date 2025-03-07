#State of the program right berfore the function call: num is an integer such that 1 ≤ num ≤ 2 · 10^5.
def func_1(num):
    a = 0
    while num != 0:
        a = a + num % 10
        
        num = int(num / 10)
        
    #State: num is 0; a is the sum of all the digits of the original num.
    return a
    #The program returns 0
#Overall this is what the function does:The function accepts an integer `num` within the range 1 to 200,000 and returns the sum of its digits.

