#State of the program right berfore the function call: There is an integer n (1 ≤ n ≤ 500,000) representing the number of names, followed by n non-empty strings each consisting of lowercase Latin letters, where the length of each string does not exceed 10 characters.
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
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `dyn` is a 26x26 matrix with values reflecting the maximum lengths of strings inputted that start with each letter and end with each letter.
    ans = max([dyn[i][i] for i in range(26)])
    print(ans)
#Overall this is what the function does:The function accepts an integer `n` representing the number of non-empty strings, followed by `n` strings consisting of lowercase Latin letters (with a maximum length of 10 characters each). It constructs a 26x26 matrix to track the maximum lengths of strings that start and end with each letter. After processing all strings, it calculates and prints the maximum length of a string that starts and ends with the same letter. The function does not handle cases where `n` is zero or negative, as it assumes `n` is always a positive integer within the specified range.

