#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^5. For each test case, n and k are integers such that 1 ≤ n ≤ 26 and 1 ≤ k ≤ 26, and m is an integer such that 1 ≤ m ≤ 1000. The string s is a string of length m comprising only the first k lowercase English alphabets. It is guaranteed that the sum of m and the sum of n over all test cases does not exceed 10^6.
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
        
    #State: All characters of the string `s` have been processed, `cur` is reset to 0, `cnt` is equal to the total number of times `cur` reached \(2^k - 1\), and `ans` is the original string `s` concatenated with itself `t` times. If `cnt` is greater than or equal to `n`, `ans` remains unchanged. Otherwise, `ans` is the original string `s` concatenated with itself `t` times followed by 'a' repeated `n - cnt - 1` times.
#Overall this is what the function does:The function processes multiple test cases, each defined by integers \( t \), \( n \), \( k \), and \( m \), and a string \( s \). For each test case, it checks if the string \( s \) contains at least \( n \) unique substrings of length \( k \). If so, it prints "YES"; otherwise, it prints "NO" followed by a modified version of \( s \) that includes additional 'a' characters to meet the requirement of \( n \) unique substrings. The function ultimately prints the result for each test case.

