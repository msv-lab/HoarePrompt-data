#State of the program right berfore the function call: n is a positive integer such that 1 <= n <= 500, and s is a string of length n consisting only of lowercase Latin letters.
def func():
    n = int(input())
    s = input()
    ans = 1
    for i in range(1, n):
        if s[i] != s[i - 1]:
            ans += 1
        
    #State of the program after the  for loop has been executed: `ans` is the number of distinct consecutive characters in `s`, and `s` is the user-entered string. If `n` is less than or equal to 1, then `ans` is 1.
    print(ans)
#Overall this is what the function does:The function accepts a positive integer `n` (where 1 <= n <= 500) and a string `s` consisting of lowercase Latin letters, then calculates and prints the number of distinct consecutive characters in the string `s`. The function does not handle the case where the length of the string is less than `n` or where `n` is not within the specified range, and it directly takes user input for `n` and `s`.

