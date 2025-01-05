#State of the program right berfore the function call: A and B are integers such that -1000 <= A, B <= 1000.
def func():
    a = int(input())
    b = int(input())
    c = a + b
    d = a - b
    e = a * b
    ary = [c, d, e]
    f = max(ary)
    print('Max:', f)
#Overall this is what the function does:The function accepts two integers `a` and `b` as input from the user, calculates their sum, difference, and product, and then determines the maximum value among these three results. It prints the maximum value. Note that the function does not return any value; it only prints the result. The inputs are assumed to be within the range of -1000 to 1000, but if invalid input is provided (e.g., non-integer values), the function will raise a ValueError.

