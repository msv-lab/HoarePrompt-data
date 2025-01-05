#State of the program right berfore the function call: n is a prime number greater than or equal to 5, and r is a positive integer greater than or equal to 1.**
def func():
    n, r = map(int, raw_input().split())
    pi = 3.141592653589793
    ans = float(n * r * r * math.sin(pi / (2 * n)) * math.sin(pi / n) / math.
    sin(3 * pi / (2 * n)))
    print(ans)
#Overall this is what the function does:The function `func` reads two integers `n` and `r` from the user input, then calculates a specific result based on these values. The calculation involves mathematical operations using the input values. However, the code snippet is incomplete as it imports the `math` module which is not present in the given code snippet. Additionally, there is a syntax error in the calculation of `ans` due to an incomplete expression. The function prints out the calculated result `ans`. It does not return any value.

