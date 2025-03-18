#State of the program right berfore the function call: num is a list of integers where each integer n satisfies 1 ≤ n ≤ 2 · 10^5, and the length of num is between 1 and 10^4, inclusive. Each element in num represents the largest number Vladislav writes for a corresponding test case.
def func_1(num):
    a = 0
    while num != 0:
        a = a + num % 10
        
        num = int(num / 10)
        
    #State: `num` is a list of zeros with the same length as the original list, and `a` is the sum of all the digits of the original numbers in `num`.
    return a
    #The program returns 0
#Overall this is what the function does:The function `func_1` accepts a parameter `num`, which is expected to be a list of integers, but due to a logical error, it treats `num` as a single integer. It attempts to compute the sum of the digits of this integer. However, the function contains a bug and always returns 0 regardless of the input.

