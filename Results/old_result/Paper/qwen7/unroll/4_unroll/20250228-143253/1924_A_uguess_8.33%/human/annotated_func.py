#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^5. For each test case, n and k are integers such that 1 ≤ n ≤ 26 and 1 ≤ k ≤ 26, and m is an integer such that 1 ≤ m ≤ 1000. The string s is a string of length m comprising only the first k lowercase English alphabets. Additionally, the sum of m and the sum of n over all test cases does not exceed 10^6.
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
        
    #State: All variables remain undefined, and the program's behavior depends on user input during each iteration of the loop. The program prints 'YES' or 'NO' followed by a string based on the input provided.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it reads integers \(t\), \(n\), \(k\), and \(m\), and a string \(s\) of length \(m\) consisting of the first \(k\) lowercase English alphabets. It then checks if the number of distinct substrings of \(s\) that contain all \(k\) characters is at least \(n\). If so, it prints 'YES'; otherwise, it prints 'NO' followed by a string constructed from the characters of \(s\) and the character 'a'. The function ensures that \(t\) is between 1 and \(10^5\), \(n\) and \(k\) are between 1 and 26, \(m\) is between 1 and 1000, and the sum of \(m\) across all test cases does not exceed \(10^6\).

