#State of the program right berfore the function call: n is an integer such that 1 <= n <= 500, and s is a string of length n consisting of lowercase Latin letters.
def func():
    n = int(input())
    s = input()
    operations = 1
    for i in range(1, n):
        if s[i] != s[i - 1]:
            operations += 1
        
    #State of the program after the  for loop has been executed: `n` is an integer between 1 and 500, `s` is a string of length `n` consisting of lowercase Latin letters, and `operations` is the number of positions where the character in the string differs from the previous character.
    print(operations)
#Overall this is what the function does:The function reads an integer `n` and a string `s` of length `n` from user input, counts the number of positions where consecutive characters in `s` differ, and prints the count. If `n` is 1, the count is 1. If all characters in `s` are the same, the count is also 1.

