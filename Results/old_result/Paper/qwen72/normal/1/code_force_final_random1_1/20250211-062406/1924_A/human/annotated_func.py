#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^5; for each test case, n, k, and m are integers such that 1 ≤ n ≤ 26, 1 ≤ k ≤ 26, and 1 ≤ m ≤ 1000; s is a string of length m comprising only of the first k lowercase English alphabets. The sum of m and the sum of n over all test cases do not exceed 10^6.
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
        
    #State: After the loop executes all iterations, `t` is an input integer such that 1 ≤ t ≤ 10^5, `i` is `t`, `n` is an input integer, `k` is an input integer, `m` is an input integer, `s` is an input string. The variable `cur` is 0, `cnt` is the total number of times `cur` reached `(1 << k) - 1` during all iterations of the loop. If `cnt` is greater than or equal to `n`, the variable `ans` is a string containing the characters from `s` that caused `cur` to reset to 0. If `cnt` is less than `n`, `ans` is extended by the current value of `tmp` followed by `'a'` repeated `(n - cnt - 1)` times, where `tmp` is the character corresponding to the bit position if the bit at position `i` in `cur` is 0, otherwise `tmp` remains an empty string.
#Overall this is what the function does:The function `func` processes multiple test cases, each defined by integers `n`, `k`, and `m`, and a string `s` of length `m` consisting of the first `k` lowercase English alphabets. For each test case, it checks if the string `s` contains a sequence of characters that collectively cover all `k` distinct alphabets at least `n` times. If such a sequence exists, it prints "YES". Otherwise, it prints "NO" and constructs a string `ans` that includes the missing characters to meet the requirement, appending the necessary characters to ensure the sequence is valid. After processing all test cases, the function terminates.

