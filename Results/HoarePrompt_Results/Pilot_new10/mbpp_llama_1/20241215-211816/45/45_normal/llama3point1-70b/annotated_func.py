#State of the program right berfore the function call: n is a positive integer.
def func_1(n):
    n = str(n)
    undulating = True
    for i in range(1, len(n) - 1):
        if n[i - 1] < n[i] and n[i] < n[i + 1] or n[i - 1] > n[i] and n[i] > n[i + 1]:
            pass
        else:
            undulating = False
            break
        
    #State of the program after the  for loop has been executed: `n` is a string representation of a positive integer, `i` is the second last index of `n` if `n` has a length of at least 3, `undulating` is `True` if all sequences of three adjacent digits in `n` are either in ascending or descending order, and `False` otherwise.
    return undulating
    #The program returns a boolean value indicating whether all sequences of three adjacent digits in the string representation of a positive integer are in ascending or descending order.
#Overall this is what the function does:The function checks if all sequences of three adjacent digits in the string representation of a positive integer are in ascending or descending order, returning True if they are and False otherwise, and returns True for integers with fewer than three digits.

