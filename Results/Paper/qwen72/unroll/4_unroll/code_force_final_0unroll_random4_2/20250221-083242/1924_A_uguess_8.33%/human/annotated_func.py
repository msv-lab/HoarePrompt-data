#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^5, n is an integer such that 1 <= n <= 26, k is an integer such that 1 <= k <= 26, m is an integer such that 1 <= m <= 1000, and s is a string of length m comprising only of the first k lowercase English alphabets. The sum of m and the sum of n over all test cases does not exceed 10^6.
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
        
    #State: The variables `t`, `n`, `k`, `m`, and `s` retain their initial values for each iteration of the outer loop. The variable `cnt` is reset to 0 and `cur` is reset to 0 at the start of each iteration of the outer loop. After all iterations of the outer loop, the final values of `t`, `n`, `k`, `m`, and `s` remain unchanged, and the loop will have printed 'YES' or 'NO' followed by a string `ans` for each test case.
#Overall this is what the function does:The function `func` processes a series of test cases. For each test case, it reads an integer `n`, an integer `k`, and a string `s` of length `m` (where `m` is provided but not explicitly used in the function). The function checks if the string `s` contains all possible combinations of the first `k` lowercase English alphabets at least `n` times. If it does, the function prints 'YES'. If it does not, the function prints 'NO' followed by a string that represents the missing combination to reach `n` occurrences. The function repeats this process for `t` test cases, where `t` is an integer provided at the beginning of the function call. After processing all test cases, the function terminates without returning any value.

