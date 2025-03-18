#State of the program right berfore the function call: n is an integer such that 1 <= n <= 500, and s is a string of length n consisting of lowercase Latin letters.
def func():
    n = int(input())
    s = input()
    ans = 1
    for i in range(1, n):
        if s[i] != s[i - 1]:
            ans += 1
        
    #State of the program after the  for loop has been executed: `s` is the input string, `n` is the input integer, `i` is `n-1`, and `ans` is `1` plus the number of transitions between different characters in `s`.
    print(ans)
#Overall this is what the function does:The function reads an integer `n` and a string `s` of length `n` consisting of lowercase Latin letters from the user, counts the number of transitions between different characters in `s` and prints the result, which is `1` plus the number of transitions. It does not return any value. The function assumes that the input string `s` only contains lowercase Latin letters and that the input integer `n` is between 1 and 500 (inclusive), but it does not validate these assumptions. If the input string `s` is empty or contains non-lowercase Latin letters, or if the input integer `n` is outside the specified range, the function's behavior is not defined. After the function concludes, the program's state is that it has printed the count of character transitions in the input string `s`, and the input variables `n` and `s` have been consumed.

