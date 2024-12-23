#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 200, and s is a string consisting only of lowercase and uppercase Latin letters.
def func():
    n = int(input())
    s = input()
    lowercase = [i for i, c in enumerate(s) if c.islower()]
    print(len(lowercase))
#Overall this is what the function does:The function reads an integer `n` and a string `s` from the standard input. It then creates a list of indices where the characters in `s` are lowercase letters and prints the length of this list. The function does not return any value. Potential edge cases include invalid input types for `n` and `s`, and the function will handle these by attempting to process the input as specified. If `n` is not within the range 1 ≤ n ≤ 200, the function will still proceed and ignore this parameter, focusing solely on counting the lowercase letters in `s`.

