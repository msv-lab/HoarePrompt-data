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
#Overall this is what the function does:The function accepts no parameters and prompts the user to input two integers, `a` and `b`. It calculates the sum, difference, and product of these integers and stores them in a list. The function then finds and prints the maximum value from this list. Note that the function does not return any value; it only prints the maximum result.

