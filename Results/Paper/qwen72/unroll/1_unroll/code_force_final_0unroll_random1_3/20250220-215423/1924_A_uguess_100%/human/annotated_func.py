#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^5, n is an integer such that 1 <= n <= 26, k is an integer such that 1 <= k <= 26, m is an integer such that 1 <= m <= 1000, and s is a string of length m comprising only of the first k lowercase English alphabets. The sum of m and the sum of n over all test cases does not exceed 10^6.
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
        
    #State: t is an input integer such that 1 <= t <= 10^5, n is an integer such that 1 <= n <= 26, k is an integer such that 1 <= k <= 26, m is an integer such that 1 <= m <= 1000, and s is a string of length m comprising only of the first k lowercase English alphabets. The sum of m and the sum of n over all test cases does not exceed 10^6. The loop has processed all t test cases, and for each test case, it has printed 'YES' if the string s contains at least n distinct subsequences of the first k lowercase English alphabets, otherwise it has printed 'NO' followed by a string that includes the first missing alphabet and the required number of 'a' characters to reach n distinct subsequences.
#Overall this is what the function does:The function reads an integer `t` indicating the number of test cases. For each test case, it reads three integers `n`, `k`, and `m`, and a string `s` of length `m` consisting of the first `k` lowercase English alphabets. The function checks if the string `s` contains at least `n` distinct subsequences of the first `k` alphabets. If it does, the function prints 'YES'. If it does not, the function prints 'NO' followed by a string that includes the first missing alphabet and the required number of 'a' characters to reach `n` distinct subsequences. After processing all `t` test cases, the function concludes.

