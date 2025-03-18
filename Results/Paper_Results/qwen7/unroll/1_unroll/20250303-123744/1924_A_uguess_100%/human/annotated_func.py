#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^5, n and k are integers such that 1 ≤ n, k ≤ 26, m is an integer such that 1 ≤ m ≤ 1000, and s is a string of length m comprising only the first k lowercase English alphabets.
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
        
    #State: Output State: t is the number of test cases, n is an integer such that 1 ≤ n ≤ 26, k is an integer such that 1 ≤ k ≤ 26, m is an integer such that 1 ≤ m ≤ 1000, and s is a string of length m comprising only the first k lowercase English alphabets. After executing the loop, for each test case, either 'YES' is printed indicating that at least n unique characters were found in the string s, or 'NO' is printed followed by a string ans which contains the first character that was missing from the last set of k characters needed to make the count of unique characters at least n, followed by 'a' repeated n - cnt - 1 times, where cnt is the count of unique characters found.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it takes an integer `t` (number of test cases), two integers `n` and `k` (representing the required number of unique characters and the set size respectively), an integer `m` (length of the string `s`), and a string `s` (comprising the first `k` lowercase English alphabets). It then checks if the string `s` contains at least `n` unique characters. If so, it prints 'YES'. Otherwise, it identifies the first missing character from the last set of `k` characters needed to reach `n` unique characters and constructs a result string consisting of this character followed by 'a' repeated `n - cnt - 1` times, where `cnt` is the count of unique characters found. The function does not return any value but prints the results for each test case.

