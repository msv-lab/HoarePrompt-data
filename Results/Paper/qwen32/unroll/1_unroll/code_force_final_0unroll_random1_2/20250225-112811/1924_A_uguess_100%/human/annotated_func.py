#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^5. For each test case, n and k are integers such that 1 <= n <= 26 and 1 <= k <= 26, and m is an integer such that 1 <= m <= 1000. s is a string of length m consisting only of the first k lowercase English alphabets. The sum of m and the sum of n over all test cases does not exceed 10^6.
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
        
    #State: t is the total number of test cases, n, k, and m are the values from the last test case, s is the string from the last test case, cnt is the final count of complete sets of k distinct characters for the last test case, cur is the final bitmask representing the presence of characters for the last test case, ans is the final constructed string for the last test case.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it checks if a given string can be divided into at least `n` sets of `k` distinct lowercase English alphabets. If possible, it prints "YES". Otherwise, it prints "NO" and constructs a string that includes the minimum required characters to meet the condition, then prints this constructed string.

