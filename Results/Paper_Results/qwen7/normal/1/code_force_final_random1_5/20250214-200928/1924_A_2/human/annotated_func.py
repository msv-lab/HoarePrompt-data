#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^5. For each test case, n and k are integers such that 1 ≤ n ≤ 26 and 1 ≤ k ≤ 26, and m is an integer such that 1 ≤ m ≤ 1000. The string s is a string of length m comprising only the first k lowercase English alphabets.
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
        
    #State: Output State: The loop will have executed `t` times, where `t` is the initial value read from input. After all iterations, the following conditions will hold:
    #
    #- `cur` will be 0, as it is reset to 0 at the start of each iteration.
    #- `t` will be the same as the initial value read from input.
    #- `i` will be `t`, indicating that the loop has completed all its iterations.
    #- `n`, `k`, and `m` will retain their last values from the final iteration's input.
    #- `s` will be the string input in the last iteration.
    #- `cnt` will be the count of times `cur` reached `(1 << k) - 1` during all iterations. This count can vary depending on the input strings but will be non-negative.
    #- `ans` will be constructed based on the conditions met during all iterations. If `cnt` is greater than or equal to `n`, `ans` will be the string `s` with certain characters removed according to the conditions. Otherwise, `ans` will be modified to include additional characters 'a' and possibly 'b' to meet the condition `cnt >= n`.
    #
    #In summary, after all iterations, `cur` will be 0, `t` will be the same as the initial input, `i` will be `t`, `n`, `k`, and `m` will be the values from the last iteration, `s` will be the last input string, `cnt` will reflect the total occurrences of the condition `(1 << k) - 1`, and `ans` will be the final constructed string based on the given rules.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads integers \( n \), \( k \), and \( m \), and a string \( s \). It then constructs a new string \( ans \) based on the following rules: if the number of times a specific pattern (represented by `cur`) is fully formed (i.e., `cur` equals \( 2^k - 1 \)) is at least \( n \), it prints "YES" followed by the string \( s \) with the pattern removed. Otherwise, it prints "NO" followed by a modified version of \( s \) that includes additional 'a' characters to ensure the pattern count meets the requirement. The function outputs the results for all test cases.

