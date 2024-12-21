#State of the program right berfore the function call: n is an integer such that 1 <= n <= 500, and s is a string of length n consisting of lowercase Latin letters.
def func():
    n = int(input())
    s = input()
    ans = 1
    for i in range(1, n):
        if s[i] != s[i - 1]:
            ans += 1
        
    #State of the program after the  for loop has been executed: `n` is an integer input value where \(1 \leq n \leq 500\), `s` is a string of length `n` consisting of lowercase Latin letters, `ans` is the count of transitions between consecutive characters in the string `s`.
    print(ans)
#Overall this is what the function does:The function `func()` accepts an integer `n` (where \(1 \leq n \leq 500\)) and a string `s` of length `n` consisting of lowercase Latin letters. It then counts the number of transitions (changes) between consecutive characters in the string `s`. A transition is defined as a change in character from one position to the next. If the string starts with a transition (i.e., the first and second characters are different), it is counted as well. The function prints the total count of these transitions.

