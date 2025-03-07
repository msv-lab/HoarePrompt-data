#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^5, n is an integer such that 1 <= n <= 26, k is an integer such that 1 <= k <= 26, m is an integer such that 1 <= m <= 1000, and s is a string of length m comprising only of the first k lowercase English alphabets. Additionally, the sum of m and the sum of n over all test cases does not exceed 10^6.
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
        
    #State: `t` is 0, `i` is `t - 1`, `n`, `k`, and `m` are input integers, `s` is a non-empty input string, `cnt` is the number of times the loop has encountered a sequence of `k` unique characters in `s` for all iterations, `cur` is 0 if the loop has reset it due to reaching `(1 << k) - 1` in the last iteration, otherwise `cur` is the bitwise OR of the differences between the ASCII values of the characters in `s` and the ASCII value of 'a' for the last iteration, `ans` is a string that, if `cnt` is less than `n`, consists of `cnt` repetitions of the character `chr(ord('a') + k - 1)`, followed by the character `tmp` (which is the last character in the alphabet that has a corresponding bit in `cur` set to 0), and then `(n - cnt - 1)` repetitions of the character `'a'`. If `cnt` is greater than or equal to `n`, `ans` is not modified, and the program prints 'YES' for each iteration where `cnt` >= `n`.
#Overall this is what the function does:The function reads an integer `t` indicating the number of test cases. For each test case, it reads three integers `n`, `k`, and `m`, and a string `s` of length `m` consisting of the first `k` lowercase English alphabets. The function checks if the string `s` contains at least `n` sequences of `k` unique characters. If it does, the function prints 'YES'. If it does not, the function prints 'NO' followed by a string of length `n` that is constructed to contain exactly `n` sequences of `k` unique characters, based on the characters in `s`. The function does not return any value; it only prints the results. After processing all test cases, the function concludes, and the state of the program is that `t` is 0, `i` is `t - 1`, and the variables `n`, `k`, `m`, `s`, `cnt`, `cur`, and `ans` are in their final states as described in the annotations.

