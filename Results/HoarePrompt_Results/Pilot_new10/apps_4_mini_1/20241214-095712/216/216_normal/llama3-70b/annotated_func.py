#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 200, and s is a string consisting of only lowercase and uppercase Latin letters with a length equal to n.
def func():
    n = int(input())
    s = input()
    lowercase = [i for i, c in enumerate(s) if c.islower()]
    print(len(lowercase))
#Overall this is what the function does:The function accepts an integer `n` (1 ≤ n ≤ 200) and a string `s` that is expected to be of length `n`, consisting only of lowercase and uppercase Latin letters. It calculates the number of lowercase letters in the string `s` and prints this count.

