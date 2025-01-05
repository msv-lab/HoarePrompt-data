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
#Overall this is what the function does:The function does not accept any parameters. It prompts the user to input two integers, A and B, computes their sum, difference, and product, and then finds and prints the maximum value among these results. The output is a printed statement showing the maximum value of the three computed results.

