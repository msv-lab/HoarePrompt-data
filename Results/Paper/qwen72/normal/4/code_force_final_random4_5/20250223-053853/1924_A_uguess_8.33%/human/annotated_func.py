#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^5, n and k are integers such that 1 <= n <= 26 and 1 <= k <= 26, m is an integer such that 1 <= m <= 1000, and s is a string of length m comprising only of the first k lowercase English alphabets. The sum of m and the sum of n over all test cases does not exceed 10^6.
def func():
    t = int(input())
    for i in range(t):
        n, k, m = map(int, input().split())
        
        s = input()
        
        cnt = 0
        
        cur = 0
        
        for ss in s:
            cur_ss = ord(ss) - ord('a')
            if cur & 1 << cur_ss == 0:
                cur += 1 << cur_ss
            if cur == (1 << k) - 1:
                cnt += 1
                cur = 0
        
        if cnt >= n:
            print('YES')
        else:
            print('NO')
            tmp = ''
            ans = chr(ord('a') + k - 1) * cnt
            for i in range(k):
                if cur & 1 << i == 0:
                    tmp = chr(ord('a') + i)
            ans += tmp
            ans += 'a' * (n - cnt - 1)
            print(ans)
        
    #State: The loop iterates `t` times, and for each iteration, it reads `n`, `k`, and `m` from input, and a string `s` of length `m`. After processing the string `s`, it either prints 'YES' if the count of complete sets of the first `k` alphabets is at least `n`, or prints 'NO' followed by a string that represents the incomplete set and the remaining characters needed to complete `n` sets. The variables `t`, `n`, `k`, `m`, and `s` are reset for each iteration, and the loop does not modify any variables outside its scope.
#Overall this is what the function does:The function reads an integer `t` indicating the number of test cases. For each test case, it reads three integers `n`, `k`, and `m`, followed by a string `s` of length `m` containing only the first `k` lowercase English alphabets. It then processes the string `s` to determine if it contains at least `n` complete sets of the first `k` alphabets. If it does, the function prints 'YES'. If it does not, the function prints 'NO' followed by a string that represents the incomplete set and the remaining characters needed to complete `n` sets. The function does not return any values; it only prints the results.

