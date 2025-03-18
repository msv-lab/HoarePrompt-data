#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^5. For each test case, n and k are integers such that 1 <= n <= 26 and 1 <= k <= 26, and m is an integer such that 1 <= m <= 1000. The string s is of length m and consists only of the first k lowercase English alphabets. The sum of m and the sum of n over all test cases do not exceed 10^6.
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
        
    #State: `t` is 0; `n`, `k`, `m`, and `s` are the values from the last iteration; `cnt` is the number of complete sequences of `k` unique characters found in the last `s`; `cur` is 0 if the last sequence was complete, otherwise it holds the bitmask of the last incomplete sequence; `ans` contains the last character of each complete sequence of `k` unique characters, or is extended with the smallest missing character and enough 'a's to reach `n` sequences if `cnt` is less than `n`.
#Overall this is what the function does:The function processes multiple test cases, each defined by integers `n`, `k`, and `m`, and a string `s`. For each test case, it checks if the string `s` contains at least `n` non-overlapping sequences of `k` unique characters. If it does, it prints "YES". Otherwise, it prints "NO" and constructs a string by appending the smallest missing character and enough 'a's to reach `n` sequences, then prints this constructed string.

