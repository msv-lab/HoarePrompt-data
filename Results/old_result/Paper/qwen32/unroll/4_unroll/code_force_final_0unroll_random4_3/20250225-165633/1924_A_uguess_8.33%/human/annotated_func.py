#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^5, for each test case, n, k, and m are integers such that 1 <= n <= 26, 1 <= k <= 26, and 1 <= m <= 1000, s is a string of length m consisting only of the first k lowercase English alphabets, and the sum of m and the sum of n over all test cases does not exceed 10^6.
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
        
    #State: `t` is an input integer, `n`, `k`, `m` are integers as per the last test case, and `s` is the string of length `m` from the last test case.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it checks if a given string `s` contains at least `n` distinct substrings, each containing all `k` unique lowercase English alphabets up to the `k`-th letter. If the condition is met, it prints "YES". Otherwise, it prints "NO" and constructs a string of length `n` using the available characters, ensuring it contains as many distinct substrings with all `k` unique letters as possible, followed by the remaining required characters to meet the length `n`.

