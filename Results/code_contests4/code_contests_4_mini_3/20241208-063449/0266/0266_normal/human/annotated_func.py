#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 500000) representing the number of abbreviated names, followed by n non-empty sequences of lowercase Latin letters, each representing an abbreviated name with a length not exceeding 10 characters.
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
        
    #State of the program after the  for loop has been executed: `n` is a positive integer (1 ≤ n ≤ 500000), `dyn` is a 26x26 list where each element `dyn[first][last]` represents the maximum length of strings that start with the character corresponding to `first` and end with the character corresponding to `last`.
    ans = max([dyn[i][i] for i in range(26)])
    print(ans)
#Overall this is what the function does:The function accepts a positive integer `n` (1 ≤ n ≤ 500000) that represents the number of abbreviated names, followed by `n` non-empty sequences of lowercase Latin letters. It constructs a 26x26 matrix `dyn` where each entry `dyn[first][last]` holds the maximum length of strings that start with the character corresponding to `first` and end with the character corresponding to `last`. Finally, it calculates and prints the maximum length of strings that both start and end with the same character (i.e., `dyn[i][i]` for each character), effectively finding the longest abbreviated name that starts and ends with the same letter. The function does not handle cases where `n` is 0 or negative, as it assumes valid input based on the constraints.

