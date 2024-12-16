#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 500, and s is a string of length n consisting of lowercase Latin letters.
def func():
    n = int(input())
    s = input()
    ans = 1
    for i in range(1, n):
        if s[i] != s[i - 1]:
            ans += 1
        
    #State of the program after the  for loop has been executed: `s` is the string input by the user, `n` is the length of the string `s`, `ans` is the count of positions where consecutive characters in the string `s` are different.
    print(ans)
#Overall this is what the function does:The function reads an integer `n` and a string `s` of length `n` consisting of lowercase Latin letters. It counts the number of positions where consecutive characters in the string `s` are different and prints the count.

