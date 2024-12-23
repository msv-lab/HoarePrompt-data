#State of the program right berfore the function call: The input consists of two lines, the first line contains a positive integer n (1 <= n <= 500), and the second line contains a string s of length n consisting of lowercase Latin letters.
def func():
    n = int(input())
    s = input()
    operations = 1
    for i in range(1, n):
        if s[i] != s[i - 1]:
            operations += 1
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `s` is the input string of length `n`, `operations` is 1 plus the number of transitions between different characters in `s`, and `i` is `n-1`.
    print(operations)
#Overall this is what the function does:The function reads two lines of input from the user, where the first line is a positive integer `n` and the second line is a string `s` of length `n` consisting of lowercase Latin letters. It then calculates the number of transitions between different characters in the string `s` and prints this count plus one. The function does not return any value, but instead outputs the result directly to the console. The state of the program after execution will have `n` and `s` stored in memory, with `n` being the length of `s` and the output being the total number of transitions between different characters in `s` plus one, which effectively counts the total number of distinct character sequences or groups in `s`. The function does not handle cases where the input may not match the expected format (e.g., non-integer or non-string inputs), and it assumes that the length of the string `s` will always match the integer `n` provided in the first line.

