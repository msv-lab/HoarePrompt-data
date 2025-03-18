#State of the program right berfore the function call: The input consists of multiple test cases. Each test case starts with two integers n and m (1 ≤ n ≤ 50, 1 ≤ m ≤ 5), where n is the number of problems in the bank and m is the number of upcoming rounds. This is followed by a string a of length n, consisting of characters from 'A' to 'G', representing the difficulties of the problems in the bank.
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
        
    #State: a series of integers, each representing the result of one test case.
#Overall this is what the function does:The function processes multiple test cases, each involving a set of problems with specified difficulties and a number of upcoming rounds. For each test case, it calculates and prints the number of additional problems needed to ensure that each difficulty level ('A' to 'F') is represented in at least the specified number of rounds.

