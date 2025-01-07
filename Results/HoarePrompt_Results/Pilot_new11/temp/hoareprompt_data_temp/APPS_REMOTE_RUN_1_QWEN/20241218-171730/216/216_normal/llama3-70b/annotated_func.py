#State of the program right berfore the function call: The input consists of two lines. The first line contains a single integer n (1 ≤ n ≤ 200) representing the length of the string s. The second line contains a string s consisting of lowercase and uppercase Latin letters.
def func():
    n = int(input())
    s = input()
    lowercase = [i for i, c in enumerate(s) if c.islower()]
    print(len(lowercase))
#Overall this is what the function does:The function reads an integer `n` and a string `s` from the user. It then enumerates through the string `s` to find all indices where the character is lowercase and prints the count of such indices. The function does not modify the input string `s`. If the input string `s` is empty or contains no lowercase letters, the output will be `0`.

