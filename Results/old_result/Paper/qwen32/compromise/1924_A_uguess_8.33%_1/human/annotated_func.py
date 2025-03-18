#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^5. For each test case, n, k, and m are integers such that 1 <= n <= 26, 1 <= k <= 26, and 1 <= m <= 1000. The string s is of length m and consists only of the first k lowercase English alphabets. The sum of m and the sum of n over all test cases do not exceed 10^6.
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
        
    #State: `t` iterations of the loop have completed, and for each iteration, the program determines whether the string `s` contains at least `n` sequences of all `k` distinct characters in any order. If it does, it prints 'YES'. If not, it prints 'NO' followed by a constructed string `ans` that consists of the `k`-th letter of the alphabet repeated `cnt` times, the character `tmp` (the highest-indexed character not yet encountered in the last incomplete sequence), and 'a' repeated `n - cnt - 1` times.
#Overall this is what the function does:The function processes multiple test cases, each consisting of integers `n`, `k`, and `m`, and a string `s`. For each test case, it checks if the string `s` contains at least `n` sequences of all `k` distinct characters in any order. If it does, it prints 'YES'. If not, it prints 'NO' followed by a constructed string `ans` that consists of the `k`-th letter of the alphabet repeated `cnt` times, the highest-indexed character not yet encountered in the last incomplete sequence, and 'a' repeated `n - cnt - 1` times.

