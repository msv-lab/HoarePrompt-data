#State of the program right berfore the function call: n is a non-negative integer.**
def func_1(n):
    if (n <= 2) :
        return 0
        #The program returns 0
    #State of the program after the if block has been executed: *n is a non-negative integer. n is larger than 2.
    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n, i):
                is_prime[j] = False
        
    #State of the program after the  for loop has been executed: After all iterations of the loop have finished, `n` is a non-negative integer larger than 2, `is_prime` is a list of n elements where each element is True if the corresponding index is a prime number, and False otherwise.
    return sum(is_prime)
    #The program returns the sum of the elements in the list `is_prime`, where each element is True if the corresponding index is a prime number, and False otherwise.
#Overall this is what the function does:The function `func_1` accepts a non-negative integer `n`. If `n` is less than or equal to 2, the function returns 0. For `n` greater than 2, the function generates a list `is_prime` where each element is True if the index is a prime number, and False otherwise. It then returns the sum of the elements in the `is_prime` list. However, the code does not handle the case when `n` is 1 or 2, where the function should return 0 according to the comments, but `is_prime` is not being correctly calculated.

