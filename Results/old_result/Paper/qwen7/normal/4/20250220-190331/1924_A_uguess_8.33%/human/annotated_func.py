#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^5. For each test case, n and k are positive integers such that 1 ≤ n ≤ 26 and 1 ≤ k ≤ 26, and m is a positive integer such that 1 ≤ m ≤ 1000. The string s in each test case consists only of the first k lowercase English alphabets, and the sum of m and the sum of n over all test cases does not exceed 10^6.
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
        
    #State: After the loop executes all iterations, `cnt` will be the total count of valid substrings of length `k` found in the string `s`, where each character's bit in the substring matches the corresponding bit in `cur`. `cur` will be reset to 0, and `cnt` will contain the final count. If `cnt` is less than `n`, then `tmp` will be 'e', `ans` will be a string consisting of `cnt` characters, each character being `chr(ord('a') + k - 1)` followed by 'a' repeated `n - cnt - 1` times, and `k` will retain its initial state.
#Overall this is what the function does:The function processes multiple test cases, each containing integers \(t\), \(n\), \(k\), and \(m\), along with a string \(s\) consisting of the first \(k\) lowercase English alphabets. For each test case, it checks if there are at least \(n\) valid substrings of length \(k\) in \(s\) where each character's bit in the substring matches the corresponding bit in a bitmask \(cur\). If the count of such substrings is at least \(n\), it prints 'YES'. Otherwise, it prints 'NO' followed by a constructed string \(ans\) consisting of \(cnt\) characters, each being the character at position \(k-1\) in the alphabet, followed by 'a' repeated \(n - cnt - 1\) times.

