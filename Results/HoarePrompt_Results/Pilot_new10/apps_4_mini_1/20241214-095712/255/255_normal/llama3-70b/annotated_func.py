#State of the program right berfore the function call: n is an integer such that 1 <= n <= 500, and s is a string of length n consisting of lowercase Latin letters.
def func():
    n = int(input())
    s = input()
    ans = 1
    for i in range(1, n):
        if s[i] != s[i - 1]:
            ans += 1
        
    #State of the program after the  for loop has been executed: `n` is an integer input within the range 1 to 500, `s` is a string of length `n`, and `ans` is the count of distinct character sequences in `s` starting from an initial value of 1. If `n` is 1, `ans` remains 1. If `n` is greater than 1, `ans` counts transitions between different characters in `s`.
    print(ans)
#Overall this is what the function does:The function accepts an integer `n` (where 1 ≤ n ≤ 500) and a string `s` of length `n` consisting of lowercase Latin letters. It counts and prints the number of distinct consecutive character sequences in `s`. If all characters are the same, it will return 1, as there are no transitions. The function does not return any value but directly prints the result.

