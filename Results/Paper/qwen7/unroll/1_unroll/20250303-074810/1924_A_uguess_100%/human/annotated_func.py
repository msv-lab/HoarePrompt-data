#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^5. For each test case, n and k are positive integers such that 1 ≤ n ≤ 26 and 1 ≤ k ≤ 26, and m is a positive integer such that 1 ≤ m ≤ 1000. Additionally, s is a string of length m comprising only the first k lowercase English alphabets. The sum of m and the sum of n over all test cases does not exceed 10^6.
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
        
    #State: After all iterations of the loop, the variable `t` will be reduced to an input integer, `n`, `k`, and `m` will be set to values entered by the user, `s` will contain a string entered by the user, and `ans` will either contain a string that satisfies the conditions or will be constructed based on the last iteration's state if the conditions are not met. If `cnt` (the count of valid substrings) is greater than or equal to `n`, `ans` will contain the constructed string with 'YES' printed. Otherwise, `ans` will contain a specific constructed string with 'NO' printed.
#Overall this is what the function does:The function processes multiple test cases, each consisting of integers \( t \), \( n \), \( k \), and \( m \), and a string \( s \). It checks if the string \( s \) contains at least \( n \) valid substrings, where a valid substring is defined as one that includes all \( k \) distinct characters. If the condition is met, it prints 'YES' followed by the string \( s \). If not, it constructs a new string starting with 'NO', followed by the missing character and 'a' repeated \( n - cnt - 1 \) times, then prints the result.

