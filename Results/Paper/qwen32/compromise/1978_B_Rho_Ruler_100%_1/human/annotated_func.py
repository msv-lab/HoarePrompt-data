#State of the program right berfore the function call: k is an integer such that 0 <= k <= n, n is a positive integer, a and b are positive integers.
def func_1(k, n, a, b):
    return k * b - k * (k - 1) // 2 + (n - k) * a
    #The program returns the value of \( k \times b - k \times (k - 1) // 2 + (n - k) \times a \)
#Overall this is what the function does:The function calculates and returns the result of the expression \( k \times b - k \times (k - 1) // 2 + (n - k) \times a \) using the input integers \( k \), \( n \), \( a \), and \( b \).

