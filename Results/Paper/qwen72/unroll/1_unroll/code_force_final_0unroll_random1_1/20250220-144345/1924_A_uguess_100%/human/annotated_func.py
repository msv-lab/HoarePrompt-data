#State of the program right berfore the function call: t is an integer where 1 <= t <= 10^5, n is an integer where 1 <= n <= 26, k is an integer where 1 <= k <= 26, m is an integer where 1 <= m <= 1000, and s is a string of length m comprising only of the first k lowercase English alphabets. The sum of m and the sum of n over all test cases does not exceed 10^6.
def func():
    t = int(input())
    for i in range(t):
        n, k, m = map(int, input().split())
        
        s = input()
        
        cnt = 0
        
        cur = 0
        
        ans = ''
        
        for ss in s:
            cur_ss = ord(ss) - ord('a')
            if cur & 1 << cur_ss == 0:
                cur += 1 << cur_ss
            if cur == (1 << k) - 1:
                cnt += 1
                cur = 0
                ans += ss
        
        if cnt >= n:
            print('YES')
        else:
            print('NO')
            tmp = ''
            for i in range(k):
                if cur & 1 << i == 0:
                    tmp = chr(ord('a') + i)
                    break
            ans += tmp
            ans += 'a' * (n - cnt - 1)
            print(ans)
        
    #State: t is an input integer where 1 <= t <= 10^5, n is an integer where 1 <= n <= 26, k is an integer where 1 <= k <= 26, m is an integer where 1 <= m <= 1000, and s is a string of length m comprising only of the first k lowercase English alphabets. The sum of m and the sum of n over all test cases does not exceed 10^6. The loop has processed all t test cases, and for each test case, either 'YES' has been printed if the required number of complete sets of k characters was found in the string s, or 'NO' followed by a modified string ans has been printed if the required number of sets was not found. The modified string ans contains the first character that was missing to complete the set, followed by 'a' repeated (n - cnt - 1) times, where cnt is the number of complete sets found in s.
#Overall this is what the function does:The function `func` processes up to `t` test cases, where each test case involves an integer `n`, an integer `k`, and a string `s` of length `m`. The string `s` consists only of the first `k` lowercase English alphabets. For each test case, the function checks if the string `s` contains at least `n` complete sets of all `k` distinct characters. If it does, the function prints 'YES'. If it does not, the function prints 'NO' followed by a modified string `ans` that includes the first missing character to complete a set, followed by 'a' repeated `(n - cnt - 1)` times, where `cnt` is the number of complete sets found in `s`. After processing all test cases, the function concludes.

