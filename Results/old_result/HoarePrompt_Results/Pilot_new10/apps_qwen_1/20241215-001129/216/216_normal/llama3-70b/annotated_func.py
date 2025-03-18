#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 200, and s is a string consisting only of lowercase and uppercase Latin letters.
def func():
    n = int(input())
    s = input()
    lowercase = [i for i, c in enumerate(s) if c.islower()]
    print(len(lowercase))
#Overall this is what the function does:The function accepts an integer `n` such that \(1 \leq n \leq 200\) and a string `s` consisting only of lowercase and uppercase Latin letters. It then creates a list of indices where the characters in `s` are lowercase letters and prints the length of this list.

