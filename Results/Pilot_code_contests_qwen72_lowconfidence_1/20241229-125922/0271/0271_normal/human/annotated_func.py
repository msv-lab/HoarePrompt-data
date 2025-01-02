#State of the program right berfore the function call: n is an integer where 1 ≤ n ≤ 5·10^5, and the list of names is a list of n strings, each string consisting of lowercase Latin letters and having a length between 1 and 10 characters.
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
        
    #State of the program after the  for loop has been executed: `n` is a non-negative integer, `i` is `n-1` if `n > 0` or undefined if `n = 0`, the list of names is a list of `n` strings, each string consisting of lowercase Latin letters and having a length between 1 and 10 characters, `__author__` is 'Rikishi', `dyn` is a 26x26 list of lists where each element is 0 except for those elements `dyn[j][last]` which are updated to `dyn[j][first] + len(s)` for all `j` where `dyn[j][first] > 0` and for each string `s` in the list of names, `first` is `ord(s[0]) - ord('a')`, `last` is `ord(s[-1]) - ord('a')`, and `dyn[first][last]` is the maximum of its original value and `len(s)`. If `n = 0`, `dyn` remains a 26x26 list of lists where each element is 0.
    ans = max([dyn[i][i] for i in range(26)])
    print(ans)
#Overall this is what the function does:The function reads an integer `n` and a list of `n` strings from the standard input, where each string consists of lowercase Latin letters and has a length between 1 and 10 characters. It then constructs a 26x26 matrix `dyn` where each element represents the maximum possible length of a chain of strings that can be formed such that the last character of one string matches the first character of the next string. The function finally prints the maximum value in the diagonal of this matrix, which represents the longest such chain that can be formed using the given strings. If no valid chains exist, it prints 0. The function does not return any value. Edge cases include when `n` is 0, in which case the function initializes the matrix `dyn` to a 26x26 zero matrix and prints 0.

