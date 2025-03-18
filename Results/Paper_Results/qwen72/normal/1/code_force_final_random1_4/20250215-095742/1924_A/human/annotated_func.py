#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^5, representing the number of test cases. For each test case, n is an integer such that 1 ≤ n ≤ 26, k is an integer such that 1 ≤ k ≤ 26, and m is an integer such that 1 ≤ m ≤ 1000. The string s is of length m and consists only of the first k lowercase English alphabets. The sum of m and the sum of n over all test cases do not exceed 10^6.
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
        
    #State: `t` is 0, `i` is `t` (which is 0), `n`, `k`, and `m` are the last input integers for the final test case, `s` is the last input string for the final test case, `cnt` is the total number of times `cur` has reached `(1 << k) - 1` across all test cases, `ans` is the final concatenated string for the last test case, and `cur` is the final bitmask representing the characters seen in the last sequence of the last test case. If `cnt` is greater than or equal to `n` for the last test case, `ans` contains the characters from `s` that caused `cur` to reset to 0. If `cnt` is less than `n`, `ans` is extended by the character `tmp` followed by `(n - cnt - 1)` 'a' characters, and `tmp` is the character corresponding to the first unset bit in `cur` or an empty string if all bits are set.
#Overall this is what the function does:The function processes a series of test cases, where each test case is defined by integers `n`, `k`, and `m`, and a string `s` of length `m` consisting of the first `k` lowercase English alphabets. For each test case, the function checks if the string `s` can be divided into `n` segments such that each segment contains all `k` distinct characters. If possible, it prints "YES". Otherwise, it prints "NO" followed by a modified version of `s` that includes the necessary characters to form `n` valid segments. After processing all test cases, the function ends with the state of the last test case preserved in the variables `n`, `k`, `m`, `s`, `cnt`, `ans`, and `cur`.

