#State of the program right berfore the function call: s is a string of lowercase English letters with a length between 1 and 20, inclusive.
def func():
    n = raw_input()
    print(len(n) + 1) * 26 - len(n)
#Overall this is what the function does:The function reads a string of lowercase English letters from input, calculates and prints a value based on the formula `(length of the input string + 1) * 26 - length of the input string`. It does not return any value. The function does not accept any parameters directly.

