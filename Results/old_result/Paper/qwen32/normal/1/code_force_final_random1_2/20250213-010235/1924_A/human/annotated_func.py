#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^5. For each test case, n, k, and m are integers such that 1 ≤ n ≤ 26, 1 ≤ k ≤ 26, and 1 ≤ m ≤ 1000. The string s is of length m and consists only of the first k lowercase English alphabets. The sum of m and the sum of n over all test cases do not exceed 10^6.
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
        
    #State: After all iterations, `t` remains the same, `n`, `k`, `m`, and `s` reflect the values of the last test case, `cnt` reflects the count of sequences of `k` distinct characters for the last test case, `cur` reflects the bitmask of the last incomplete sequence for the last test case, and `ans` contains the constructed string if `cnt < n` for the last test case.
#Overall this is what the function does:The function processes multiple test cases where each test case consists of integers `n`, `k`, and `m`, and a string `s`. It checks if the string `s` contains at least `n` sequences of `k` distinct characters. If it does, it prints "YES". Otherwise, it prints "NO" and constructs a string by appending a character that completes the last incomplete sequence of distinct characters and additional 'a' characters to meet the requirement of `n` sequences, then prints this constructed string.

