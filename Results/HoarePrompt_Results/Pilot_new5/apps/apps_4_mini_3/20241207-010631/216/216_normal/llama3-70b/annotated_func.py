#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 200), and s is a string consisting of lowercase and uppercase Latin letters with a length equal to n.
def func():
    n = int(input())
    s = input()
    lowercase = [i for i, c in enumerate(s) if c.islower()]
    print(len(lowercase))
#Overall this is what the function does:The function accepts a positive integer `n` (1 ≤ n ≤ 200) and a string `s` of length `n`. It counts and prints the number of lowercase letters in the string `s`. The function does not return any value.

