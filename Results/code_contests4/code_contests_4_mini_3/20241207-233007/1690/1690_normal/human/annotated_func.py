#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 10^5, s is a string of length n consisting of lowercase Latin letters, and a is a list of n integers where each integer a_i (1 ≤ a_i ≤ 998244353) corresponds to the ambiguity associated with the i-th character in the string.
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
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 ≤ `n` ≤ 10^5; `ans` is the minimum sum of `a[j]` values for all valid indices `j` where `s[j]` matches `word[i]` over all iterations of `i`, `be` is the starting index for the inner forward loop, `en` is the final index for the inner backward loop, and `tem` is the sum of `a[j]` values within the range from `be` to `en - 1` for each respective `i`.
    print(ans)
#Overall this is what the function does:The function accepts an integer `n`, a string `s` of length `n`, and a list of integers `a` of length `n`. It calculates the minimum sum of values from `a` corresponding to indices in `s` that match the characters of the word "hard". The function iterates through each character of "hard", determining ranges in `s` to count the ambiguity values from `a`, and returns the smallest sum found. If no valid characters match, it returns infinity as the minimum sum.

