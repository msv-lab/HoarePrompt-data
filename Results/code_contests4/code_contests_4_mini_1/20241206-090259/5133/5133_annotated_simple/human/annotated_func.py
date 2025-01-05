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
#Overall this is what the function does:The function accepts two integers `a` and `b` from user input, calculates their sum, difference, and product, and then determines the maximum value among these three results. It prints the maximum value prefixed with 'Max:'. The function does not return any value.

