#State of the program right berfore the function call: k is an integer such that 0 <= k <= min(n, b), n is an integer representing the number of buns, a is an integer representing the usual price of a bun, and b is an integer representing the price of the first bun to be sold at a modified price.
def func_1(k, n, a, b):
    return k * b - k * (k - 1) // 2 + (n - k) * a
    #The program returns the value calculated as k times b minus k times (k minus 1) divided by 2 plus (n minus k) times a
#Overall this is what the function does:The function accepts four parameters: k, n, a, and b. It calculates and returns the value given by the formula k times b minus k times (k minus 1) divided by 2 plus (n minus k) times a.

