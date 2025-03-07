#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^5. For each test case, n, k, and m are integers such that 1 <= n <= 26, 1 <= k <= 26, and 1 <= m <= 1000. s is a string of length m consisting only of the first k lowercase English alphabets. The sum of m and the sum of n over all test cases do not exceed 10^6.
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
        
    #State: `n`, `k`, `m`, and `s` are the values from the last test case; `cnt` is the number of complete sequences of `k` unique characters found in `s`; `cur` is the bitmask representing the last set of characters seen before the loop ended; `ans` is the constructed string if `cnt` is less than `n`.
#Overall this is what the function does:The function processes multiple test cases where each test case consists of integers `n`, `k`, and `m`, and a string `s` of length `m` using only the first `k` lowercase English alphabets. For each test case, it checks if the string `s` contains at least `n` disjoint sequences of all `k` unique characters. If it does, it prints "YES". If not, it prints "NO" and constructs a string by appending a missing character and additional 'a' characters to meet the requirement, then prints the constructed string.

