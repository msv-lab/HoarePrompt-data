#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^5. For each test case, n and k are positive integers such that 1 ≤ n ≤ 26 and 1 ≤ k ≤ 26, and m is a positive integer such that 1 ≤ m ≤ 1000. Additionally, the sum of m and the sum of n over all test cases does not exceed 10^6. s is a string of length m comprising only the first k lowercase English alphabets.
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
        
    #State: All the characters of the string `s` are concatenated into `ans`, `cnt` is the total length of `s`, `cur` is 0, and `tmp` is 'd'.
#Overall this is what the function does:The function processes multiple test cases, where each test case involves integers t, n, k, m, and a string s. It checks if the string s contains at least n unique substrings of length k. If so, it prints 'YES'. Otherwise, it identifies the missing character needed to form such substrings and constructs a valid output string, then prints 'NO' followed by the constructed string.

