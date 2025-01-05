#State of the program right berfore the function call: s is a string of lowercase English letters with a length between 1 and 20, inclusive.
def func():
    n = raw_input()
    print(len(n) + 1) * 26 - len(n)
#Overall this is what the function does:The function accepts input from the user as a string of lowercase English letters, calculates a specific value based on the length of this string (specifically, it computes `(length of string + 1) * 26 - length of string`), and prints this value. However, it does not explicitly accept any parameters since it uses `raw_input()` to obtain the string directly from user input. It also lacks error handling for unexpected input, and the result is not returned but printed instead.

