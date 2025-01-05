#State of the program right berfore the function call: s is a string of length between 1 and 20, consisting only of lowercase English letters.
def func():
    n = raw_input()
    print(len(n) + 1) * 26 - len(n)
#Overall this is what the function does:The function reads a string from user input, calculates a value based on its length, and prints the result. However, it does not return any value or handle edge cases, such as invalid input types.

