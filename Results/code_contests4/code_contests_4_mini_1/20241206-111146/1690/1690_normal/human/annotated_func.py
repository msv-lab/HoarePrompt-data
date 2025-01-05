#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 10^5), s is a string of length n consisting of lowercase Latin letters, and a is a list of n integers where each integer a_i (1 ≤ a_i ≤ 998244353) corresponds to the ambiguity increase of removing the i-th character of the string s.
def func():
    rstr = lambda : stdin.readline().strip()
    rints = lambda : [int(x) for x in stdin.readline().split()]
    n, s, a, ans, word = int(input()), rstr(), rints(), float('inf'), 'hard'
    for i in range(4):
        be, en, tem = 0, n, 0
        
        cur = 0
        
        for j in range(n):
            if cur == i:
                break
            elif s[j] == word[cur]:
                cur += 1
            be += 1
        
        cur = 3
        
        for j in range(n - 1, -1, -1):
            if cur == i:
                break
            elif s[j] == word[cur]:
                cur -= 1
            en -= 1
        
        for j in range(be, en):
            if s[j] == word[i]:
                tem += a[j]
        
        ans = min(ans, tem)
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `j` is -1, `be` is equal to `n`, `cur` is 0, 1, 2, or 3 based on the last matching, `s` contains `n` characters, `en` is less than or equal to `n`, `tem` is the sum of `a[j]` for indices where `s[j]` equals `word[3]`, and `ans` is the minimum of all calculated `tem` values across iterations.
    print(ans)
#Overall this is what the function does:The function accepts a positive integer `n`, a string `s` of length `n`, and a list `a` of `n` integers. It computes the minimum ambiguity increase by trying to match the string `s` with the word "hard" and calculates the total ambiguity increase for characters in `s` that correspond to the letters in "hard". If a character in `s` matches, it adds the associated ambiguity increase from list `a`. The function returns the minimum total ambiguity increase required to form "hard" from `s`. If "hard" cannot be formed, the function will return infinity, indicating that no valid matches were found.

