#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^5. For each test case, n and k are positive integers such that 1 ≤ n ≤ 26 and 1 ≤ k ≤ 26, and m is a positive integer such that 1 ≤ m ≤ 1000. The string s consists of only the first k lowercase English alphabets, and the sum of m and the sum of n over all test cases does not exceed 10^6.
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
        
    #State: The output state depends on the input values provided during each iteration of the loop. For each input, the program processes a string `s` and checks if it contains at least `n` substrings where each substring has exactly `k` distinct characters. If such substrings exist, it prints 'YES'. Otherwise, it prints 'NO' followed by a specific string `ans` constructed based on the bits set in `cur`. The final output is a combination of 'YES'/'NO' and the constructed string `ans` for each input.
#Overall this is what the function does:The function processes multiple test cases, each consisting of integers \( t \), \( n \), \( k \), \( m \), and a string \( s \). For each test case, it checks if the string \( s \) contains at least \( n \) substrings where each substring has exactly \( k \) distinct characters. If such substrings exist, it prints 'YES'. Otherwise, it prints 'NO' followed by a specific string \( ans \) constructed based on the bits set in the variable \( cur \). The final output is a combination of 'YES'/'NO' and the constructed string \( ans \) for each test case.

