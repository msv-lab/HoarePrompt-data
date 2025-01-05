#State of the program right berfore the function call: n is a prime number greater than or equal to 5 and r is a positive integer greater than or equal to 1.**
def func():
    n, r = map(int, raw_input().split())
    pi = 3.141592653589793
    ans = float(n * r * r * math.sin(pi / (2 * n)) * math.sin(pi / n) / math.
    sin(3 * pi / (2 * n)))
    print(ans)
#Overall this is what the function does:The function reads two integers `n` and `r` from input and calculates the value of nCr using a mathematical formula. It then prints the result. The function assumes `n` is a prime number greater than or equal to 5 and `r` is a positive integer greater than or equal to 1. However, the code snippet is missing the import statement for the `math` module, which is necessary for the calculations to be performed. Additionally, the function lacks error handling for cases where the input values are not within the specified constraints.

