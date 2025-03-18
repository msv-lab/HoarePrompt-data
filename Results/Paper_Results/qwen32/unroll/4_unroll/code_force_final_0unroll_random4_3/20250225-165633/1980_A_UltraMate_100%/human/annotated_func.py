#State of the program right berfore the function call: The function `func` will receive a list of test cases. Each test case consists of two integers `n` and `m` (1 ≤ n ≤ 50, 1 ≤ m ≤ 5) representing the number of problems in the bank and the number of upcoming rounds, respectively, followed by a string `a` of length `n` consisting of characters from 'A' to 'G' representing the difficulties of the problems in the bank. The function will process each test case independently.
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
        
    #State: A series of integers, each representing the total number of additional problems needed for each test case.
#Overall this is what the function does:The function processes a series of test cases, each consisting of the number of problems in a bank, the number of upcoming rounds, and a string representing the difficulties of the problems. For each test case, it calculates and prints the total number of additional problems needed to ensure that each difficulty level from 'A' to 'G' is represented in at least as many problems as there are upcoming rounds.

