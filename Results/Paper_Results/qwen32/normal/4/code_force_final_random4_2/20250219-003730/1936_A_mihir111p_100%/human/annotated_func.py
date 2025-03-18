#State of the program right berfore the function call: a, b, c, and d are integers such that 0 <= a, b, c, d < n, where n is the length of the secret permutation p.
def func_1(a, b, c, d):
    print('?', a, b, c, d)
    #This is printed: ? [a] [b] [c] [d] (where a, b, c, and d are integers such that 0 <= a, b, c, d < n)
    return input()
    #The program returns the input provided by the user.
#Overall this is what the function does:The function accepts four integer parameters `a`, `b`, `c`, and `d`, each within the range from 0 to `n-1`, where `n` is the length of a secret permutation `p`. It prints these four integers in a specific format and then returns the input provided by the user.

