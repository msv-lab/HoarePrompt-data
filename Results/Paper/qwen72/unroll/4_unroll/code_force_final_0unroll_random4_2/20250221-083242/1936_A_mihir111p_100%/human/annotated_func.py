#State of the program right berfore the function call: a, b, c, and d are non-negative integers such that 0 <= a, b, c, d < n, where n is the length of the permutation p.
def func_1(a, b, c, d):
    print('?', a, b, c, d)
    #This is printed: ? [a] [b] [c] [d] (where a, b, c, and d are non-negative integers such that 0 <= a, b, c, d < n, and n is the length of the permutation p)
    return input()
    #The program returns the input provided by the user.
#Overall this is what the function does:The function `func_1` accepts four non-negative integer parameters `a`, `b`, `c`, and `d`, and prints a query string in the format `? [a] [b] [c] [d]`. It then waits for user input and returns whatever the user inputs. The function does not modify the input parameters or any external state.

