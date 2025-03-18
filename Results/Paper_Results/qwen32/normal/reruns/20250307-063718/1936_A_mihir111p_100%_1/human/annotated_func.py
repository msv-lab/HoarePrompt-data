#State of the program right berfore the function call: a, b, c, and d are integers such that 0 <= a, b, c, d < n, where n is the length of the secret permutation p. The function func_1 is used to make a query by providing these indices to compare the bitwise OR of two pairs of elements in the permutation.
def func_1(a, b, c, d):
    print('?', a, b, c, d)
    #This is printed: ? [a] [b] [c] [d] (where a, b, c, and d are integers such that 0 <= a, b, c, d < n)
    return input()
    #The program returns the value provided by the user input.
#Overall this is what the function does:The function `func_1` accepts four integer parameters `a`, `b`, `c`, and `d`, each within the range from 0 to `n-1`, where `n` is the length of a secret permutation `p`. It prints a query comparing the bitwise OR of the pairs `(p[a], p[b])` and `(p[c], p[d])`. The function returns the value provided by the user input in response to this query.

