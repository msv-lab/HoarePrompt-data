#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^5. For each test case, n and k are positive integers such that 1 ≤ n ≤ 26 and 1 ≤ k ≤ 26, and m is a positive integer such that 1 ≤ m ≤ 1000. The string s in each test case consists only of the first k lowercase English alphabets. Additionally, the sum of m and the sum of n over all test cases does not exceed 10^6.
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
        
    #State: Output State: The loop has executed all iterations, and the final output state depends on the values of `t`, `n`, `k`, `m`, and the string `s`. Here's a detailed description:
    #
    #- `t` is the initial input integer, representing the number of test cases.
    #- After processing all test cases, for each test case:
    #  - `n` is the number of times the pattern needs to appear.
    #  - `k` is the length of the pattern.
    #  - `m` is not used in the provided code and can be ignored.
    #  - `s` is the input string that was processed.
    #  - `cnt` is the count of times the pattern `(1 << k) - 1` was fully formed in the string `s`.
    #  - `cur` is the current bitmask value, which tracks the characters seen so far.
    #  - `tmp` is a temporary string used to store the last incomplete pattern.
    #  - `ans` is the final answer string, constructed based on whether `cnt` meets or exceeds `n`.
    #
    #If `cnt` is greater than or equal to `n`, the output is 'YES'. Otherwise, the output is 'NO' followed by a string `ans` constructed as follows:
    #- A string of length `cnt` where each character is `chr(ord('a') + k - 1)`.
    #- Followed by `tmp`, which is either an empty string or 'a' + `2k-1`.
    #- Followed by 'a' repeated `n - cnt - 1` times if `cnt` is less than `n`.
    #- Or 'a' repeated `n - 1` times followed by `tmp` if `cnt` is greater than or equal to `n`.
    #
    #The final output will be a series of 'YES' or 'NO' answers followed by the corresponding `ans` strings for each test case.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it accepts integers \( t \), \( n \), \( k \), and a string \( s \). It checks if the string \( s \) contains a pattern of length \( k \) at least \( n \) times. If the pattern appears at least \( n \) times, it prints 'YES'; otherwise, it prints 'NO' followed by a constructed string based on the pattern's occurrences and the remaining required characters.

