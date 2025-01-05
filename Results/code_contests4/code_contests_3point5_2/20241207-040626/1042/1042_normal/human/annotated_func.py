#State of the program right berfore the function call: s is a string of lowercase English letters with length between 1 and 20.**
def func():
    n = raw_input()
    print(len(n) + 1) * 26 - len(n)
#Overall this is what the function does:The function `func` reads a string `n` as input and calculates a value based on the length of the string. It multiplies the length of the string by 26, subtracts the length of the string from this result, and then prints the final value. The function does not return any value.

