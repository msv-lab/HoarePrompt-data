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
        
    #State: t is 0, ans is the cumulative sum of ans values calculated in each iteration.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a string `s` of length `n` and an integer `m`. It calculates and prints the minimum number of character additions required to ensure that each of the characters 'A' through 'F' appears at least `m` times in the string `s`.

