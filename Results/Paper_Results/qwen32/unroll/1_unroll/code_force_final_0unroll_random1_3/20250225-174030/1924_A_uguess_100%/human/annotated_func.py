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
        
    #State: `t` is an integer such that 1 <= t <= 10^5, `n`, `k`, and `m` are integers reflecting the values of the last test case, `s` is a string of length `m` reflecting the string of the last test case, `cnt` is an integer representing the count of valid substrings in the last test case, `cur` is an integer representing the bitmask of characters seen in the last test case, and `ans` is a string constructed based on the conditions of the last test case.
#Overall this is what the function does:The function processes multiple test cases, each defined by integers `n`, `k`, and `m`, and a string `s`. For each test case, it checks if there are at least `n` distinct substrings of `s` that contain all `k` unique characters. If so, it outputs 'YES'. Otherwise, it outputs 'NO' and constructs a string that includes the missing characters and additional 'a's to meet the requirement of `n` substrings.

