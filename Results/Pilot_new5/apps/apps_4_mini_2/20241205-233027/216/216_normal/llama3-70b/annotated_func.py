#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 200, and s is a string consisting of lowercase and uppercase Latin letters with a length of n.
def func():
    n = int(input())
    s = input()
    lowercase = [i for i, c in enumerate(s) if c.islower()]
    print(len(lowercase))
#Overall this is what the function does:The function accepts an integer `n` (1 ≤ n ≤ 200), reads a string `s` of length `n` consisting of lowercase and uppercase Latin letters, and counts the number of lowercase letters in the string. It then prints this count. The function does not return any value.

