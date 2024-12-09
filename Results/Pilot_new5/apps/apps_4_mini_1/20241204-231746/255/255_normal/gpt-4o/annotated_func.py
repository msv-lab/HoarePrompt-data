#State of the program right berfore the function call: n is an integer such that 1 <= n <= 500, and s is a string of length n consisting of lowercase Latin letters.
def func():
    n = int(input())
    s = input()
    operations = 1
    for i in range(1, n):
        if s[i] != s[i - 1]:
            operations += 1
        
    #State of the program after the  for loop has been executed: `n` is an integer, `s` is a string of length `n`, `operations` is equal to the number of transitions between different characters in the string `s`, and `i` is equal to `n - 1` if the loop executes. If the loop does not execute, then `operations` remains 1.
    print(operations)
#Overall this is what the function does:The function accepts an integer `n` and a string `s` of length `n`, and counts the number of transitions between different characters in `s`, printing the total operations counted. If the string has no transitions (all characters are the same), it still returns 1.

