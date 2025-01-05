#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 10^5, s is a string of length n consisting of lowercase Latin letters, and a is a list of n integers where each integer a_i satisfies 1 ≤ a_i ≤ 998244353.
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
        
    #State of the program after the  for loop has been executed: `n` is an integer, `i` is 3, `be` is less than or equal to `en`, `cur` is either 0 or -1 depending on matching conditions, `tem` is the sum of `a[j]` for all indices `j` from `be` to `en - 1` where `s[j]` equals `word[i]`, `ans` is the minimum of its final value and `tem`.
    print(ans)
#Overall this is what the function does:The function accepts an integer `n`, a string `s` of length `n`, and a list `a` of `n` integers. It calculates the minimum sum of integers from `a` corresponding to characters in `s` that match the word "hard" when evaluated from the beginning and end of the string. The function prints the minimum sum found for the specified conditions but does not return any value.

