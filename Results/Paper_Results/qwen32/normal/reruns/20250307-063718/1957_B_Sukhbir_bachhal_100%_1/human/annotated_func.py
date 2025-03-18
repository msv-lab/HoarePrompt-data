#State of the program right berfore the function call: The input consists of an integer t (1 ≤ t ≤ 10^4) representing the number of test cases. Each of the next t lines contains two integers n (1 ≤ n ≤ 2 · 10^5) and k (1 ≤ k ≤ 10^9), where n is the number of non-negative integers to be printed and k is their sum. The sum of n over all test cases does not exceed 2 · 10^5.
def func_1(n):
    if (n == 0) :
        return -1
        #The program returns -1
    #State: The input consists of an integer t (1 ≤ t ≤ 10^4) representing the number of test cases. Each of the next t lines contains two integers n (1 ≤ n ≤ 2 · 10^5) and k (1 ≤ k ≤ 10^9), where n is the number of non-negative integers to be printed and k is their sum. The sum of n over all test cases does not exceed 2 · 10^5. Additionally, n is not equal to 0.
    position = 0
    while n != 0:
        n >>= 1
        
        position += 1
        
    #State: `n` is 0 and `position` is the number of bits in the binary representation of the original `n`.
    return position - 1
    #The program returns -1
#Overall this is what the function does:The function `func_1` accepts an integer `n` as a parameter and always returns -1, regardless of the value of `n`.

