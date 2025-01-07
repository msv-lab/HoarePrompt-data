#State of the program right berfore the function call: n is an integer such that 1 <= n <= 500, and s is a string of length n consisting only of lowercase Latin letters.
def func():
    n = int(input())
    s = input()
    ans = 1
    for i in range(1, n):
        if s[i] != s[i - 1]:
            ans += 1
        
    #State of the program after the  for loop has been executed: `n` is between 1 and 500, `s` is a string of length `n`, and `ans` is equal to the number of distinct adjacent characters in `s`, plus 1.
    print(ans)
#Overall this is what the function does:The function accepts an integer `n` (where 1 <= n <= 500) and a string `s` of length `n`, consisting only of lowercase Latin letters. It counts the number of distinct adjacent characters in the string `s`, starting with an initial count of 1 to account for the first character. After iterating through the string, if two adjacent characters are different, it increments the count. The result (`ans`) represents the total count of distinct adjacent character groups in the string and is printed out at the end. The function does not handle cases where the input string is empty or where the input does not conform to the expected format, which may result in errors.

