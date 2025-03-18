#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000. For each test case, n and m are integers such that 1 ≤ n ≤ 50 and 1 ≤ m ≤ 5. The string a consists of n characters where each character is from 'A' to 'G'.
def func():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        
        s = input()
        
        ans = 0
        
        p = 'ABCDEFG'
        
        hmp = Counter(s)
        
        for i in p:
            if i not in hmp:
                ans += m
        
        for i in hmp:
            if hmp[i] < m:
                ans += m - hmp[i]
        
        print(ans)
        
    #State: The value of `ans` is the sum of `m - hmp[i]` for all keys `i` in the dictionary `hmp` where the value of `hmp[i]` is less than `m`.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads two integers \( n \) and \( m \), and a string \( a \) consisting of \( n \) characters from 'A' to 'G'. It then calculates the sum of \( m - \text{count}(i) \) for all unique characters \( i \) in the string \( a \) where the count of \( i \) is less than \( m \). Finally, it prints the calculated sum for each test case.

