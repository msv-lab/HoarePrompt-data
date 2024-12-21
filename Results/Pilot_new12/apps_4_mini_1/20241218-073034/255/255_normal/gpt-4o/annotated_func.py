#State of the program right berfore the function call: n is a positive integer such that 1 <= n <= 500, and s is a string of length n consisting of lowercase Latin letters.
def func():
    n = int(input())
    s = input()
    operations = 1
    for i in range(1, n):
        if s[i] != s[i - 1]:
            operations += 1
        
    #State of the program after the  for loop has been executed: `n` is a positive integer such that \( 1 \leq n \leq 500 \), `s` is a string of length `n`, `operations` is equal to the number of transitions between different consecutive characters in `s` plus 1.
    print(operations)
#Overall this is what the function does:The function reads a positive integer `n` (with 1 ≤ n ≤ 500) and a string `s` of length `n` consisting of lowercase Latin letters. It counts the number of transitions between different consecutive characters in the string `s`, starting the count at 1 for the first character. The final output is the total count of operations, which represents the number of unique character segments in the string, as well as accounting for edge cases such as when all characters are the same or when `n` is 1, where it will still return 1. The function does not return any value; it solely prints the result.

