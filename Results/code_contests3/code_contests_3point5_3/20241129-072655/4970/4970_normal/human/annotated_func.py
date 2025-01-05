#State of the program right berfore the function call: a is a non-negative integer such that 0 <= a <= 15.**
def func():
    print([15, 14, 12, 13, 8, 9, 10, 11, 0, 1, 2, 3, 4, 5, 6, 7][int(raw_input())])
#Overall this is what the function does:The function `func` does not accept any parameters. It prompts the user for input and based on the input value, it returns the corresponding word representation of the input integer within the range 0 to 15. For example, if the input is 3, the function will print "three". However, the code does not handle cases where the input is outside the range of 0 to 15.

