#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 200, and s is a string consisting of lowercase and uppercase Latin letters with length exactly n.
def func():
    n = int(input())
    s = input()
    lowercase = [i for i, c in enumerate(s) if c.islower()]
    print(len(lowercase))
#Overall this is what the function does:The function takes two inputs: a positive integer `n`, which must be between 1 and 200 inclusive, and a string `s` whose length is exactly `n`. It counts the number of lowercase letters in the string `s` and prints that count. The function does not handle cases where `s` is not strictly `n` characters long or where `n` is outside the specified bounds, though such inputs are assumed to be valid based on the given preconditions. The final state of the program is that it outputs the count of lowercase letters found in the input string `s`.

