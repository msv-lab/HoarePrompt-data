#State of the program right berfore the function call: The input consists of an integer n, where 1 <= n <= 500, and a string s of length n, consisting only of lowercase Latin letters.
def func():
    n = int(input())
    s = input()
    ans = 1
    for i in range(1, n):
        if s[i] != s[i - 1]:
            ans += 1
        
    #State of the program after the  for loop has been executed: `n` is an integer where `1 <= n <= 500`, `s` is the input string of length `n`, `i` is `n-1`, and `ans` is the number of segments of continuous characters in `s`, which is at least `1` and increases by `1` for each transition to a different character in `s`.
    print(ans)
#Overall this is what the function does:The function accepts an integer `n` and a string `s` of length `n` as inputs from the user, counts the number of segments of continuous characters in `s`, and prints this count, which is at least 1 and increases by 1 for each transition to a different character in `s`.

