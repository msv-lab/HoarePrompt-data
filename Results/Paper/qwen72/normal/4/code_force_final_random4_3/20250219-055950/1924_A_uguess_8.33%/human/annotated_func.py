#State of the program right berfore the function call: t is a positive integer (1 ≤ t ≤ 10^5), n and k are positive integers (1 ≤ n, k ≤ 26), m is a positive integer (1 ≤ m ≤ 1000), and s is a string of length m comprising only the first k lowercase English alphabets. The sum of m and the sum of n over all test cases does not exceed 10^6.
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
        
    #State: `t` is 0, `i` is the number of iterations that have been completed, `n` and `k` are the final input integers from the last iteration, `m` is the final input integer from the last iteration, `s` is the final input string from the last iteration, `cnt` is the number of times the loop has set all bits from 0 to `k-1` in `cur` to 1 for the last iteration, and `cur` is the final value of the bitwise representation after processing all characters in `s` for the last iteration. If `cur` was set to `(1 << k) - 1` at any point, it was reset to 0, and `cnt` was incremented. If `cnt` is greater than or equal to `n`, the current value of `cnt` remains unchanged and `ans` is 'YES'. Otherwise, `ans` is a string consisting of `cnt` occurrences of the character `chr(ord('a') + k - 1)` followed by `tmp` if the bit at position `k-1` in `cur` is 0, otherwise `ans` remains the same, and `ans` is now extended by `n - cnt - 1` occurrences of the character 'a'.
#Overall this is what the function does:The function `func` processes a series of test cases. For each test case, it reads three integers `n`, `k`, and `m`, and a string `s` of length `m` consisting of the first `k` lowercase English alphabets. It then checks if the string `s` can be divided into `n` substrings, each containing all `k` distinct characters. If it can, the function prints 'YES'. If it cannot, the function prints 'NO' followed by a constructed string that represents the closest possible valid substring to meet the condition, padded with additional characters as needed. After processing all test cases, the function concludes, and the final state includes `t` being 0, `i` being the total number of test cases processed, and the last values of `n`, `k`, `m`, `s`, `cnt`, and `cur` from the final test case.

