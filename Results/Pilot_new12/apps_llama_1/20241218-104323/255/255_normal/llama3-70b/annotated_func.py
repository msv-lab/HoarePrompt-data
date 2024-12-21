#State of the program right berfore the function call: The input consists of two lines, the first line contains an integer n, where 1 <= n <= 500, representing the length of the string s, and the second line contains the string s, a sequence of n lowercase Latin letters.
def func():
    n = int(input())
    s = input()
    ans = 1
    for i in range(1, n):
        if s[i] != s[i - 1]:
            ans += 1
        
    #State of the program after the  for loop has been executed: `n` is an integer between 1 and 500, `s` is an input string, `ans` is 1 plus the number of transitions between different characters in the first `n-1` characters of `s`, `i` is `n-1` if the loop executed, otherwise `i` is not defined, but the initial state had `n` and `s`, so in all cases `n` is between 1 and 500 and `s` remains the same input string.
    print(ans)
#Overall this is what the function does:The function processes two lines of input: an integer n and a string s of length n, consisting of lowercase Latin letters, and returns the total number of transitions between different characters in the string s plus one, effectively counting the number of distinct character sequences in s, including handling edge cases where n is 1 (in which case it returns 1) or s is a string of the same character repeated (in which case it also returns 1), and it does not modify the input variables n and s, but instead uses them to compute and print the result, which is based solely on the transitions between characters in s.

