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
#Overall this is what the function does:The function accepts no parameters and prompts the user to input two integers, `a` and `b`, within the range of -1000 to 1000. It calculates the sum, difference, and product of these integers, stores these results in a list, and then prints the maximum value among them. The function does not return any value.

