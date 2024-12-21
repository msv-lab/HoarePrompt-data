#State of the program right berfore the function call: n is a positive integer such that 1 <= n <= 500, and s is a string of length n consisting only of lowercase Latin letters.
def func():
    n = int(input())
    s = input()
    ans = 1
    for i in range(1, n):
        if s[i] != s[i - 1]:
            ans += 1
        
    #State of the program after the  for loop has been executed: `n` is a positive integer such that 1 <= `n` <= 500; `s` is a string of length `n` consisting only of lowercase Latin letters; `ans` is the number of distinct adjacent character groups in `s`.
    print(ans)
#Overall this is what the function does:The function reads an integer `n` and a string `s` of length `n` consisting of lowercase Latin letters from user input. It calculates and prints the number of distinct adjacent character groups in the string `s`. Each group is formed by consecutive identical characters. For instance, in the string "aaabbc", there are three groups: "aaa", "bb", and "c". The function does not accept parameters or return a value directly. It assumes valid input based on the given constraints but does not handle potential edge cases such as invalid input or empty strings.

