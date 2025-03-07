#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000. For each test case, n and m are integers such that 1 ≤ n ≤ 50 and 1 ≤ m ≤ 5. a is a string of length n consisting of characters from 'A' to 'G'.
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
        
    #State: t is 0, n and m are the values from the last iteration, s is the string from the last iteration, p is 'ABCDEF', hmp is the Counter object from the last iteration, and ans is the cumulative sum of ans values from all iterations.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a string `s` of length `n` and an integer `m`. It calculates and prints the minimum number of additions needed to ensure that each character from 'A' to 'F' appears in the string at least `m` times.

