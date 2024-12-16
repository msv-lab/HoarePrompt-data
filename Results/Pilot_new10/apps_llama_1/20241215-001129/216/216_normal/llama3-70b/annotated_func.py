#State of the program right berfore the function call: The function func() takes no explicit parameters, but uses variables that are defined before it's called. These variables are n, an integer such that 1 <= n <= 200, and s, a string consisting only of lowercase and uppercase Latin letters, with a length of n characters.
def func():
    n = int(input())
    s = input()
    lowercase = [i for i, c in enumerate(s) if c.islower()]
    print(len(lowercase))
#Overall this is what the function does:The function takes an integer `n` and a string `s` as input from the user, counts the number of lowercase characters in the string `s`, and prints this count. The input `n` is not used within the function. The function does not handle any potential errors that might occur during input, such as non-integer input for `n` or a string `s` that does not match the expected length or character set.

