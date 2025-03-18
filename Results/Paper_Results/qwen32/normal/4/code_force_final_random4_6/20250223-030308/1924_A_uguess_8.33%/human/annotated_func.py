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
        
    #State: After processing all `t` test cases, for each test case, the output is either "YES" if `cnt` (the number of sequences of `k` distinct characters) is greater than or equal to `n`, or "NO" followed by a constructed string `ans` if `cnt` is less than `n`. The constructed string `ans` consists of the `k`-th letter in the alphabet repeated `cnt` times, concatenated with `tmp` (the last valid character assigned based on `cur`), and then 'a' repeated `n - cnt - 1` times.
#Overall this is what the function does:The function processes multiple test cases, each defined by integers `n`, `k`, and `m`, and a string `s`. For each test case, it checks if there are at least `n` sequences of `k` distinct characters in the string `s`. If so, it outputs "YES". Otherwise, it outputs "NO" followed by a constructed string consisting of the `k`-th letter repeated `cnt` times, a specific character based on the current state, and 'a' repeated `n - cnt - 1` times.

