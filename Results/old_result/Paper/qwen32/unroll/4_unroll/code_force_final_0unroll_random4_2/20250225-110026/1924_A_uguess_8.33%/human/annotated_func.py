#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^5. For each test case, n, k, and m are integers such that 1 <= n <= 26, 1 <= k <= 26, and 1 <= m <= 1000. s is a string of length m consisting only of the first k lowercase English alphabets. The sum of m and the sum of n over all test cases do not exceed 10^6.
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
        
    #State: `t` remains the same, `n`, `k`, `m`, `s` are from the last test case, `cnt` is the count of segments with all `k` distinct characters from the last test case, `cur` is the bitmask of characters in the last segment of the last test case, `tmp` and `ans` are constructed based on the last test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of integers `n`, `k`, and `m`, and a string `s`. For each test case, it checks if the string `s` contains at least `n` segments where each segment includes all `k` distinct characters from the first `k` lowercase English alphabets. If such segments exist, it prints 'YES'. Otherwise, it prints 'NO' followed by a constructed string that includes the maximum number of segments with all `k` distinct characters and additional characters to meet the requirement of `n` segments.

