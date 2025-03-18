#State of the program right berfore the function call: num is a list of integers where each integer n satisfies 1 ≤ n ≤ 2 \cdot 10^5, and the length of num is between 1 and 10^4, inclusive. Each element in num represents the largest number Vladislav writes for a test case.
def func_1(num):
    a = 0
    while num != 0:
        a = a + num % 10
        
        num = int(num / 10)
        
    #State: `num` is 0 and `a` is the sum of the digits of the original integer `num`.
    return a
    #The program returns 0
#Overall this is what the function does:The function `func_1` accepts a parameter `num`, which is expected to be a single integer (not a list of integers as annotated), and returns 0 regardless of the input value.

