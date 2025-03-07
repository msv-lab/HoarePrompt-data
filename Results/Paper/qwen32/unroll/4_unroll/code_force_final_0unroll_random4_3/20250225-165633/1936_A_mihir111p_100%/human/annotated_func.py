#State of the program right berfore the function call: a, b, c, and d are integers such that 0 <= a, b, c, d < n, where n is the length of the secret permutation p_0, p_1, ..., p_{n-1}. The function `func_1` is used to make a query by providing these four indices and receiving the comparison result between (p_a | p_b) and (p_c | p_d).
def func_1(a, b, c, d):
    print('?', a, b, c, d)
    #This is printed: ? [a] [b] [c] [d] (where a, b, c, and d are integers such that 0 <= a, b, c, d < n)
    return input()
    #The program returns the value provided by the user input.
#Overall this is what the function does:The function `func_1` takes four integer parameters `a`, `b`, `c`, and `d` within the range from 0 to `n-1` (inclusive) and returns the result of a user-provided comparison between the bitwise OR of the elements at indices `a` and `b` in a secret permutation and the bitwise OR of the elements at indices `c` and `d`.

