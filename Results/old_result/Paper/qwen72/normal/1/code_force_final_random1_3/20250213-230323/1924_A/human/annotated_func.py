#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^5, representing the number of test cases. For each test case, n is an integer where 1 ≤ n ≤ 26, k is an integer where 1 ≤ k ≤ 26, and m is an integer where 1 ≤ m ≤ 1000. The string s is of length m and consists only of the first k lowercase English alphabets. The sum of m and the sum of n over all test cases do not exceed 10^6.
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
        
    #State: After the loop executes all the iterations, `t` is 0, `i` is `t-1` (which would be -1 since `t` is 0), `n`, `k`, and `m` are the final input integers for the last test case, `s` is the final input string for the last test case, `cnt` is the total number of times the condition `cur == (1 << k) - 1` was met during the last test case, `ans` is the final string constructed during the last test case, and `cur` is the final bitmask value after processing all characters in the last test case. If `cnt` is greater than or equal to `n`, the program prints "YES". Otherwise, it prints "NO" followed by the string `ans` concatenated with `tmp` (if `tmp` is not an empty string) and `'a'` repeated `(n - cnt - 1)` times.
#Overall this is what the function does:The function `func` processes multiple test cases, each defined by parameters `n`, `k`, `m`, and a string `s`. For each test case, it checks if the string `s` can be partitioned into `n` substrings such that each substring contains all `k` distinct characters. If it can, the function prints "YES". If it cannot, the function prints "NO" followed by a modified version of the string `s` that includes additional characters to meet the requirement. The function reads inputs from standard input and prints results to standard output. After processing all test cases, the function terminates.

