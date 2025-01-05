#State of the program right berfore the function call: **Precondition**: 
- n is an integer such that 1 ≤ n ≤ 10^5.
- s is a string of length n consisting of lowercase Latin letters.
- a_i is an integer such that 1 ≤ a_i ≤ 998244353 for each i where 1 ≤ i ≤ n.
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
        
    #State of the program after the  for loop has been executed: At the end of the loop, `tem` will be the sum of values in `a` corresponding to the characters in `s` that match 'hard'. `ans` will be the minimum sum found in `tem` after all iterations of the loop. All other variables remain the same as their initial values.
    print(ans)
#Overall this is what the function does:Functionality: The function `func` reads input values for `n`, `s`, and `a`, initializes `ans` to infinity, and `word` to 'hard'. It then iterates through different configurations of the word 'hard' within the string `s` to calculate the minimum sum of values in `a` corresponding to the characters that match 'hard'. Finally, it prints the minimum sum found. The function does not accept any parameters and does not return any value. However, it misses handling the case where the characters of 'hard' are not found in the string `s`.

