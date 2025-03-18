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
        
    #State: Output State: t is an input integer, n and k are integers such that 1 ≤ n, k ≤ 26, m is an integer such that 1 ≤ m ≤ 1000, and s is a string of length m comprising only the first k lowercase English alphabets. After executing the loop, cnt is an integer representing the number of times the condition `cur == (1 << k) - 1` was met, cur is an integer used to track the current combination of characters, ans is a string built from characters that form a complete combination, and if cnt is less than n, ans is modified to include additional 'a' characters and a missing character to meet the count n.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads an integer \( t \), followed by \( t \) sets of values \( n \), \( k \), and \( m \), and a string \( s \) of length \( m \) consisting of the first \( k \) lowercase English alphabets. It then checks if the string \( s \) contains at least \( n \) distinct combinations of \( k \) characters. If it does, it prints "YES". Otherwise, it identifies a missing character and constructs a new string with \( n \) characters, including the missing one, and prints "NO" followed by this new string.

