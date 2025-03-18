#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^5. For each test case, n and k are integers such that 1 ≤ n ≤ 26 and 1 ≤ k ≤ 26, and m is an integer such that 1 ≤ m ≤ 1000. The string s is a string of length m comprising only the first k lowercase English alphabets.
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
        
    #State: After executing the loop, the value of `t` will be decremented by 1 for each iteration, and for each input, either "YES" or "NO" followed by a string `ans` will be printed. The string `ans` is constructed based on the conditions within the loop.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads integers \( t \), \( n \), \( k \), and \( m \), and a string \( s \). It then checks if the string \( s \) contains at least \( n \) unique substrings of length \( k \). If so, it prints "YES". Otherwise, it prints "NO" followed by a constructed string based on the remaining characters needed to meet the condition. The function does not return any value but prints the results for each test case.

