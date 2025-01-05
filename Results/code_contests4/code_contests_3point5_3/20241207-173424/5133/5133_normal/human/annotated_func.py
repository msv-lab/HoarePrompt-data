#State of the program right berfore the function call: A and B are integers such that -1000 <= A,B <= 1000.
def func():
    a = int(input())
    b = int(input())
    c = a + b
    d = a - b
    e = a * b
    ary = [c, d, e]
    f = max(ary)
    print('Max:', f)
#Overall this is what the function does:The function takes user input for two integers A and B, calculates their sum, difference, and product, stores them in an array, finds the maximum value among them, and prints the maximum value as 'Max: f'.

