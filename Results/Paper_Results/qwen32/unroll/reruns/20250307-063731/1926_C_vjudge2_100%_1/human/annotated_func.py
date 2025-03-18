#State of the program right berfore the function call: num is an integer such that 1 ≤ num ≤ 2 · 10^5.
def func_1(num):
    a = 0
    while num != 0:
        a = a + num % 10
        
        num = int(num / 10)
        
    #State: `a` is the sum of the digits of the original `num`.
    return a
    #The program returns the sum of the digits of the original `num`.
#Overall this is what the function does:The function accepts an integer `num` between 1 and 200,000 inclusive and returns the sum of its digits.

