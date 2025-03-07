#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^5, n and k are integers such that 1 ≤ n ≤ 26 and 1 ≤ k ≤ 26, m is an integer such that 1 ≤ m ≤ 1000, and s is a string of length m comprising only the first k lowercase English alphabets. Additionally, the sum of m and the sum of n over all test cases does not exceed 10^6.
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
        
    #State: Output State: The loop has executed all its iterations, meaning `i` is equal to the length of the input string `s`. `t` is reduced by a total of 15 if `cnt` is greater than or equal to `n`, otherwise it is reduced by 9. `cur` is `(1 << k) - 1` if `cnt` is less than `n`, and `0` if `cnt` is greater than or equal to `n`. `ss` is the last character in the string `s` after the loop has executed. `cnt` is the total number of times `cur` reached `(1 << k) - 1`. `tmp` holds the character 'a' if `cnt` is less than `n`, and is empty if `cnt` is greater than or equal to `n`. `ans` is constructed as follows: if `cnt` is less than `n`, `ans` is the character `chr(ord('a') + k - 1)` repeated `cnt` times plus `tmp` plus 'a' repeated `n - cnt - 1` times. If `cnt` is greater than or equal to `n`, `ans` is simply 'YES'.
#Overall this is what the function does:The function processes multiple test cases, each defined by integers \( t \), \( n \), \( k \), and \( m \), and a string \( s \). For each test case, it counts how many times a specific pattern (formed by the first \( k \) lowercase English letters) appears in the string \( s \). If the count is at least \( n \), it prints 'YES'. Otherwise, it constructs and prints a string consisting of the last used letter in the pattern, followed by the remaining required letters to reach \( n \) occurrences, and fills the rest with 'a'.

