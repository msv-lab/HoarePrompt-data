#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000. For each test case, n and m are integers such that 1 <= n <= 50 and 1 <= m <= 5. a is a string of length n consisting of characters from 'A' to 'G'.
def func():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        
        s = input()
        
        ans = 0
        
        p = 'ABCDEF'
        
        hmp = Counter(s)
        
        for i in p:
            if i not in hmp:
                ans += m
        
        for i in hmp:
            if hmp[i] < m:
                ans += m - hmp[i]
        
        print(ans)
        
    #State: t is 0, n remains the same, m remains the same, s is the string from the last iteration, hmp is the Counter object for the last s, p is 'ABCDEF', and ans is the result of the last iteration.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads two integers `n` and `m`, and a string `a` of length `n` consisting of characters from 'A' to 'G'. It then computes and prints the minimum number of changes required to ensure that each of the characters 'A' to 'F' appears at least `m` times in the string `a`.

