#State of the program right berfore the function call: n is an integer such that 1 <= n <= 500, and s is a string of length n consisting only of lowercase Latin letters.
def func():
    n = int(input())
    s = input()
    ans = 1
    for i in range(1, n):
        if s[i] != s[i - 1]:
            ans += 1
        
    #State of the program after the  for loop has been executed: `s` is an input string of length `n`, `ans` is equal to the number of distinct adjacent characters in `s`, and `n` is between 1 and 500.
    print(ans)
#Overall this is what the function does:The function reads an integer `n` and a string `s` of length `n` consisting of lowercase Latin letters from user input. It then counts the number of distinct adjacent characters in the string `s` and prints this count. The function accepts no parameters directly but relies on user input for its data. If `n` is 1, the output will always be `1`, since a single character has no adjacent characters to compare. The function does not handle any errors related to input, such as invalid integer input or string length mismatches.

