#State of the program right berfore the function call: a, b, c, and d are integers such that 0 <= a, b, c, d < n, where n is the length of the secret permutation p. The function is used to make a query to compare the bitwise OR of two pairs of elements from the permutation.
def func_1(a, b, c, d):
    print('?', a, b, c, d)
    #This is printed: ? [a] [b] [c] [d] (where a, b, c, and d are integers such that 0 <= a, b, c, d < n)
    return input()
    #The program returns the value provided by the user input.
#Overall this is what the function does:The function `func_1` takes four integer parameters `a`, `b`, `c`, and `d` and prints a query to compare the bitwise OR of the elements at positions `a` and `b` with the bitwise OR of the elements at positions `c` and `d` in a secret permutation `p`. It then returns the value provided by the user input as a result of this query.

