#State of the program right berfore the function call: n is a positive integer such that 1 <= n <= 500, and s is a string of length n consisting of lowercase Latin letters.
def func():
    n = int(input())
    s = input()
    ans = 1
    for i in range(1, n):
        if s[i] != s[i - 1]:
            ans += 1
        
    #State of the program after the  for loop has been executed: `n` is a positive integer (1 <= `n` <= 500), `s` is a string of length `n`, `ans` is the count of distinct adjacent characters in `s`.
    print(ans)
#Overall this is what the function does:The function accepts a positive integer `n` (1 <= n <= 500) and a string `s` of length `n` consisting of lowercase Latin letters. It counts the number of distinct adjacent characters in the string `s` and prints this count. The function does not return any value; it only prints the result to standard output.

