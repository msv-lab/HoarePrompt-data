#State of the program right berfore the function call: s is a string of lowercase English letters with length between 1 and 20 (inclusive).**
def func():
    n = raw_input()
    print(len(n) + 1) * 26 - len(n)
#Overall this is what the function does:The function `func` reads a string `n` as input, calculates a value based on the length of the string, and prints the result. The function does not explicitly return any value. However, there is a missing functionality in the code where the multiplication operation is missing brackets, which might affect the intended calculation. Additionally, there is no validation for the input string `n` to ensure it only contains lowercase English letters.

