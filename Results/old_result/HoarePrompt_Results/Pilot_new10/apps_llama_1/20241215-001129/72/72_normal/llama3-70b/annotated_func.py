#State of the program right berfore the function call: n and m are integers between 1 and 100, k is a non-negative integer, x and y are integers between 1 and n and 1 and m respectively.
def func():
    n, m, k, x, y = map(int, input().split())
    max_asked = (k + (n - 1)) // (2 * n)
    min_asked = max(1, max_asked - (n - 1))
    sergei_asked = (k + x - 1) // (2 * n) + ((k + x - 1) % (2 * n) >= n - x + 1)
    print(max_asked, min_asked, sergei_asked)
#Overall this is what the function does:The function takes five integer inputs from the user, calculates the maximum, minimum, and Sergei's asked items based on the provided formulas, and prints these values, without enforcing any explicit constraints on the input values.

