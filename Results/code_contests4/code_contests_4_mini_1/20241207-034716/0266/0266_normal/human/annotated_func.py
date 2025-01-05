#State of the program right berfore the function call: The input consists of an integer n (1 ≤ n ≤ 5·10^5) followed by n non-empty strings, each string being an abbreviated name of lowercase Latin letters with a length not exceeding 10 characters.
def func():
    __author__ = 'Rikishi'
    n = int(raw_input())
    dyn = [([0] * 26) for i in range(26)]
    for i in range(n):
        s = raw_input()
        
        first = ord(s[0]) - ord('a')
        
        last = ord(s[-1]) - ord('a')
        
        for j in range(26):
            if dyn[j][first] > 0:
                dyn[j][last] = dyn[j][first] + len(s)
        
        dyn[first][last] = max(dyn[first][last], len(s))
        
    #State of the program after the  for loop has been executed: `__author__` is 'Rikishi', `n` is a non-negative integer, `dyn` is a 26x26 list where `dyn[first][last]` is the maximum length of strings that start with the character corresponding to `first` and end with the character corresponding to `last`.
    ans = max([dyn[i][i] for i in range(26)])
    print(ans)
#Overall this is what the function does:The function accepts an integer `n` followed by `n` non-empty strings, each consisting of lowercase Latin letters. It calculates a 26x26 matrix (`dyn`) that tracks the maximum length of strings that start with a specific character and end with another. Finally, it outputs the maximum length of strings that start and end with the same character. If no such strings exist, the output will be 0. The function does not explicitly return any value; instead, it directly prints the result.

