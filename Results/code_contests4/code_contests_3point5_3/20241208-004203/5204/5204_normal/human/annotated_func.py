#State of the program right berfore the function call: l, p, q are positive integers such that 1 <= l <= 1000 and 1 <= p, q <= 500.**
def func():
    l = input()
    p = input()
    q = input()
    print(float(l) / (p + q)) * p
#Overall this is what the function does:The function `func` prompts the user for input values for variables `l`, `p`, and `q`, which are then used to perform a calculation. The calculation involves dividing `l` by the sum of `p` and `q`, then multiplying the result by `p`. The function does not return any value. However, it is important to note that the provided annotations mention that `l`, `p`, and `q` are positive integers within specific ranges, but the code does not enforce these constraints or handle any potential input errors related to non-integer inputs or division by zero.

