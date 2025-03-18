#State of the program right berfore the function call: n is a positive integer between 1 and 500 (inclusive), and s is a string of length n consisting of lowercase Latin letters.
def func():
    n = int(input())
    s = input()
    operations = 1
    for i in range(1, n):
        if s[i] != s[i - 1]:
            operations += 1
        
    #State of the program after the  for loop has been executed: `s` is the input string, `n` is the input integer, `i` is `n-1`, and `operations` is 1 plus the number of transitions between different consecutive characters in the first `n-1` characters of `s`. If `n` is 1 or less, the loop does not execute, and `operations` remains 1, `i` is undefined in the context of the loop's execution but is determined by the loop's range which would not have executed, and `s` remains the input string.
    print(operations)
#Overall this is what the function does:The function takes an integer `n` and a string `s` as input from the user, calculates the number of transitions between different consecutive characters in the string `s`, and prints this count. If `n` is 1 or less, it prints 1. The function does not check if `n` is within the range of 1 to 500 or if `s` is a string of length `n` consisting of lowercase Latin letters.

