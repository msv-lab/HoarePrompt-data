#State of the program right berfore the function call: k, n, a, and b are integers such that 0 <= k <= n, and 1 <= n, a, b <= 10^9.
def func_1(k, n, a, b):
    return k * b - k * (k - 1) // 2 + (n - k) * a
    #The program returns \( k \times b - k \times \frac{k - 1}{2} + (n - k) \times a \)
#Overall this is what the function does:The function calculates and returns the value of the expression \( k \times b - k \times \frac{k - 1}{2} + (n - k) \times a \) using the input integers \( k \), \( n \), \( a \), and \( b \) where \( 0 \le k \le n \) and \( 1 \le n, a, b \le 10^9 \).

