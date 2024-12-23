#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 200) representing the length of string s, and s is a string consisting of lowercase and uppercase Latin letters.
def func():
    n = int(input())
    s = input()
    lowercase = [i for i, c in enumerate(s) if c.islower()]
    print(len(lowercase))
#Overall this is what the function does:The function accepts a positive integer `n` (1 ≤ n ≤ 200) representing the length of a string `s`, and the string `s` itself, which consists of lowercase and uppercase Latin letters. It counts the number of lowercase characters in the string and prints this count. However, the function does not validate if the length of `s` matches `n`, which is a potential edge case. After execution, the program will display the total number of lowercase letters in `s`.

