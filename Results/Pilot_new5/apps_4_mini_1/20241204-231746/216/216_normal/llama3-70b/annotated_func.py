#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 200, and s is a string consisting of lowercase and uppercase Latin letters with length n.
def func():
    n = int(input())
    s = input()
    lowercase = [i for i, c in enumerate(s) if c.islower()]
    print(len(lowercase))
#Overall this is what the function does:The function accepts a positive integer `n` (where 1 ≤ n ≤ 200) and a string `s` of length `n`, and it counts and prints the number of lowercase letters in the string `s`. It does not handle cases where the input string length does not match `n`.

